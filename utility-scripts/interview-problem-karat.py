'''
Interview Question (Karat)
You are a developer for a university. Your current project is to develop
a system for students to find courses they share with friends. The
university has a system for querying courses students are enrolled in,
returned as a list of (ID, course) pairs.

Write a function that takes in a list of (student ID number, course name)
pairs and returns, for every pair of students, a list of all courses
they share.

Sample Input:
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

Sample Output (pseudocode, in any order):
find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
}

Additional test cases:

Sample Input:
student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

Sample output:
find_pairs(student_course_pairs_2) =>
{
  [0, 42]: []
  [0, 9]: []
  [9, 42]: []
}
'''

################
### SOLUTION ###
################

from collections import defaultdict
from itertools import combinations

# # Only returns pairs with matches, no empty pairs
# def walk_lists(course_dic, student_set): 
#     output = defaultdict(list)
#     students = list(student_set)
#     num_students = len(students)
#     classes = list(course_dic.keys())

#     for c in classes:
#       for i in range(num_students-1):
#           # print(students[i], students[i+1])
#           for j in range(i+1, num_students):
#               if (students[i] in course_dic[c]) and \
#                  (students[j]in course_dic[c]):
#                   output[(students[i], students[j])].append(c)

#     return output  

# Returns empty lists and matching lists
def walk_lists(course_dic, student_set): 
    output = dict()
    students = list(student_set)
    student_pairs = combinations(students, 2)
    classes = list(course_dic.keys())
    
    for sp in student_pairs:
        output[(sp[0], sp[1])] = []
        for c in classes:
          if (sp[0] in course_dic[c]) and (sp[1] in course_dic[c]):
              output[(sp[0], sp[1])].append(c)

    return output  


def parse_data(input_list):
    courses = defaultdict(list)
    students = set()

    for pair in input_list:
        courses[pair[1]].append(pair[0])
        students.add(pair[0])

    return courses, students

############
### MAIN ###
############

if __name__ == "__main__":
    course_pairs_lists = [ 
      [["58", "Software Design"],["58", "Linear Algebra"],["94", "Art History"],
       ["94", "Operating Systems"],["17", "Software Design"],["58", "Mechanics"],
       ["58", "Economics"],["17", "Linear Algebra"],["17", "Political Science"],
       ["94", "Economics"],["25", "Economics"]],
      [["42", "Software Design"],["0", "Advanced Mechanics"],
       ["9", "Art History"]]
    ] 


for pairs_list in course_pairs_lists:
    courses, students = parse_data(pairs_list)
    pairs = walk_lists(courses, students) 
    for k,v in pairs.items():
        print(f"{list(k)}: {v}")
    print()    
