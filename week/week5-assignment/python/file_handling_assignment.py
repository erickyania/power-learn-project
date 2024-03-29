# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("First line\n")
        file.write("Second line with numbers: 12345\n")
        file.write("Third line with special characters: !@#$%\n")
    print("File 'my_file.txt' created successfully.")
except PermissionError:
    print("Permission denied. Unable to create the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Fourth line appended\n")
        file.write("Fifth line appended\n")
        file.write("Sixth line appended\n")
    print("Content appended to 'my_file.txt' successfully.")
except PermissionError:
    print("Permission denied. Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.\n")

# Error Handling
try:
    # Attempt to open a non-existent file for reading
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Error handling process completed.")
