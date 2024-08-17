import random
import pandas
#list comprehension 
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
#print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
#print(letters_list[3:])

range = range(1, 5)
range_list = [double_range * 2 for double_range in range]
#print(range_list)

#Conditional List Comprehension 
#new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
#print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
#print(long_names)

students_scores = {student:random.randint(1, 100) for student in names}

#passed_students = {pass_student: student_score[pass_student] for pass_student in student_score if student_score[pass_student] > 60}
students = [student for (student, score) in students_scores.items()]
scores = [score for (student, score) in students_scores.items()]
students_score = {
    "students": students,
    "scores": scores
    }

students_data = pandas.DataFrame(students_score)
print(students_data)

#Loop through a data frame 
#for (key, value) in student_data_frame.items():

#Loop through rows of a data frame 
for (index, row) in students_data.iterrows():
    if row.students == "Freddie":
        print(row.scores)