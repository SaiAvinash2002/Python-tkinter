from  tkinter import *  
from tkinter import messagebox
a=Tk()
a.minsize(1500,900)
a.title("Registration Form")
a.configure(bg='lightslateblue')
label_0=Label(a,text="FIRST NAME",width=20,font=20,bg='lightslateblue',fg='white')
label_0.place(x=90,y=23)

fn_entry=Entry()
fn_entry.place(x=350,y=23)

label_1=Label(a,text="LAST NAME",width=20,font=20,bg='lightslateblue',fg='white')
label_1.place(x=85,y=65)

ln_entry=Entry()
ln_entry.place(x=350,y=65)

label_2=Label(a,text="DATE OF BIRTH",width=20,font=20,bg='lightslateblue',fg='white')
label_2.place(x=100,y=105)

date=range(1,32)
d_click=StringVar()
d_click.set("Day")

drop=OptionMenu(a,d_click,*date)
drop.place(x=350,y=105)

month=["January","February","March","April","May","June","July","August","September","October","November","December"]
m_click=StringVar()
m_click.set("Month")

drop1=OptionMenu(a,m_click,*month)
drop1.place(x=450,y=105)

year=range(1999,2022)
y_click=StringVar()
y_click.set("Year")

drop2=OptionMenu(a,y_click,*year)
drop2.place(x=600,y=105)

label_3=Label(a,text="EMAIL ID",width=20,font=20,bg='lightslateblue',fg='white')
label_3.place(x=70,y=145)

eid_entry=Entry()
eid_entry.place(x=350,y=145)

def onclick():
    pass
radio=IntVar()
g1=Radiobutton(a,text="Male",width=10,font=10,variable=radio,command=onclick,value=1,bg='lightslateblue',fg='white')
g1.place(x=310,y=230)

radio2=IntVar()
g2=Radiobutton(a,text="Female",width=10,font=10,variable=radio,value=2,command=onclick,bg='lightslateblue',fg='white')
g2.place(x=410,y=230)

label_4=Label(a,text="MOBILE NUMBER",width=20,font=20,bg='lightslateblue',fg='white')
label_4.place(x=107,y=190)

m_entry=Entry()
m_entry.place(x=350,y=190)

label_5=Label(a,text="GENDER",width=20,font=20,bg='lightslateblue',fg='white')
label_5.place(x=63,y=230)

label_6=Label(a,text="ADDRESS",width=20,font=20,bg='lightslateblue',fg='white')
label_6.place(x=69,y=270)

ad_entry=Entry()
ad_entry.place(x=350,y=270)

label_7=Label(a,text="CITY",width=20,font=20,bg='lightslateblue',fg='white')
label_7.place(x=52,y=310)

c_entry=Entry()
c_entry.place(x=350,y=310)

label_8=Label(a,text="PINCODE",width=20,font=20,bg='lightslateblue',fg='white')
label_8.place(x=67,y=349)

p_entry=Entry()
p_entry.place(x=345,y=349)

label_9=Label(a,text="STATE",width=20,font=20,bg='lightslateblue',fg='white')
label_9.place(x=53,y=390)

st_entry=Entry()
st_entry.place(x=350,y=390)

label_10=Label(a,text="COUNTRY",width=20,font=20,bg='lightslateblue',fg='white')
label_10.place(x=70,y=430)

co_entry=Entry()
co_entry.place(x=350,y=430)

label_11=Label(a,text="HOBBIES",width=20,font=20,bg='lightslateblue',fg='white')
label_11.place(x=62,y=470)

h1_ck=Checkbutton(a,text="Drawing ",width=10,font=5,bg='lightslateblue',fg='white')
h1_ck.place(x=340,y=470)

h2_ck=Checkbutton(a,text="Singing ",width=10,font=5,bg='lightslateblue',fg='white')
h2_ck.place(x=460,y=470)

h3_ck=Checkbutton(a,text="Dancing ",width=10,font=5,bg='lightslateblue',fg='white')
h3_ck.place(x=570,y=470)

h4_ck=Checkbutton(a,text=" Sketching",width=10,font=5,bg='lightslateblue',fg='white')
h4_ck.place(x=350,y=500)

h5_ck=Checkbutton(a,text="Others",width=10,font=5,bg='lightslateblue',fg='white')
h5_ck.place(x=480,y=500)

h_entry=Entry()
h_entry.place(x=600,y=505)

label_12=Label(a,text="QUALIFICATION",width=20,font=20,bg='lightslateblue',fg='white')
label_12.place(x=90,y=530)

label_13=Label(a,text="Sl.No.\n1\n\n2\n\n3\n\n4",width=20,font=20,bg='lightslateblue',fg='white')
label_13.place(x=290,y=530)

label_14=Label(a,text="Examination\nClassX\n\nClassXll\n\nGraduation\n\nMasters",width=20,font=20,bg='lightslateblue',fg='white')
label_14.place(x=430,y=530)

label_15=Label(a,text="Board               Percentage             Year of Passing",width=50,font=20,bg='lightslateblue',fg='white')
label_15.place(x=630,y=530)

bo_entry=Entry()
bo_entry.place(x=625,y=560)

bo1_entry=Entry()
bo1_entry.place(x=625,y=600)

bo2_entry=Entry()
bo2_entry.place(x=625,y=640)

bo3_entry=Entry()
bo3_entry.place(x=625,y=690)

p_entry=Entry()
p_entry.place(x=800,y=560)

p1_entry=Entry()
p1_entry.place(x=800,y=600)

p2_entry=Entry()
p2_entry.place(x=800,y=640)

p3_entry=Entry()
p3_entry.place(x=800,y=690)

y_entry=Entry()
y_entry.place(x=975,y=560)

y1_entry=Entry()
y1_entry.place(x=975,y=600)

y2_entry=Entry()
y2_entry.place(x=975,y=640)

y3_entry=Entry()
y3_entry.place(x=975,y=690)

label_16=Label(a,text="COURSES\nAPPLIED FOR",width=20,font=20,bg='lightslateblue',fg='white')
label_16.place(x=90,y=725)

radio_1=IntVar()
c1=Radiobutton(a,text="BCA",width=5,font=10,variable=radio_1,value=1,bg='lightslateblue',fg='white')
c1.place(x=310,y=725)

c2=Radiobutton(a,text="B.Com",width=5,font=10,variable=radio_1,value=2,bg='lightslateblue',fg='white')
c2.place(x=410,y=725)

c3=Radiobutton(a,text="B.Sc",width=5,font=10,variable=radio_1,value=3,bg='lightslateblue',fg='white')
c3.place(x=510,y=725)

c4=Radiobutton(a,text="B.A",width=5,font=10,variable=radio_1,value=4,bg='lightslateblue',fg='white')
c4.place(x=610,y=725)

def myclick():
    msg=messagebox.showinfo("Confirmation","Your response has been submitted")


s_button=Button(a,text="Submit",command=myclick)
s_button.place(x=570,y=760)

r_button=Button(a,text="Reset")
r_button.place(x=650,y=760)
