from ntpath import join
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter
from tkinter import filedialog
import os
import mapvdrawer
import handlers
from PIL import Image


wind=Tk()
wind.title("Localize Dz")
wind.configure(width=1250,height=700,bg="#142B6F")
f1 = font.Font(family='Roboto',size=14,weight= font.BOLD)
f2 = font.Font(family='Roboto',size=10,weight= font.BOLD)

line_style = ttk.Style()
line_style.configure("Line.TSeparator", background="#FED601")

separator = ttk.Separator(wind, orient='vertical',style='Line.TSeparator')
separator.place(relx=0.25, rely=0, relwidth=0.005, relheight=1)

#separator2 = ttk.Separator(wind, orient='horizontal')
#separator2.place(relx=0, rely=1, relwidth=0.005, relheight=1)
D={}
#active_img
def browsefunc1():
    filename = filedialog.askopenfilename(filetypes=[])
    pathlabel1.config(text = os.path.basename(filename))
    D[1]=handlers.get_exif_data(Image.open(filename))
    #print(D)

def browsefunc2():
    filename = filedialog.askopenfilename()
    pathlabel2.config(text = os.path.basename(filename))
    D[2]=handlers.get_exif_data(Image.open(filename))
    #print(D)

def browsefunc3():
    filename = filedialog.askopenfilename()
    pathlabel3.config(text = os.path.basename(filename))
    D[3]=handlers.get_exif_data(Image.open(filename))
    #print(D)
#def UploadAction(event=None):
##filename = filedialog.askopenfilename()
#print('Selected:', filename)

firstlabel=tkinter.Label(wind, text="Insert 3 images to geolocalize them",font=f2,bg='#142B6F',fg='#FED601')
firstlabel.place(relx=0.01,rely=0.015)

## les labels et les buttons de browse et clear
## first ones
pathlabel1= Label(wind,width=25, height=1,font=f2)
pathlabel1.place(relx=0.0, rely=0.07)
browsebutton1 = Button(wind, text = "Browse", command = browsefunc1,bg='#FED601',fg='#142B6F',font=f2)
browsebutton1.place(relx=0.16, rely=0.07)
def clear1():
    pathlabel1.configure(text='')
    D[1]={}
    
clearbutton1 = Button(wind, text = " Clear  ", command = clear1,bg='#FED601',fg='#142B6F',font=f2)
clearbutton1.place(relx=0.208, rely=0.07)
## second ones
pathlabel2= Label(wind,width=25, height=1,font=f2)
pathlabel2.place(relx=0.0, rely=0.14)
browsebutton2 = Button(wind, text = "Browse", command = browsefunc2,bg='#FED601',fg='#142B6F',font=f2)
browsebutton2.place(relx=0.16, rely=0.14)
def clear2():
    pathlabel2.configure(text='')
    D[2]={}

clearbutton2 = Button(wind, text = " Clear  ", command = clear2,bg='#FED601',fg='#142B6F',font=f2)
clearbutton2.place(relx=0.208, rely=0.14)
## third ones
pathlabel3= Label(wind,width=25, height=1,font=f2)
pathlabel3.place(relx=0.0, rely=0.21)
browsebutton3 = Button(wind, text = "Browse", command = browsefunc3,bg='#FED601',fg='#142B6F',font=f2)
browsebutton3.place(relx=0.16, rely=0.21)
def clear3():
    pathlabel3.configure(text='')
    D[3]={}
clearbutton3 = Button(wind, text = " Clear  ", command = clear3,bg='#FED601',fg='#142B6F',font=f2)
clearbutton3.place(relx=0.208, rely=0.21)
## clear all button
def clearlabels():
    clear1()
    clear2()
    clear3()
    D.clear()

clearall = Button(wind, text = " CLEAR ALL ", height=2, command = clearlabels,bg='#FED601',fg='#142B6F',font=f2)
clearall.place(relx=0.1, rely=0.29)

##Draw 
def drawmap():
    mapvdrawer.main()
drawper = Button(wind, text = " DRAW PEREMETRE ", height=2, command = drawmap,bg='#FED601',fg='#142B6F',font=f2)
drawper.place(relx=0.083, rely=0.36)

separator2= ttk.Separator(wind, orient='horizontal',style='Line.TSeparator')
separator2.place(relx=0.0, rely=0.99, relwidth=0.255, relheight=0.008)
separator3= ttk.Separator(wind, orient='horizontal',style='Line.TSeparator')
separator3.place(relx=0.0, rely=0.44, relwidth=0.255, relheight=0.008)

separator4= ttk.Separator(wind, orient='horizontal',style='Line.TSeparator')
separator4.place(relx=0.0, rely=0.0, relwidth=0.255, relheight=0.008)

imglist=[("image 1",0.028,1),("image 2",0.098,2),("image 3",0.168,3)]
imglabel=tkinter.Label(wind, text="Choose an Image to show thier information, plz",font=f2,bg='#142B6F',fg='#FED601')
imglabel.place(relx=0.01,rely=0.47)

v = tkinter.IntVar()
v.set(1)
def SelectChoice():
    get_info(v.get())
    #return v.get()
def get_info(image_num):
    longtitude_lb.configure(text=handlers.get_lat_lon(D[image_num])[0])
    latitude_lb.configure(text=handlers.get_lat_lon(D[image_num])[1])
    time_lb.configure(text=handlers.get_time(D[image_num]))

common_bg='#FFFFFF'
common_fg = '#142B6F'

for m, x, val in imglist:
    tkinter.Radiobutton(wind,text=m, variable=v, command=SelectChoice, value=val , font=f2,bg='#142B6F',fg='#FED601',selectcolor=common_fg ,activeforeground=common_fg,activebackground=common_bg,padx=15,pady=15).place(relx=x,rely=0.52)

frame = Frame(wind,width=1000,height=700)
frame.place(relx=0.26,rely=0.01)

def exiter():
    wind.destroy()
exitbutton = Button(wind, text = "   EXIT  ", height=2, command = exiter,bg='#FED601',fg='#142B6F',font=f2)
exitbutton.place(relx=0.1,rely=0.92)

##
log_label = Label(wind,text="       Longtitude", height=2,font=f2,bg='#142B6F',fg='#FED601')
log_label.place(relx=0.001,rely=0.6)
longtitude_lb= Label(wind,width=31, height=2,font=f2)

longtitude_lb.place(relx=0.07, rely=0.6)

lat_label = Label(wind,text="       Latitude", height=2,font=f2,bg='#142B6F',fg='#FED601')
lat_label.place(relx=0.001,rely=0.7)
latitude_lb= Label(wind,width=31, height=2,font=f2)
latitude_lb.place(relx=0.07, rely=0.7)

time_label = Label(wind,text="Time Captured", height=2,font=f2,bg='#142B6F',fg='#FED601')
time_label.place(relx=0.001,rely=0.8)
time_lb= Label(wind,width=31, height=2,font=f2)
time_lb.place(relx=0.07, rely=0.8)

##btn1 = tkinter.Button(wind, text='Insert', command=UploadAction)
#btn1.place(relx=0.85, rely=0.01)

#separator.pack(fill='y')

#btn1=Button(wind,text='Tester ',font=f,padx=11,pady=10,bg='#FED601',fg='#142B6F',command=debut)

##btn1.place(x=800,y=200)
#btn2=Button(wind,text='Quitter',font=f,padx=12,pady=10,bg='#FED601',fg='#142B6F',command=fin)
#btn2.place(x=800,y=270)

def excuter():
    wind.mainloop()
