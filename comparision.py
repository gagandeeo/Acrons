import os
import face_recognition
import cv2

cropped=os.listdir("cropped")

arr_students=os.listdir("arr_students")
## global i

#original = cv2.imread("saved0.jpg")
#duplicate = cv2.imread("saved1.jpg")
for crp in cropped:
    picture_of_me = face_recognition.load_image_file("cropped/"+crp)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    for sid in arr_students:
        unknown_picture = face_recognition.load_image_file("arr_students/"+sid)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            print("PRESENT")
            
            
            ##PRESENT(y)
            
        else:
            print("UNKNOWN")
##for absent in student_id:
##    if student_id!="\\temp_image\\":
##        print("ABSENT")
##        ##ABSENT(student_id.index(absent))
                

