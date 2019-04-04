import os

arr_students = os.listdir("arr_students")
cropped = os.listdir("cropped")


def insert(y):
    arr_students.insert(y, "cropped0.jpg")
    
for crp in arr_students:
    print(crp)
    y = arr_students.index(crp)
    del(arr_students[y])
    insert(y)
    print(y)


print(arr_students)
