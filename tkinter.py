from tkinter import *
import cv2
from PIL import Image
import os
import face_recognition
import xlwt
from xlwt import Workbook
from xlutils.copy import copy
from xlrd import *

wb = copy(open_workbook('ATTENDENCE.xlsx'))
sheet = wb.get_sheet(0)

z=3
c=0

y=0
counter = 0
i = 0

root = Tk()
message = StringVar()
message.set('SET DAY')

k=0
u=3

G = Label(root,text="SET DAY")
def press():
    global u
    G.config(text="DAY u")
        


##for z in range(3,22):
##    sheet.write(0,z,2)
def add_day():
    global u
    u+=1
    G.config(text="DAY %d"%u)
def subtract_day():
    global u
    u-=1
    G.config(text="DAY %d"%u)

def PRESENT(row,u):
    sheet.write(row+3,u,'P')
    wb.save('book5.xls')
    
def ABSENT(row,u):
    k=add_day.u
    sheet.write(row+3,u,'A')
    wb.save('book5.xls')    

def cropping():
    count = 0
    global counter
    frames=os.listdir("frames")
    for frame in frames:
        
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        img = cv2.imread("frames/"+frame)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        def crop(image_path, coords):
            global counter
            image_obj = Image.open(image_path)
            cropped_image = image_obj.crop(coords)
            cropped_image.save("cropped/cropped%d.jpg"% counter)
            counter+=1
                
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)   
            crop("frames/"+frame, (x,y,x+w,y+h))

        count+=1
    print("PROCEDURE HAS BEEN EXECUTED")

def initiate_attendance():

    global y
    global u

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

            if results[0] == True and sid!='cropped0.jpg':
            
                y = arr_students.index(sid)
                print("PRESENT")
                PRESENT(y-1,u)
                print(y)
                del(arr_students[y])
                arr_students.insert(y, "cropped0.jpg")
 
                
            elif (sid=="cropped0.jpg"):
                print("picture is cropped0")

            elif(results[0]!=True):
                print("unknown")
##for absent in student_id:
##    if student_id!="\\temp_image\\":
##        print("ABSENT")
##        ##ABSENT(student_id.index(absent))
    for absenties in arr_students:
        if(absenties!="cropped0.jpg"):
          
            print("ABSENT")
            l = arr_students.index(absenties)
            print(l)
            ABSENT(l-1,u)

            


root.geometry('720x720+50+50')
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.place(x=600,y=40)
detect_faces_button = Button(root, text='Detect Faces', command=cropping)
detect_faces_button.place(x=154,y=183)
initiate_attendance_button = Button(root,text='Initiate Attendance',command=initiate_attendance)
initiate_attendance_button.place(x=324,y=302)
add_day = Button(root,text='--->',command=add_day)
add_day.place(x=640,y=203)

subtract_day = Button(root,text='<---',command=subtract_day)
subtract_day.place(x=526,y=203)
b1 = Button(root, text = "DAY", command = press).pack()
G.place(x=578,y=206)

##e = Entry(root)
##e.pack()
##e.focus_set()
##k=e.get()
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)


root.mainloop()

