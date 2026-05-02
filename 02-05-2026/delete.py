# Create a list of dictionaries to store student records

# ====== Initial Data =======

students = [
    {"id":101 , "name":"Alice" , "score":45},
    {"id":102 , "name":"Bob" , "score": 78},
    {"id":103 , "name":"Charlie" , "score":92}
]

# Print the name of each student using a loop

print("Student Names:")
for s in students:
    print(s["name"])


# Print the average score of all students


total = 0

for s in students:
    total += s["score"] # total = total + 85 total = 0 + 85 total = 85
                        # total = total + 78 total = 85 + 78 = 163
avg = total / len(students)                        # total = total + 78 total = 163 + 92 = 255 / 3 = 85
print("\n Average Score:" , avg)

# Add a new student record to the list

students.append({"id":104 , "name":"John" , "score" : 75})

print("\nStudent List:" , students)

# Update the score of a student with ID 102 to 88


for s in students:
    if s["id"] == 102:
        s["score"] = 88

print("Students List:" , students)

# Delete the record of the student named "Charlie"
'''
new_list = []

for s in students:
    if s["name"] != "Charlie":
        new_list.append(s)

students = new_list
'''
print("\nStudents List:" , students)

# Print names of students who scored more than 80

print("\n Student scoring more than 80:")

for s in students:
    if s["score"] < 80:
        print(s["name"])

# Sort the list of students by score (descending)

def get_score(student):
    return student["score"]

students.sort(key = get_score , reverse = True)

print("\n Sorted by score (Desc):")

for s in students:
    print(s)

# Find the student with the highest score

max_score = max(student["score"] for  student in students)

top_student = [s for s in students if s["score"] == max_score]

print("\n\ntop_student:" , top_student)
'''
#  Use a loop to create a report in this format:
  - Name: Alice | Score: 85 | Grade: B
   (Add grading logic: A = 90+, B = 80–89, C = <80)
'''

print("Student Report:")

def get_report(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

for s in students:
    grade = get_report(s["score"])
    print("Name:" , s["name"] , "| Score:" , s["score"] , "|grade:" , grade)


#  Count how many students got each grade

grade_count = {"A":0 , "B":0 , "C":0}

for s in students:
    grade = get_report(s["score"])
    grade_count[grade]+=1

print("\n Grade count:" , grade_count)
    



                        
