#String Concatenation 
str1= input('Enter first string: ')
str2= input('Enter second string: ')
result= str1 + str2
print(f"Concatenation of {str1} and {str2} is {result}")

#String Reversing
a = input('Enter the string that you want to revese: ')
rev= a[::-1]
print('Reversed string is: 'rev)

#Length of the string 
str = input('Enter a string: ')
length=len(str)
print('Length of the given string is: ',length)

#Upper and Lower Case
str= input('Enter a String: ')
upper= str.upper()
lower= str.lower()
print('The given string in upper case is: ',upper)
print('The given string in lower case is: ',lower)
