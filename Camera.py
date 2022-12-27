
From tkinter import *
From deepface import Deepface
Import imutils
Import cv2

def speak(text):
  engine=
  engine.
  engine.RunAndWait()
  

def video():
  Cam=cv2.videocapture(0)
  fourcc=cv2.videowriter_fourcc('XVID')
  Out=cv2.videowriter('output',fourcc,20(fps))
  While(True):
    ret,frame=Cam.read()
    cv2.imshow('frame',frame)
    if ret==true:
      Out.write(frame)
  Out.release()
  Cam.release()
  cv2.destroyAllWindow()

def capture():
  Cap_save=Top-level
  name=(nam+'jpg')
  Capt=cv2.imread(name,1)
  Read=Deepface.analyze(Capt,action['age','gender','emotion'])
  


Camera=Tk()
Camera.title("next gen")
Camera.geometry('400x350')
Camera.minsize(400,350)
Camera.maxsize(800,550)

#frame creation
Frame_camera=Frame(Camera)
Cam=cv2.videocapture(0)
  While(True):
    ret,frame=cam.read()
    cv2.imshow(Frame_camera,frame)
Cam.release()
cv2.destroyAllWindow()



Frame_bottom=Frame(Camera)
# Button list
Button_click=RoundButton(Frame_bottom,text="Cap",bg='yellow',command=capture)
Button_rec=RoundButton(Frame_bottom,text="Rec",bg='red',command=video)

Button_click.pack()
Button_rec.pack()

Frame_side=Frame(Camera)

Frame_bottom.pack(side=bottom)
Frame_side.pack(side=left)
Frame_camera.pack()

Camera.mainloop()
