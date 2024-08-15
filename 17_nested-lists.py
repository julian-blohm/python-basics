# a list can contain more lists
# following would be a 2d Array, so a list that contains other lists
classroom = [
    ["Anna", "Bob", "Carl", "Dave"],
    ["Eva", "Joe", "Sofie", "Kim"],
    ["Claire", "Sarah", "Leo", "Zoe"],
    ["Tim", "Sam", "Anne", "Sasha"]
]
# let's get the student Sarah
student = classroom[2] # we have the entire row of students now
student_sarah = classroom[2][1] # we now have index 2 of the rows and index 1 in the row which is sarah
print(student_sarah)
print("")
