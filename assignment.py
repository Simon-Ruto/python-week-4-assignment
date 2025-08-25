#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.


file='original.txt'
try:
    # Step 1: Read from the input file
    with open('original.txt', "r", encoding="utf-8") as infile:
        content = infile.read()

    # Step 2: Modify the content (example: convert to uppercase)
    modified_content = content.lower()

    # Step 3: Write the modified content to the new file
    new_filename='modified'
    with open(new_filename, "w", encoding="utf-8") as outfile:
        outfile.write(modified_content)

    print(f"Modified file has been written to '{new_filename}'")

except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

file_name=input("Enter the filename: ")


try:
    with open(file_name,"r") as file:
        content=file.read()
        print(content)
    print("Read succefully")

except FileNotFoundError:
    print("File not found")        