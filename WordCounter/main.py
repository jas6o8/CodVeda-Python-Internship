import os
from docx import Document 

script_dir = os.path.dirname(os.path.abspath(__file__))
inputfile = input("Enter the name of the input file (e.g., message.docx): ")
inputpath = os.path.join(script_dir, inputfile)

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
except Exception as e:
    
    print(f"Error reading file: {e}")
    exit()

word_count = len(message.split())
print(f"The number of words in the file '{inputfile}' is: {word_count}")