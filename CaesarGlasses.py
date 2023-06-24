# Caesar Shift by Maddhu

#Encryption
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

#Decryption
def decrypt(text,s):
    result = ""

    #traverse text
    for i in range(len(text)):
        char = text[i]

        #Decrypt uppercase
        if(char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    
    return result


#Run Program
while True:
    #Select Operation with validation
    while True:
        ops = int(input("Select an operation, [1] = Encryption || [2] = Decryption: "))
        if ops > 0 and ops > 2:
            print("Please Enter 1 or 2")
        else:
            break

    text = input("Enter text: ")
    s = int(input("Shift Value: "))
    
    if ops == 1:
        enc = encrypt(text,s)
        print ("Cipher: " + enc)
    else:
        dec = decrypt(enc,s)
        print("Plaintext: "+ dec)
    
    #Continue for new cypher with validation
    while True:
        cond = input("Do you wish to continue? [Y/N]: ")
        if cond == "Y" or cond == "y" or cond == "N" or cond == "n":
            break
        else:
            print("Please enter Y or N")


    if  cond == "N" or cond == "n":
        break
    else:
        continue
    
    
