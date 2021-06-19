from tkinter import Tk,Entry,NW,Button,Label,filedialog
from PIL import ImageTk, Image
from mainfunc import*


def vp_start_gui():
    global window
    window=Tk()
    
    
    window.title('VPD')
    window.geometry("700x500+150+150")
    
    
    window.columnconfigure(0,weight=2)
    window.configure(bg='#1f666b')
    
    ent1=Entry(window,font=40,width=60,bd=4)
    #nt1.grid(row=2,column=2)
    #ent1.pack(expand=True,pady=10)
    ent1.place(anchor=NW)  
    ent1.grid(pady=10)
    #ent1.grid(row=0,column=1,sticky=W+E) 
    #ent1.pack(side=LEFT,in_=TOP)
    #image_path='image2.jpg'
    def browseFiles():
        filename = filedialog.askopenfilename(
                                              title = "Select a File",
                                              filetypes = (("all files",
                                                            "*.*"),
                                                           ("PNG files","*.png*")
                                                           ))
        ent1.insert(0,filename)
    def ShowImage():
        #photo=PhotoImage(file=ent1.get())
        Dict = {"٢٥٩٤سجط": ['Andrew Raafat','24','No Fees','Kia Rio'],
            "٢٥٩٦٣": ['Passant El Baroudy','23','400','lancer'], "٢٥٩٤س٦٣": ['Youssef Raafat','23','700','MG6'], "٢٥١٦سم": ['Reem Mady','24','No Fees','Mercedes C180'], "٢٥٩فحق": ['Amr Sherif','36','1520','Suzuki Van'],"٦٧٤٣طدر": ['Adham Hesham','42','855','BMW 320i'],"٢٣٤٨نر": ['Fatma Abdel Aziz','63','8535','Jeep'],"٨٧٦دخع": ['Ibrahim Talaat','82','45','Chrysler'],"١٢١صخع": ['Fady Farid','42','450','Nissan Sunny']}  
        path=ent1.get() 
        #print("path=",path)
        carcolor,GovName,chars,numbers=mainfunc(path)
        wholePlate= numbers+chars
        Name = Dict[wholePlate][0]
        Age = Dict[wholePlate][1]
        Fees = Dict[wholePlate][2]
        carType = Dict[wholePlate][3]
        possy1=GovName
        possy2=carcolor
        photo=ImageTk.PhotoImage(Image.open(ent1.get()))
        #logo=PhotoImage(file=ent1.get())
        l1=Label(window)
        #l1.config(fg='silver')
        l1.config(image=photo)
        l1.image=photo
        #l1.grid(row=2,column=0,pady=10)
        l1.place(x=2,y=200)
        l2=Label(window,text="Input Image",bg='#1f666b',height=1,width=10,bd=6,font='Helvetica 11 bold')
        l2.place(x=20,y=160)
        
        label1=Label(window,text="Govname = "+possy1,font='Helvetica 12 bold',bg='#1f666b')
        label2=Label(window,text="Plate Type = "+possy2,font='Helvetica 12 bold',bg='#1f666b')
        label3=Label(window,text="Owner's Name = "+Name,font='Helvetica 12 bold',bg='#1f666b')
        label4=Label(window,text="Owner's Age = "+Age,font='Helvetica 12 bold',bg='#1f666b')
        label5=Label(window,text="Fees = "+Fees,font='Helvetica 12 bold',bg='#1f666b')
        label6=Label(window,text="Car Model = "+carType,font='Helvetica 12 bold',bg='#1f666b')
        label1.place(x=200,y=200)
        label2.place(x=200,y=220)
        label3.place(x=200,y=240)
        label4.place(x=200,y=260)
        label5.place(x=200,y=280)
        label6.place(x=200,y=300)
        
        #Method=combobox.get()
    
    
    #pathh=ShowImage()
    #possy="4455533132"+'\n'+"dnksms"
    #carcolor,GovName,chars=mainfunc(pathh)
    #possy=carcolor
    Font_tuple = ("Comic Sans MS", 9,"bold")
    
    b1= Button(window,text = "Browse Files",
                            command = browseFiles,bd=4,font=Font_tuple) 
    
    
    b1.grid(row=0,column=5,pady=30)
    
    
    b2=Button(window,text="Submit",bd=4,command=ShowImage,cursor='hand2',font=Font_tuple)
    b2.grid(row=3,column=0,pady=10)
    
    Restart_B=Button(window,text="Restart",bd=4,command=refresh,cursor='hand2',font=Font_tuple)
    # command=window.destroy
    Restart_B.grid(row=40,column=5,pady=10)
    
    b3=Button(window,text="Exit",bd=4,command=window.destroy,font=Font_tuple)
    b3.grid(row=30,column=5,pady=10)
    
    
    #window.resizable(True, True)
    
    window.mainloop()
    
    

if __name__ == '__main__':
    def refresh():
        window.destroy()
        vp_start_gui()

    vp_start_gui()
