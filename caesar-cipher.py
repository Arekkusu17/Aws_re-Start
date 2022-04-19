"""
Write a program that implements a Caesar cipher, 
which is a simple method of encryption. A Caesar cipher takes the letters of a message
and shifts each letter along the alphabet by a certain number of places.
"""

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
def encryptMessage(message,cipherkey,alphabet):
    encryptedMessage=""
    uppercaseMessage=""
    uppercaseMessage=message.upper()
    for currentCharacter in uppercaseMessage:
        position=alphabet.find(currentCharacter)
        newPosition=position+int(cipherkey)
        if currentCharacter in alphabet:
            encryptedMessage=encryptedMessage+alphabet[newPosition]
        else:
            encryptedMessage=encryptedMessage+currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()