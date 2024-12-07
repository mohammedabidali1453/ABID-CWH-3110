#Write a program that checks if a given number is positive, negative, or zero. If it's positive, print "Positive number." If it's negative, print "Negative number." If it's zero, print "Zero.
num= int(input('Enter a number: '))
if num>0:
    print('Entered number is Postive')
elif num==0:
    print('Entered number is Zero')    
else:
    print('Entered number is Negative')    
  


#Create a program that takes a student's exam score as input. Classify the student's performance as follows: If the score is greater than or equal to 90, print "A" If the score is between 80 and 89, print "B" If the score is between 70 and 79, print "C" If the score is between 50 and 69, print "D"  If the score is below 50, print "F"
score = int(input('Enter your Score: '))
if score>=90:
    print('\'A\' Grade')
elif score>=80 and score<90:
    print('\'B\' Grade') 
elif score>=70 and score<80:
    print('\'C\' Grade') 
elif score>=60 and score<70:
    print('\'D\' Grade') 
else:
    print('\'F\' Grade')    
