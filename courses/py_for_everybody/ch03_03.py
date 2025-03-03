# https://www.py4e.com/html3/03-conditional
# Exercise 3

grade = ''
score = -1
input_error_msg = 'Score must be a float between 0.0 and 1.0.'

# Catch input type error
try: 
    score = float(input('Input a score: '))
except:
    print(input_error_msg)
    score = float(input('Input a score: '))

# Bad range isn't an exception 
while (((score >= 0) and (score <= 1.0)) == False):
    print(input_error_msg)
    try: 
        score = float(input('Input a score: '))
    except:
        score = float(input('Input a score: '))

# Print grade
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score} is grade: {grade}")