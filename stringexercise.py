# A program to demonstrate the use of string functions

text = "In Python Basics: Strings and String Methods, you used strings for text data in Python. You also learned how to  manipulate strings with string methods. For example, you changed strings from lowercase to uppercase, removed whitespace from the beginning or end of a string, and replaced parts of a string with different text. "

# Count the occurence of the following words in the text

print(f"String: {text.count('String')}")

print(f"Python: {text.count('Python')}")

print(f"Method: {text.count('Method')}")

#Replacing space characters with ->

print(text.replace(" ", "->"))

#dispalying the length of the text

print(f"Length of the text: {len(text)}")

#checking if print exists

print(f"finding print: {text.find('print')}")

print('print' in text) 
print(text.find("print"))