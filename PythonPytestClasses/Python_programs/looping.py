count=1
while count<=5:
    print(count)
    count+=1


#Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89

def calculate_grade(score):
    if 90 <= score < 100:
        return 'A'
    elif 80 <= score < 89:
        return 'B'
    elif 70 <= score < 79:
        return 'C'
    elif 60 <= score <69:
        return 'D'

score=int(input("Enter score:\n"))
Grade=calculate_grade(score)
print(f'the letter grade for the {score} is :{Grade}')

