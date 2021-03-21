from  tkinter import *  
from tkinter import messagebox
import sqlite3

a=Tk()
a.minsize(1500,900)
a.title("Registration Form")
a.configure(bg='lightslateblue')

fn=StringVar()
ln=StringVar()
mob=StringVar()
eid=StringVar()
add=StringVar()
city=StringVar()
coun=StringVar()
state=StringVar()
pin=StringVar()

label_0=Label(a,text="FIRST NAME",width=20,font=20,bg='lightslateblue',fg='white')
label_0.place(x=90,y=23)

fn_entry=Entry(a,textvar=fn)
fn_entry.place(x=350,y=23)

label_1=Label(a,text="LAST NAME",width=20,font=20,bg='lightslateblue',fg='white')
label_1.place(x=85,y=65)

ln_entry=Entry(a,textvar=ln)
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

eid_entry=Entry(a,textvar=eid)
eid_entry.place(x=350,y=145)


radio=StringVar()
Radiobutton(a,text="Male",width=10,font=10,variable=radio,textvar='male',bg='lightslateblue',fg='white').place(x=310,y=230)

Radiobutton(a,text="Female",width=10,font=10,variable=radio,textvar='female',bg='lightslateblue',fg='white').place(x=410,y=230)

label_4=Label(a,text="MOBILE NUMBER",width=20,font=20,bg='lightslateblue',fg='white')
label_4.place(x=107,y=190)

m_entry=Entry(a,textvar=mob)
m_entry.place(x=350,y=190)

label_5=Label(a,text="GENDER",width=20,font=20,bg='lightslateblue',fg='white')
label_5.place(x=63,y=230)

label_6=Label(a,text="ADDRESS",width=20,font=20,bg='lightslateblue',fg='white')
label_6.place(x=69,y=270)

ad_entry=Entry(a,textvar=add)
ad_entry.place(x=350,y=270)

label_7=Label(a,text="CITY",width=20,font=20,bg='lightslateblue',fg='white')
label_7.place(x=52,y=310)

city_entry=Entry(a,textvar=city)
city_entry.place(x=350,y=310)



label_8=Label(a,text="PINCODE",width=20,font=20,bg='lightslateblue',fg='white')
label_8.place(x=67,y=349)


pin_entry=Entry(a,textvar=pin)
pin_entry.place(x=345,y=349)

label_9=Label(a,text="STATE",width=20,font=20,bg='lightslateblue',fg='white')
label_9.place(x=53,y=390)

st_entry=Entry(a,textvar=state)
st_entry.place(x=350,y=390)

label_10=Label(a,text="COUNTRY",width=20,font=20,bg='lightslateblue',fg='white')
label_10.place(x=70,y=430)

country_entry=Entry(a,textvar=coun)
country_entry.place(x=350,y=430)

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

hobbies=StringVar()
h_entry=Entry(a,text=hobbies)
h_entry.place(x=600,y=505)

label_12=Label(a,text="QUALIFICATION",width=20,font=20,bg='lightslateblue',fg='white')
label_12.place(x=90,y=530)

label_13=Label(a,text="Sl.No.\n1\n\n2\n\n3\n\n4",width=20,font=20,bg='lightslateblue',fg='white')
label_13.place(x=290,y=530)

label_14=Label(a,text="Examination\nClassX\n\nClassXll\n\nGraduation\n\nMasters",width=20,font=20,bg='lightslateblue',fg='white')
label_14.place(x=430,y=530)

label_15=Label(a,text="    Board                            Percentage                         Year of Passing",width=50,font=20,bg='lightslateblue',fg='white')
label_15.place(x=630,y=530)

dxb=StringVar()
bo_entry=Entry(a,textvar=dxb)
bo_entry.place(x=625,y=560)

dxllb=StringVar()
bo1_entry=Entry(a,textvar=dxllb)
bo1_entry.place(x=625,y=600)

dgb=StringVar()
bo2_entry=Entry(a,textvar=dgb)
bo2_entry.place(x=625,y=640)

dmg=StringVar()
bo3_entry=Entry(a,textvar=dmg)
bo3_entry.place(x=625,y=690)

