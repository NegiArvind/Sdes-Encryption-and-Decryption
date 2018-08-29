# This program is used to encrypt and decrypt the data using des method

# message is of 64 bit size
messageText = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]

# key is of 64 bit size
key = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0,
       1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]

parityDrop = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]

compressionKeyBox = [14, 17, 11, 24, 1, 5,
                     3, 28, 15, 6, 21, 10,
                     23, 19, 12, 4, 26, 8,
                     16, 7, 27, 20, 13, 2,
                     41, 52, 31, 37, 47, 55,
                     30, 40, 51, 45, 33, 48,
                     44, 49, 39, 56, 34, 53,
                     46, 42, 50, 36, 29, 32]

expansionPBox = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

straightPBox = [16, 7, 20, 21,
                29, 12, 28, 17,
                1, 15, 23, 26,
                5, 18, 31, 10,
                2, 8, 24, 14,
                32, 27, 3, 9,
                19, 13, 30, 6,
                22, 11, 4, 25]
initialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

finalPermutation = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

sBox = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

keyAfterParity = 56 * [None]
keyLeft = 28 * [None]
keyRight = 28 * [None]
combineLeftRight = 56 * [None]
subKey = 48 * [None]
functionOutput = 32 * [None]


# This below method will apply Parity drop on given key
def applyParityDrop():
    for i in range(56):
        keyAfterParity[i] = key[parityDrop[i] - 1]

    keyLeft = keyAfterParity[:int(56 / 2)]  # Assign first 28 bit to keyLeft list
    keyRight = keyAfterParity[int(56 / 2):]  # Assign last 28 bit to keyRight list
    print(keyAfterParity)
    return keyLeft, keyRight;


# This below method will calculate all the sub keys
def calculateKey(keyType, keyLeft=[], keyRight=[]):
    if keyType == 1 or keyType == 2 or keyType == 9 or keyType == 16:
        # shift the keyLeft list to one bit left
        keyLeft = keyLeft[1::] + keyLeft[:1:]
        keyRight = keyRight[1::] + keyRight[:1:]

    else:
        # shift the keyLeft list to two bit left
        keyLeft = keyLeft[2::] + keyLeft[:2:]
        keyRight = keyRight[2::] + keyRight[:2:]

    combineLeftRight = keyLeft + keyRight  # combining left list and right list

    # Applying compression key box

    for i in range(48):
        subKey[i] = combineLeftRight[compressionKeyBox[i] - 1]
    return keyLeft, keyRight, subKey  # returning three list from this function


def CalculateFunction(roundType, messageHalf=[], keyLeft=[], keyRight=[]):
    afterExpansion = 48 * [None]

    for i in range(48):
        afterExpansion[i] = messageHalf[expansionPBox[i] - 1]

    if roundType == 1:
        keyLeft, keyRight = applyParityDrop()

    keyLeft, keyRight, subKey = calculateKey(roundType, keyLeft, keyRight)
    print("subkey--->",subKey)

    afterExpansion = [x ^ y for x, y in zip(afterExpansion, subKey)]

    functionResult = 32 * [None]

    afterSBoxString = ''
    afterSBoxList = 32 * [None]

    for i in range(0,48,6):
        stringCol = ''.join(str(afterExpansion[j]) for j in range(i + 1, i + 5))  # it will convert 4 bit into decimal
        col = int(stringCol, 2)  # converts binary string into decimal
        #print("col-- ",col)
        #print(i,i+5)
        stringRow = str(afterExpansion[i]) + str(afterExpansion[i + 5])
        row = int(stringRow, 2)  # cinverts binary string into decimal
        value = sBox[int(i / 6)][row][col]
        binaryString=bin(value).split('b', 1)[1];

        #padding zero at the start of binaryString
        binaryString=('0'*(4-len(binaryString)))+binaryString;
        afterSBoxString +=binaryString # bin(value) convert decimal value into binary.
        #print(afterSBoxString)
        #  it returns binary string(0b101 for 5)
        # 0b is appended by defalut with binaryString so we have to remove this 0b.That's why we have splited it from b.
        #print("iiii ",i);

    print(afterSBoxString,len(afterSBoxString))
    afterSBoxList = [int(x) for x in afterSBoxString]

    for j in range(32):
        functionResult[j] = afterSBoxList[straightPBox[j] - 1]

    return keyLeft, keyRight, functionResult;


xorResult = 32 * [None]

# Applying initial permutation
message = [messageText[x - 1] for x in initialPermutation]
cipherText=64*[None]

# Now Applying Round from 1 to 16
messageLeft = message[:32]
messageRight = message[32:]
finalResult=64*[None]
#print(messageRight)
for j in range(16):
    print("RoundNumber  ",j+1)
    if j < 15:
        keyLeft, keyRight, functionOutput = CalculateFunction(j+1,messageRight, keyLeft, keyRight)
        xorResult = [x ^ y for x, y in zip(messageLeft, functionOutput)]
        messageLeft = messageRight;
        messageRight = xorResult
    else:
        keyLeft, keyRight, functionOutput = CalculateFunction(j+1,messageRight, keyLeft, keyRight)
        xorResult = [x ^ y for x, y in zip(messageLeft, functionOutput)]
        print("XorResult",xorResult,len(xorResult))
        finalResult=xorResult+messageRight;
        cipherText = [finalResult[x-1] for x in finalPermutation]

print("CipherText--- >",cipherText)

# Now Decryption


