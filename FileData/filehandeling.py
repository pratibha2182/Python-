'''

Python’s built-in open() function lets you work with files.
open(filename, mode)
Mode                Meaning
"r"                 Read (default) – file must exist
"w"	                Write – overwrites file (creates if not exists)
"a"	                Append – adds content at end
"x"	                Create – fails if file exists
"rb"	            Read in binary mode
"wb"	            Write in binary mode



# Read entire file
with open("okay", "r") as f:
    content = f.read()
    print(content)

# Read first 10 characters
with open("okay", "r") as f:
    content = f.read(10)
    print(content)


# Read line by line
with open("okay", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("okay", "r") as f:
    # lines = f.readlines() #it will give whole in list form 
    lines = f.readline(2)  # it will only read the first entered character
    print(lines)


# Write (overwrites existing content)
with open("FileData/example.txt", "w") as f:  # if file is not avaiable will create a new file 
    f.write("Hello, Python!\n")
    f.write("This will overwrite the file.\n")
    f.write("Hello, Python!\n")

# Append (adds to existing content)
with open("FileData/example.txt", "a") as f:
    f.write("This line is added at the end.\n")

# Reading binary (image, pdfs)
with open("FileData/image.jpg", "rb") as f:
    data = f.read()

Best Practice: with Statement
Closes the file automatically after use
Avoids memory leaks
'''