dxp=StringVar()
p_entry=Entry(a,textvar=dxp)
p_entry.place(x=800,y=560)

dxllp=StringVar()
p1_entry=Entry(a,textvar=dxllp)
p1_entry.place(x=800,y=600)

dgp=StringVar()
p2_entry=Entry(a,textvar=dgp)
p2_entry.place(x=800,y=640)

dmp=StringVar()
p3_entry=Entry(a,textvar=dmp)
p3_entry.place(x=800,y=690)

dxy=StringVar()
y_entry=Entry(a,textvar=dxy)
y_entry.place(x=975,y=560)

dxlly=StringVar()
y1_entry=Entry(a,textvar=dxlly)
y1_entry.place(x=975,y=600)

dgy=StringVar()
y2_entry=Entry(a,textvar=dgy)
y2_entry.place(x=975,y=640)

dmy=StringVar()
y3_entry=Entry(a,textvar=dmy)
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



def submit():
    connection=sqlite3.connect("avi.db")
    cur=connection.cursor()
    cur.execute("insert into users values('"+str(fn.get())+"','"+str(ln.get())+"','"+str(eid.get())+"','"+str(mob.get())+"','"+str(add.get())+"','"+str(city.get())+"','"+str(pin.get())+"','"+str(state.get())+"','"+str(dxb.get())+"','"+str(dxp.get())+"','"+str(dxy.get())+"','"+str(dxllb.get())+"','"+str(dxllp.get())+"','"+str(dgb.get())+"','"+str(dgy.get())+"','"+str(dmg.get())+"','"+str(dmy.get())+"')")
    connection.commit()
    connection.close()
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    eid_entry.delete(0,END)
    m_entry.delete(0,END)
    city_entry.delete(0,END)
    country_entry.delete(0,END)
    pin_entry.delete(0,END)
    st_entry.delete(0,END)
    ad_entry.delete(0,END)
    bo_entry.delete(0,END)
    bo1_entry.delete(0,END)
    bo2_entry.delete(0,END)
    bo3_entry.delete(0,END)
    p_entry.delete(0,END)
    p1_entry.delete(0,END)
    p2_entry.delete(0,END)
    p3_entry.delete(0,END)
    y_entry.delete(0,END)
    y1_entry.delete(0,END)
    y2_entry.delete(0,END)
    y3_entry.delete(0,END)
    
    msg=messagebox.showinfo("Confirmation","Your response has been submitted")

def reset():
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    eid_entry.delete(0,END)
    m_entry.delete(0,END)
    city_entry.delete(0,END)
    country_entry.delete(0,END)
    pin_entry.delete(0,END)
    st_entry.delete(0,END)
    ad_entry.delete(0,END)
    bo_entry.delete(0,END)
    bo1_entry.delete(0,END)
    bo2_entry.delete(0,END)
    bo3_entry.delete(0,END)
    p_entry.delete(0,END)
    p1_entry.delete(0,END)
    p2_entry.delete(0,END)
    p3_entry.delete(0,END)
    y_entry.delete(0,END)
    y1_entry.delete(0,END)
    y2_entry.delete(0,END)
    y3_entry.delete(0,END)
    
s_button=Button(a,text="Submit",command=submit)
s_button.place(x=570,y=760)

r_button=Button(a,text="Reset",command=reset)
r_button.place(x=650,y=760)

avi = sqlite3.connect("avi.db")
cursor=avi.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(FIRSTNAME VARCHAR(225),LASTNAME VARCHAR(225),EMAILID VARCHAR(225),MOBILENUMBER VARCHAR(10),ADDRESS VARCHAR(225),CITY VARCHAR(225),PINCODE VARCHAR(6),STATE VARCHAR(225),COUNTRY VARCHAR(225),HOBBIES VARCHAR(225),XB VARCHAR(225),XP VARCHAR(225),XY VARCHAR(225),XLLB VARCHAR(225),XLLP VARCHAR(225),XLLY VARCHAR(225),GB VARCHAR(225),GP VARCHAR(225),GY VARCHAR(225),MG VARCHAR(225),MP VARCHAR(225),MY VARCHAR(225))")



avi.close()
