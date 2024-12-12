# https://www.py4e.com/html3/04-functions
# Exercise 7

# Constants
ERR_SCORE_RANGE = 'Score must be a float between 0.0 and 1.0.'

def get_score():
    try: 
        score = float(input('Input a score: '))
    except:
        print(ERR_SCORE_RANGE)
        score = float(input('Input a score: '))

    return score

def check_score(score):
    if (((score >= 0) and (score <= 1.0)) == False):
        return False
    
    return True

def compute_grade(score):
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

    return grade

############
### MAIN ###
############

score = get_score()
while (check_score(score) != True):
    print(ERR_SCORE_RANGE)
    score = get_score()

grade = compute_grade(score) 

print(f"Score: {score} is grade: {grade}")