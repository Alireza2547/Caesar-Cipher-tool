chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print("\nEncode: 1\nDecode: 2\nCrack: 3\nExit: 4")
enorde= int(input("enter your choice: "))
print("\n")
while True:
    if enorde == 1:
        plain_text = input("Enter you'r plain text: ")
        key = int(input("Enter your key: "))
        print("****your encode is : ****\n")
        plain_text = plain_text.lower()
        for i in plain_text:
            if i == " ":
                print(" ", end="")
            if i in chars:
                number = chars.find(i)
                num = number+(key)
                ciphertext = (chars[num])
                print(ciphertext, end="")
        print("\n")
        
    if enorde == 2:
        plain_text = input("Enter you'r decryption: ")
        key = int(input("Enter your key: "))
        print("****your decode is : ****\n")
        plain_text = plain_text.lower()
        for i in plain_text:
            if i == " ":
                print(" ", end="")
            if i in chars:
                number = chars.find(i)
                num = number+(-key)
                ciphertext = (chars[num])
                print(ciphertext, end="")
        print("\n")
        
        
    if enorde == 3:
        encoded_code = input("Enter your decryption: ")
        encoded_code = encoded_code.lower()
        print("****your crack is : ****\n")
        for key in range(-26,26):
            
            for i in encoded_code:
                if i == " ":
                    print(" ", end="")
                if i in chars:
                    find_num = chars.find(i)
                    find_num = find_num - key
                    print(chars[find_num],end="")
            print(" ",key,"      ")
    print("\nEncode: 1\nDecode: 2\nCrack: 3\nExit: 4")
    enorde= int(input("Enter your choice: "))
