# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:51:45 2020

@author: kirtika jain
"""

from tkinter import *
window = Tk()
window.geometry('1500x700')
window.title('COVID_TEST')
def ent():
    m=x.get()
    B=Button(text='ENTER',width=9,height=2,bg='white',fg='black',activebackground='black',command=ent1,activeforeground='white',bd=10,relief=RAISED,cursor='arrow').grid(row=12,column=4)
def ent1():
    n=y.get()
    l3=Label(text="YOUR CHANCE OF TESTING POSITIVE=",font=6).grid(row=14,column=2)
x=StringVar()
y=StringVar()
list= ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
age=IntVar()
age.set(list[0])
b=OptionMenu(window,age,*list).grid(row=2,column=8)
l=Label(text="Please enter your age",font=8,fg='#646060').grid(row=2,column=1)
list1= ["MALE","FEMALE"]
gender=StringVar()
b1=OptionMenu(window,gender,*list1).grid(row=4,column=8)
l1=Label(text="Select your Gender",font=8,fg='#646060').grid(row=4,column=1)
l2=Label(text="Please select what symptoms are you facing",font=10,fg='#646060').grid(row=7,column=2)
b2=Button(text="FEVER",width=9,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=8,column=3)
b3=Button(text="TIREDNESS",width=10,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=8,column=4)
b4=Button(text="DRY COUGH",width=10,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=8,column=5)
b5=Button(text="SHORTNESS OF BREATH",width=18,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=3)
b6=Button(text="ACHES AND PAIN",width=15,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=4)
b7=Button(text="SORE THROAT",width=11,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=9,column=5)
b8=Button(text="OTHERS",width=9,height=2,bg='white',fg='black',command= ent,activebackground='black',activeforeground='white',bd=10,relief=SUNKEN,cursor='plus').grid(row=10,column=4)




window.mainloop()