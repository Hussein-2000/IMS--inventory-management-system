from tkinter import*
from PIL import Image, ImageTk #What can pillow library do? ANSWER: The Pillow library contains all the basic image processing functionality. You can do image resizing, rotation and transformation 
from tkinter import ttk
from dashboard import *


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Inventory mmanagement system | Developped by Hussein")
        self.root.focus_force()
        self.root.config(bg="white")

        # ============== 
        # ====AlL VARIABLES=======
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact= StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_UserType  = StringVar()
        self.var_salary  = StringVar()


        # ?============= Serach frame work-----------
        SearchFrame = LabelFrame(self.root, text="Search Employee ", bg="White")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # =========== Options============= and search button
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchBy,values=("Select", "Email", "Name", "contact"), state="readonly", justify=CENTER, font=(" Roboto Slab",12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchTxt ,font=("Signika", 15), bg=Light).place(x= 200 , y = 10)
        btn_search =  Button(SearchFrame, text="Search" ,font=("Signika", 15), bg=Black, fg='white', cursor="hand2").place(x= 440, y = 9, width=130, height=30)
        

        # ============== Tittle ----------------
        title = Label(self.root, text="Employee details", font=("Oregon", 18), bg=LightBlack, fg='white').place(x = 50, y = 100, width=1000 )



        # =========== CONTENT ===================
        # ======Row 1========================
        lbl_empid = Label(self.root, text="Emp ID", font=("Oregon", 15), bg="white").place(x = 50, y = 150)
        lbl_gender = Label(self.root, text="Gender", font=("Oregon", 15), bg="white").place(x = 350, y = 150)
        lbl_contact = Label(self.root, text="Contact", font=("Oregon", 15), bg="white").place(x = 750, y = 150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id,font=("Oregon", 15), bg="light Blue").place(x = 150, y = 150    , width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select", "Male", "Female"), state="readonly", justify=CENTER, font=(" Roboto Slab",12))
        cmb_gender.place(x = 500, y = 150   , width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Oregon", 15), bg="light Blue").place(x = 850, y = 150, width=180)

        # ======Row 2========================
        lbl_name = Label(self.root, text="Name", font=("Oregon", 15), bg="white").place(x = 50, y = 190)
        lbl_dob = Label(self.root, text="D.O.B", font=("Oregon", 15), bg="white").place(x = 350, y = 190)
        lbl_doj = Label(self.root, text="D.O.J", font=("Oregon", 15), bg="white").place(x = 750, y = 190)

        txt_name = Entry(self.root, textvariable=self.var_name,font=("Oregon", 15), bg="light Blue").place(x = 150, y = 190    , width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob,font=("Oregon", 15), bg="light Blue").place(x = 500, y = 190   , width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Oregon", 15), bg="light Blue").place(x = 850, y = 190, width=180)

        # ======Row 3========================
        lbl_email = Label(self.root, text="Email", font=("Oregon", 15), bg="white").place(x = 50, y = 230)
        lbl_pass = Label(self.root, text="Pasword", font=("Oregon", 15), bg="white").place(x = 350, y = 230)
        lbl_userType = Label(self.root, text="User Type", font=("Oregon", 15), bg="white").place(x = 750, y = 230)

        txt_email = Entry(self.root, textvariable=self.var_email,font=("Oregon", 15), bg="light Blue").place(x = 150, y = 230    , width=180)
        txt_Password = Entry(self.root, textvariable=self.var_pass,font=("Oregon", 15), bg="light Blue").place(x = 500, y = 230   , width=180)
        cmb_UserType = ttk.Combobox(self.root, textvariable=self.var_UserType,values=("Select", "Admin", "Employee"), state="readonly", justify=CENTER, font=(" Roboto Slab",12))
        cmb_UserType.place(x = 850, y = 230, width=180)
        cmb_UserType.current(0)


        # ======Row 4========================
        lbl_adress = Label(self.root, text="Adress", font=("Oregon", 15), bg="white").place(x = 50, y = 270)
        lbl_Salary = Label(self.root, text="SAlary", font=("Oregon", 15), bg="white").place(x = 500, y = 270)

        self.txt_adress = Text(self.root,font=("Oregon", 15), bg="light Blue").place(x = 150, y = 270    , width=300 , height=60)
        txt_Salary = Entry(self.root, textvariable=self.var_salary,font=("Oregon", 15), bg="light Blue").place(x = 600, y = 270   , width=180)
        















if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
