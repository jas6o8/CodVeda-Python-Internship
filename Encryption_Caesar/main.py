#this program encrypts a message using the caesar cipher method
import os
from docx import Document 

print("Welcome to the Caesar Cipher Program!")
letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)


def encrypt_decrypt(text, shift, mode):
    if mode == 'd':
        shift = -shift
    message = ""
    for char in text:
        lower_char = char.lower()
        index = letters.find(lower_char)

        if index == -1:
            # not a letter (space, punctuation, newline, digit) 
            message += char
        else:
            new_index = (index + shift) % num_letters
            shifted = letters[new_index]
            if char.isupper():
                shifted = shifted.upper()
            message += shifted

    return message

text=input("choose whether you want to encrypt or decrypt a message e/d: ")

if text =='e' or text == 'd':

    script_dir = os.path.dirname(os.path.abspath(__file__))#this gets the directory of the script
    inputfile = input("Enter the name of the input file (e.g., message.txt): ")
    inputpath = os.path.join(script_dir, inputfile)#looks for the file in the same directory as the script

    try:
        if inputfile.endswith('.docx'):
            doc = Document(inputpath)
            
            message = "\n".join([p.text for p in doc.paragraphs])
        else:
        
            with open(inputpath, "r") as f:
                message = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{inputfile}' was not found.")
        exit()

    outputfile=input("Enter the name of the output file (e.g., message.txt): ")
    outputpath = os.path.join(script_dir, outputfile)#creates the file in the same directory as the script
    shift=int(input("Enter the shift value (1-25): "))



    enc_dec=encrypt_decrypt(message,shift,text)

    with open(outputpath,"w") as f:
        f.write(enc_dec)

    print(f"result written to {outputfile}")
    

else:
    print("Invalid input. Please choose 'e' for encrypt or 'd' for decrypt.")

