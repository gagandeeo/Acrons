import cv2
from PIL import Image
counter = 0

def cropping():
    count = 0

    global counter
    
        
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread("group.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    def crop(image_path, coords):
        global counter
        image_obj = Image.open(image_path)
        cropped_image = image_obj.crop(coords)
        cropped_image.save("cropped%d.jpg"% counter)
        cropped_image.show()
        counter+=1
            
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)   
        crop("group.jpg", (x,y,x+w,y+h))

    count+=1
            
    cv2.imshow("output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





 

 
