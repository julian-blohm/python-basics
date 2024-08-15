# in 17 we saw 2d arrays, 3d arrays also exist (cubes)
# e.g. list of an entire school building with multiple classroms stacked on top of each other
# school is a list of lists which contain lists
# 3d array or cube
school = [
    [
        ["Ann0a", "B0ob", "Ca0rl", "Da0ve"],
        ["E0va", "0oe", "So0fie", "0Kim"],
        ["Cl0aire", "Sa0rah", "0Leo", "Z0oe"],
        ["T0im", "0Sam", "Ann0e", "Sa0sha"]
    ],
    [
        ["1Anna", "1Bob", "1Carl", "1Dave"],
        ["1Eva", "1Joe", "1Sofie", "1Kim"],
        ["1Claire", "1Sarah", "1Leo", "1Zoe"],
        ["1Tim", "1Sam", "1Anne", "1Sasha"]
    ],
    [
        ["2Anna", "2Bob", "2Carl", "2Dave"],
        ["2Eva", "2Joe", "2Sofie", "2Kim"],
        ["2Claire", "2Sarah", "Le2o", "Zo2e"],
        ["Ti2m", "S2am", "Ann2e", "Sa2sha"]
    ]
]

# lets find 1Leo
student = school[1][2][2] # second list, then third list, then third place in the list
print(student)