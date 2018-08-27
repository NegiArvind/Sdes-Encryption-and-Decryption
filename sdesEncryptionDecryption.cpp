#include<bits/stdc++.h>
using namespace std;
int key1[8],key2[8];
int ip[8]={2,6,3,1,4,8,5,7};
	int fp[8]={4,1,3,5,7,2,8,6};
	int expansionPBox[8]={4,1,2,3,2,3,4,1};
	int keyStraightPBox[10]={3,5,2,7,4,10,1,9,8,6};
    int compressionPBox[8]={6,3,7,4,8,5,10,9};
    int straightPBox[4]={2,4,3,1};
    int sBox1[4][4]={{1,0,3,2},
                   {3,2,1,0},
                   {0,2,1,3},
                   {3,1,3,2}};
    int sBox2[4][4]={{0,1,2,3},
                   {2,0,1,3},
                   {3,0,1,0},
                   {2,1,0,3}};

void calculateFunction(int temp[],int round)
{
     int expResult[8],straightTempIp[4];
     string binary[4]={"00","01","10","11"};
     int decimal[2][2]={{0,1},
                        {2,3}};
     int i;
     // cout<<"tmep=";
     // for(i=0;i<4;i++)
     // {
     //    cout<<temp[i];
     // }
     for(i=0;i<8;i++)
     {
        //cout<<"Box"<<expansionPBox[i]-1<<"\n";
     	expResult[i]=temp[expansionPBox[i]-1];
        //cout<<"ex"<<expResult[i]<<"\n";
        if(round==1)
     	    expResult[i]=expResult[i]^key1[i];
        else
            expResult[i]=expResult[i]^key2[i];
        //cout<<"exp="<<expResult[i]<<"\n";
     }

     //t1 is giving me row number whereas t2 giving me column number
     int t1=sBox1[decimal[expResult[0]][expResult[3]]][decimal[expResult[1]][expResult[2]]];
     int t2=sBox2[decimal[expResult[4]][expResult[7]]][decimal[expResult[5]][expResult[6]]];
     //cout<<"t1= "<<t1<<"t2= "<<t2;

     temp[0]=binary[t1][0]-48;
     temp[1]=binary[t1][1]-48;
     temp[2]=binary[t2][0]-48;
     temp[3]=binary[t2][1]-48;

     //Applying straightpBox
     for(i=0;i<4;i++)
     {
        straightTempIp[i]=temp[straightPBox[i]-1];
     }
     // cout<<"temp= ";
     for(i=0;i<4;i++)
     {
        temp[i]=straightTempIp[i];
        // cout<<temp[i];
     }
}

void leftShift(int temp[],int totalArray[],int start,int shiftBy)
{
  int j=0;
  for(int i=0;i<5;i++)
  {
    if(shiftBy+i<5)
    {
       temp[i]=totalArray[start+shiftBy+i];  
    }
    else
    {
      temp[i]=totalArray[start+j];
      j++;
    }
    cout<<temp[i]<<"";
  }
  cout<<"\n";
}

