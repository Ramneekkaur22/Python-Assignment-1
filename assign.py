# 1. 
import keyword
print("Python Keywords:")
print(keyword.kwlist)

# 2. 

x = 10
print("Value:", x)
print("Type:", type(x))

# 3. 

numbers = (10, 20, 30, 40)
print("Last Element:", numbers[-1])
print("Second Element:", numbers[1])

# 4. 

num = int("123")
result = num + 10
print("Result:", result)

# 5. 

num = 45.89
integer_num = int(num)
print("Float:", num)
print("Integer:", integer_num)

#6. 

str1 = "Hello"
str2 = "World"

new_string = str1 + " " + str2
print("Joined String:", new_string)
print("Length:", len(new_string))

#7. 

flag = True
print("Value:", flag)
print("Type:",type(flag))

# 8. 

t = (10, 20, 30, 40, 50)
print("Length of Tuple:", len(t))

# 9. 

language = "Python"
version = 3.13
result = language + str(version)
print(result)

# 10. 

student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course = input("Enter Course Name: ")

marks1 = float(input("Enter Marks in Subject 1: "))
marks2 = float(input("Enter Marks in Subject 2: "))
marks3 = float(input("Enter Marks in Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n----- Student Details -----")
print("Name:", student_name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Percentage:", percentage)

# 11

subjects = ["Python", "SQL", "Excel", "Tableau"]

# a.
print("Complete List:", subjects)

# b.
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# c. 
subjects.insert(1, "Java")
print("After Inserting Java:", subjects)

# d. 
subjects.remove("Excel")
print("After Removing Excel:", subjects)

# e.
new_subjects = subjects.copy()
print("Copied List:", new_subjects)

# f. 
new_subjects.sort()
print("Sorted List:", new_subjects)

# g. 
print("Is Excel Present?", "Excel" in subjects)

# 12. 

attendance = True
assignment_submitted = False

# a. 
print("attendance or assignment_submitted =", attendance or assignment_submitted)

# b. 
print("attendance and assignment_submitted =", attendance and assignment_submitted)

# c. 
print("not attendance =", not attendance)