#Write a program that takes a sentence as input and extracts the substring between the 5th and 10th characters (inclusive). Print the extracted substring.

#The below  code is given
sentence = input("Enter a sentence: ")

# Check if the sentence has at least 10 characters
if len(sentence) >= 10:
    extracted_substring = sentence[4:10]  # Note: Python uses 0-based indexing
    print("Extracted Substring:", extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")

#As we are in slicing method, so i tried it by slicing method
str= input('Enter a string atleast more than 10 letters : ')
substr= str[6:11]
print('The sub string is: ',substr)


#Reversing a string
str=("Enter a string")
print("Reverse String is: ",str[::-1])

#string check
string = input("Enter a string: ")

print("Is the string alphanumeric?", string.isalnum())
print("Does the string contain only alphabets?", string.isalpha())
print("Does the string contain only digits?", string.isdigit())
print("Does the string contain only decimal characters?", string.isdecimal())
print("Does the string contain only numeric characters?", string.isnumeric())
print("Is the string entirely in lowercase?", string.islower())
print("Is the string entirely in uppercase?", string.isupper())
print("Does the string contain only spaces?", string.isspace())

#
input_string = "abracadabra"
# Counting occurrences of 'abra'
substring_count = input_string.count('abra')
# Displaying the result
print(f"The number of times 'abra' appears is: {substring_count}")