int main()
{
	int plainText[100],cipherText[100],givenKey[10],key[10],ipResult[8];
    int i;
	cout<<"Enter the plain text\n";
	for(i=0;i<8;i++)
	{
	    cin>>plainText[i];	
	}
	cout<<"Enter the key\n";
	for(i=0;i<10;i++)
	{
	    cin>>givenKey[i];	
	}

    //Generating the keys

    //Finding the key 1

    for(i=0;i<10;i++)
    {
    	key[i]=givenKey[keyStraightPBox[i]-1];
    }
    // for(i=0;i<10;i++)
    // {
    // 	// if(i==1)
    // 	// 	cout<<"keyafter";
    // 	cout<<key[i];
    // }
    int tempKey1[5],tempKey2[5];

    //This below is left shift by one on first 4 bit
    leftShift(tempKey1,key,0,1);
    
    // cout<<"tempkey1= ";
    // for(i=0;i<5;i++)
    // {
    // 	cout<<tempKey1[i];
    // }
    // cout<<"\n";

    //This below is left shift by one on last 4 bit
    leftShift(tempKey2,key,5,1);

    // cout<<"tempkey2= ";
    // for(i=0;i<5;i++)
    // {
    // 	cout<<tempKey2[i];
    // }
    // cout<<"\n";

    int tempCompressionBox[10];
    for(i=0;i<10;i++)
    {
    	if(i<5)
    	{
            tempCompressionBox[i]=tempKey1[i];
    	}
    	else
    	{
            tempCompressionBox[i]=tempKey2[i-5];
    	}
    }

    //Applying compression box on key1
    cout<<"Key1= ";
    for(i=0;i<8;i++)
    {
    	key1[i]=tempCompressionBox[compressionPBox[i]-1];
    	cout<<key1[i];
    }
    cout<<"\n";
    
    //Now finding key2

    //LeftShift first 4 digit by two
    leftShift(tempKey1,tempCompressionBox,0,2);

    //leftShift last 4 digit by two
    leftShift(tempKey2,tempCompressionBox,5,2);
    

    int tempCompressionBox2[10];
    for(i=0;i<10;i++)
    {
    	if(i<5)
    	{
            tempCompressionBox2[i]=tempKey1[i];
    	}
    	else
    	{
            tempCompressionBox2[i]=tempKey2[i-5];
    	}
    }

    //Applying compression box

    cout<<"Key2= ";
    for(i=0;i<8;i++)
    {
    	key2[i]=tempCompressionBox2[compressionPBox[i]-1];
    	cout<<key2[i];
    }
    cout<<"\n";


	//Applying initial permutation on the plain text
    
    for(i=0;i<8;i++)
    { 
    	ipResult[i]=plainText[ip[i]-1];
        // cout<<"result="<<ipResult[i];
    }
    int tempIp1[4],tempIp2[4],copyTempIp2[4],copyTempIp1[4],finalPermResult[8],permResult[8];


    //Now performing round1 operation here

    int functionResult[4];
    
    for(i=0;i<8;i++)
    {
    	if(i<=3)
    	{
    		tempIp1[i]=ipResult[i];
            //copyTempIp1[i]=tempIp1[i];
            // cout<<"tempip"<<tempIp1[i]<<"\n";
    	}
    	else
    	{
    		 tempIp2[i-4]=ipResult[i];
         copyTempIp2[i-4]=tempIp2[i-4];
    	}
    }

    //This below function will calculate the function for round1
    calculateFunction(tempIp2,1);
    
    // Apply straightpBox after applying s box
    for(i=0;i<4;i++)
    {

        //Also add it with temp1 value which we are getting after breaking result of initial permutation
        tempIp1[i]^=tempIp2[i];
        copyTempIp1[i]=tempIp1[i];
    }

    //Now applying round 2 here

    //Calculating function value after swaping
    calculateFunction(tempIp1,2);
    for(i=0;i<4;i++)
    {
        copyTempIp2[i]^=tempIp1[i];
    }

    for(i=0;i<8;i++)
    {
       if(i<=3)
       {
          permResult[i]=copyTempIp2[i];
          //cout<<"perm"<<permResult[i];
       }
       else
       {
          permResult[i]=copyTempIp1[i-4];
          //cout<<"perm"<<permResult[i];
       }
    }

    //Now applying final permutation
    cout<<"Cipher Text = ";
    for(i=0;i<8;i++)
    {
        finalPermResult[i]=permResult[fp[i]-1];
        cipherText[i]=finalPermResult[i];
        cout<<finalPermResult[i];
    }
    cout<<"\n";





    /** Now performing Decryption here **/

    




    //first performing initialPermutation(As we have to use the inverse of finalPermutation)

    for(i=0;i<8;i++)
    { 
      ipResult[i]=cipherText[ip[i]-1];
        // cout<<"result="<<ipResult[i];
    }

    //First applying round2

    for(i=0;i<8;i++)
    {
      if(i<=3)
      {
        tempIp1[i]=ipResult[i];
            //copyTempIp1[i]=tempIp1[i];
            // cout<<"tempip"<<tempIp1[i]<<"\n";
      }
      else
      {
        tempIp2[i-4]=ipResult[i];
        copyTempIp2[i-4]=tempIp2[i-4];
      }
    }

    //This below function will calculate the function for round2
    calculateFunction(tempIp2,2);
    
    // Apply straightpBox after applying s box
    for(i=0;i<4;i++)
    {

        //Also add it with temp1 value which we are getting after breaking result of initial permutation
        tempIp1[i]^=tempIp2[i];
        copyTempIp1[i]=tempIp1[i];
    }



    //Now applying round 1 here

    //Calculating function value after swaping
    calculateFunction(tempIp1,1);
    for(i=0;i<4;i++)
    {
        copyTempIp2[i]^=tempIp1[i];
    }

    for(i=0;i<8;i++)
    {
       if(i<=3)
       {
          permResult[i]=copyTempIp2[i];
          //cout<<"perm"<<permResult[i];
       }
       else
       {
          permResult[i]=copyTempIp1[i-4];
          //cout<<"perm"<<permResult[i];
       }
    }

    //Now applying final permutation
    cout<<"Original Text = ";
    for(i=0;i<8;i++)
    {
        finalPermResult[i]=permResult[fp[i]-1];
        //cipherText[i]=finalPermResult[i];
        cout<<finalPermResult[i];
    }
    cout<<"\n";

}