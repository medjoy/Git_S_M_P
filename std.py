from tkinter import  *
from tkinter import  ttk
from tkinter import  messagebox
import pymysql


class Student:
        #___________________________________________انشاء نافدة البرنامج___________________________
    def __init__(self,med):
        self.med=med
        self.med.geometry('1350x690+1+1')
        self.med.title('برنامج ادارة المدارس')
        self.med.config(background='silver')
        self.med.resizable(False,False)
        title= Label(self.med,
                     text='[نظام تسجيل الطلاب]',
                     font=('Consolas,14'),
                     bg='#1AAECB',
                     fg='white')
        title.pack(fill=X)
        #___________________ variable _______________________________________________________________________________
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.moahel_var = StringVar()
        self.dell_var = StringVar()
        self.address_var = StringVar()
        self.gender_var = StringVar()
        self.se_by= StringVar()
        self.se_var = StringVar()
        # ______________________________________________________________ادوات التحكم بالبرنامج______________
        manage_frame = Frame(self.med, bg='white')
        manage_frame.place(x=1137, y=30, width=210, height=400)
        title1=Label(manage_frame,text='تسجيل الدخول',font=('Deco',14),fg='white',bg='#2980B9')
        title1.pack(fill=X)

        lbl_id=Label(manage_frame,text='الرقم التسلسلي',bg='white')
        lbl_id.pack()
        id_entry=Entry(manage_frame,textvariable=self.id_var,bd='2',justify='center')
        id_entry.pack()

        lbl_name = Label(manage_frame, text='اسم الطالب', bg='white')
        lbl_name.pack()
        name_entry = Entry(manage_frame,textvariable=self.name_var, bd='2',justify='center')
        name_entry.pack()

        lbl_email = Label(manage_frame, text='ايميل الطالب', bg='white')
        lbl_email.pack()
        email_entry = Entry(manage_frame,textvariable=self.email_var, bd='2',justify='center')
        email_entry.pack()

        lbl_phone = Label(manage_frame, text='هاتف الطالب', bg='white')
        lbl_phone.pack()
        phon_entry = Entry(manage_frame,textvariable=self.phone_var, bd='2',justify='center')
        phon_entry.pack()

        lbl_certi = Label(manage_frame, text='ماهلات الطالب', bg='white')
        lbl_certi.pack()
        certi_entry = Entry(manage_frame,textvariable=self.moahel_var, bd='2',justify='center')
        certi_entry.pack()

        lbl_gender = Label(manage_frame, text='اختر جنس الطالب', bg='white')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(manage_frame,textvariable=self.gender_var)
        combo_gender['value']=('ذكر','انثى')
        combo_gender.pack()

        lbl_adress = Label(manage_frame, text='عنوان الطالب', bg='white')
        lbl_adress.pack()
        adress_entry = Entry(manage_frame,textvariable=self.address_var, bd='2',justify='center')
        adress_entry.pack()

        lbl_delet=Label(manage_frame, text='حدف الطالب ',fg='red',bg='white')
        lbl_delet.pack()
        delet_entry=Entry(manage_frame,textvariable=self.dell_var,bd='2',justify='center')
        delet_entry.pack()

        #__________________________BUTTONS الازرار_____________________________________________________________________
        btn_fram=Frame(self.med,bg='white')
        btn_fram.place(x=1137,y=445,width=210,height=240)

        title2=Label(btn_fram,text='لوحة التحكم',font=('Deco',14),fg='white',bg='#2980B9')
        title2.pack(fill=X)

        add_btn=Button(btn_fram,text='اضافة طالب',bg='#85929E',command=self.add_student)
        add_btn.place(x=33,y=35,width=150,height=30)

        del_btn = Button(btn_fram, text='حدف طالب', bg='#85929E',command=self.delete)
        del_btn.place(x=33, y=69, width=150, height=30)

        update_btn = Button(btn_fram, text='تعديل بينات طالب', bg='#85929E',command=self.update)
        update_btn.place(x=33, y=103, width=150, height=30)

        clrear_btn = Button(btn_fram, text='افراغ الحقول', bg='#85929E',command=self.clear)
        clrear_btn.place(x=33, y=137, width=150, height=30)

        about_btn = Button(btn_fram, text='من نحن', bg='#85929E',command=self.about)
        about_btn.place(x=33, y=171, width=150, height=30)

        exit_btn = Button(btn_fram, text='اغلاق البرنامج', bg='#85929E',command=med.quit)
        exit_btn.place(x=33, y=205, width=150, height=30)
        #_____________________search manage البحت___________________________________________________
        search_frame=Frame(self.med,bg='white')
        search_frame.place(x=1,y=30,width=1132,height=50)

        lbl_search=Label(search_frame,text='البحت عن طالب',font=('Deco',14),fg='white',bg='#2980B9')
        lbl_search.place(x=1026,y=0)

        combo_search=ttk.Combobox(search_frame,textvariable=self.se_by,justify='right')
        combo_search['value']=('id','name','email','phone')
        combo_search.place(x=680,y=15)

        search_entry=Entry(search_frame,textvariable=self.se_var,justify='right',bd='2')
        search_entry.place(x=540,y=15)

        se_btn=Button(search_frame,text='البحت',bg='#85929E',command=self.search)
        se_btn.place(x=430,y=12,width=100,height=25)
        #___________________dietals عرض النتائج والبينات____________________________________________________________________________
        dietals_frame=Frame(self.med,bg='#8192AF')
        dietals_frame.place(x=1,y=83,width=1132,height=605)
              #_________scroll___________________
        scroll_x=Scrollbar(dietals_frame,orient=HORIZONTAL)
        scroll_y =Scrollbar(dietals_frame,orient=VERTICAL)
            #___________treeveiw__________________________
        self.student_table=ttk.Treeview(dietals_frame,
        columns=('address','gender','certi','phone','email','name','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_table.place(x=15,y=0,width=1130,height=587)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'
        self.student_table.heading('address', text='عنوان الطالب')
        self.student_table.heading('gender', text='جنس الطالب')
        self.student_table.heading('certi', text='مؤهلات الطالب')
        self.student_table.heading('phone', text='رقم الهاتف')
        self.student_table.heading('email', text='البريد الالكتروني')
        self.student_table.heading('name', text='اسم الطالب')
        self.student_table.heading('id', text='الرقم التسلسلي')

        self.student_table.column('address',width=120)
        self.student_table.column('gender',width=30)
        self.student_table.column('certi',width=65)
        self.student_table.column('phone',width=65)
        self.student_table.column('email',width=70)
        self.student_table.column('name',width=100)
        self.student_table.column('id',width=30)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)


    #______________________________________________تشغيل الاضهار البينات___________________
        self.fetch_all()
    #____________________add  +con______________________________________________________________________
    def add_student(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stud')
        cur=con.cursor()
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',(
                                                     self.address_var.get(),
                                                     self.gender_var.get(),
                                                     self.moahel_var.get(),
                                                     self.phone_var.get(),
                                                     self.email_var.get(),
                                                     self.name_var.get(),
                                                     self.id_var.get()  ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    #________________________________________________________________اضهار البينات_______________________
    def fetch_all(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute('select* from student')
        rows=cur.fetchall()
        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()
    #________________delete_________________________________________________________________________________________
    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute('delete from student where id=%s',self.dell_var.get())
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    #________________________________________________________________________________دالة افراغ الحقول___________________________
    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.moahel_var.set('')
        self.gender_var.set('')
        self.dell_var.set('')
        self.address_var.set('')
    #________________________________________________________________________________________تعديل البينات___________________
    def get_cursor(self,ev):
        cursor_row= self.student_table.focus() #عندما انقر
        contents = self.student_table.item(cursor_row)#خبي ليا داك شي لبركت علو فهاد لمتغير
        row=contents['values']
        self.id_var.set(row[6])
        self.name_var.set(row[5])
        self.email_var.set(row[4])
        self.phone_var.set(row[3])
        self.moahel_var.set(row[2])
        self.gender_var.set(row[1])
        self.address_var.set(row[0])
    #_________________Update______________________________________________________________________
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')
        cur = con.cursor()
        cur.execute('update student set address=%s,gender=%s,moahel=%s,phone=%s,email=%s,name=%s where id=%s', (
            self.address_var.get(),
            self.gender_var.get(),
            self.moahel_var.get(),
            self.phone_var.get(),
            self.email_var.get(),
            self.name_var.get(),
            self.id_var.get()))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    #__________________________________________________________________البحت ____________________
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute("select * from student where " +
        str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()
    #_________________messagebox____________________________________________________________________________
    def about(self):
        messagebox.showinfo("devloper mohammed bouaroua","welcom to my first projet")

med =Tk()
ob = Student(med)
med.mainloop()