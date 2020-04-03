
from tkinter import *

window = Tk()

window.geometry('1500x700')
window.configure(bg='misty rose')
window.title('COVID_TEST')
def ent():
    m=x.get()
    B=Button(text='ENTER',width=9,height=2,bg='lavender blush',fg='black',activebackground='black',command=lambda:[ent1(),pre()],activeforeground='white',bd=10,relief=RAISED,cursor='arrow').grid(row=12,column=4)
def ent1():
    n=y.get()
    l3=Label(text="YOUR CHANCE OF TESTING POSITIVE=",font=6,bg='misty rose').grid(row=14,column=2,sticky=W)
x=StringVar()
y=StringVar()
list= ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
age=IntVar()
age.set(list[0])
b=OptionMenu(window,age,*list).grid(row=2,column=8,sticky=W)
l=Label(text="Please enter your age",font=8,fg='#646060',bg='misty rose').grid(row=2,column=1,sticky=W)
list1= ["MALE","FEMALE"]
gender=StringVar()
b1=OptionMenu(window,gender,*list1).grid(row=4,column=8)
l1=Label(text="Select your Gender",font=8,fg='#646060',bg='misty rose').grid(row=4,column=1,sticky=W)
l2=Label(text="Please select what symptoms are you facing",font=10,fg='#646060',bg='misty rose').grid(row=7,column=2,sticky=W)
b2=Button(text="FEVER",width=9,height=1,bg='white',fg='black',command= ent,bd=4,relief=RIDGE,cursor='plus').grid(row=8,column=3)
b3=Button(text="COUGH",width=10,height=1,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=8,column=4)
b4=Button(text="SHORTNESS OF BREATH",width=18,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=8,column=5)
b5=Button(text="SORE THROAT",width=15,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=3)
b6=Button(text="CHILLS",width=15,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=4)
b7=Button(text="MUSCLE PAIN",width=11,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=5)
b8=Button(text="NAUSEA",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=10,column=3)
b8=Button(text="DIARRHOEA",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=10,column=4)
b8=Button(text="FATIGUE",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=10,column=5)
b8=Button(text="VOMITING",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=11,column=3)
b8=Button(text="HEADACHE",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=11,column=4)
b8=Button(text="MALAISE",width=9,height=2,bg='lavender blush',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=11,column=5)

z=StringVar()
def pre():
    o=z.get()
    l4=Label(text="Based on your scan, here are some recommendations:",font=5,bg='azure',fg='navy').grid(row=16,column=1,sticky=W)
    l5=Label(text="1.Seek immediate medical attention and get yourself tested.",font=4,bg='azure').grid(row=17,column=1,sticky=W)
    l6=Label(text="2.Please visit physician as there may be requirement for further care.",font=4,bg='azure').grid(row=18,column=1,sticky=W)
    l7=Label(text="3.COVID-19 testing may be needed at your physician's advise.",font=4,bg='azure').grid(row=19,column=1,sticky=W)
    l8=Label(text="5.Monitor your symptoms and isolate yourself",font=4,bg='azure').grid(row=20,column=1,sticky=W)
    l9=Label(text="4.Preventions and Precautions->",font=4,bg='azure').grid(row=21,column=1,sticky=W)




def run_animation():
    while True:
        try:
            global photo
            global frame
            global label
            photo = PhotoImage(
                file = photo_path,
                format = "gif - {}".format(frame)
                )

            label.configure(image = nextframe)

            frame = frame + 1

        except Exception:
            frame = 1
            break

photo_path = "E://Covid project//t.gif"

photo = PhotoImage(
    file = photo_path,
    )
label = Label(
    image = photo
    )
animate = Button(
    window,
    text = "animate",
    command = run_animation
    )

label.grid(row=21,column=2,sticky=S)
animate.grid(row=21,column=2)

window.mainloop()