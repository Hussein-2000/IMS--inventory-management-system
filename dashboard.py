from tkinter import*
from PIL import Image, ImageTk #What can pillow library do? ANSWER: The Pillow library contains all the basic image processing functionality. You can do image resizing, rotation and transformation 
from Employees import Employee 

# CLOURS===========
Black = "#393646"
LightBlack = "#4F4557"
MoreLight = "#6D5D6E"
Light = "#F4EEE0"


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("Inventory mmanagement system | Developped by Hussein")
        

        # ====== TITTLE==================
        self.icon_title = PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Inventory management system", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"),bg=MoreLight, fg='white' , anchor='w', padx=20).place(x=0, y=0, relwidth=1, heigh=70)

        # Button LOgout
        btn_logout = Button(self.root, text="Log-Out", font=("times new roman", 15,"bold"), bg=Black, fg=Light, cursor='hand2').place(x=1180, y=10, height=50, width=150)

        # Clock label 
        self.lb_clock = Label(self.root, text="Welcome tp Inventory   management system\t\t  Date: DD-MM-YYYY \t\t  Time: HH:mm:SS", font=("times new roman", 15),bg=LightBlack, fg='white')
        self.lb_clock.place(x=0, y=70, relwidth=1, heigh=30)

        # Let menues ================== Inta sa fcn u fahn ma fahansanidee war\yaaaaaaaaaaaaaa
        self.menu_logo = Image.open("images/menu_logo.png").resize((200,200), Image.Resampling.LANCZOS)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        LeftMenue = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        LeftMenue.place(x=0 , y= 102 , width=200, height=565)


        lbl_menuLogot = Label(LeftMenue, image=self.menu_logo)
        lbl_menuLogot.pack(side=TOP, fill=X)

        # MENUES BUTTONS ==========
        LabelMenu = Label(LeftMenue, text="Menue", bg=MoreLight, fg="white", font=("times new roman", 20))
        LabelMenu.pack(side=TOP, fill=X)

        self.MenuBtnLogo = Image.open("images/menuBtn.png").resize((35,35), Image.Resampling.LANCZOS)
        self.MenuBtnLogo = ImageTk.PhotoImage(self.MenuBtnLogo)

        #Employee button-
        btn_Employee = Button(LeftMenue, text="Employee", command=self.employee, image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Employee.pack(fill=X)
        
        #suplier button-
        btn_Suplier = Button(LeftMenue, text="Supplier", image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Suplier.pack(fill=X)
        
        #Category button-
        btn_Category = Button(LeftMenue, text="Category", image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Category.pack(fill=X)
        
        #products button-
        btn_Products = Button(LeftMenue, text="Products", image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Products.pack(fill=X)
        
        #Sales button-
        btn_Sales = Button(LeftMenue, text="Sales", image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Sales.pack(fill=X)
        
        #Exit button-
        btn_Exit = Button(LeftMenue, text="Exit", image=self.MenuBtnLogo, compound=LEFT , padx=7, anchor='w', font=("times new roman", 20,"bold"), bg='white', bd=3,  cursor='hand2')
        btn_Exit.pack(fill=X)
        

        # ===========CONTENT OF THE BODY ======================

        self.lbl_employee = Label(self.root, text="Total Employee\n [0]", bd=5, relief=RIDGE, bg='#FF6000', fg='white', font=('goudy old ', 20,"bold"))
        self.lbl_employee.place(x=300 , y=120, width=300, height=150)

        self.lbl_suplier = Label(self.root, text="Total Suplier\n [0]", bd=5, relief=RIDGE, bg='#454545', fg='white', font=('goudy old ', 20,"bold"))
        self.lbl_suplier.place(x=650 , y=120, width=300, height=150)

        self.lbl_category = Label(self.root, text="Total Category\n [0]", bd=5, relief=RIDGE, bg='#009688', fg='white', font=('goudy old ', 20,"bold"))
        self.lbl_category.place(x=1000 , y=120, width=300, height=150)

        self.lbl_product = Label(self.root, text="Total Product\n [0]", bd=5, relief=RIDGE, bg='#607d8b', fg='white', font=('goudy old ', 20,"bold"))
        self.lbl_product.place(x=300 , y=305, width=300, height=150)

        self.lbl_sales = Label(self.root, text="Total Sales\n [0]", bd=5, relief=RIDGE, bg='#ffc107', fg='white', font=('goudy old ', 20,"bold"))
        self.lbl_sales.place(x=650 , y=305, width=300, height=150)






         # Footer label 
        lb_footer = Label(self.root, text="IMS_Inventory management system | developped By Hussein \n For any technical issue contact: +252612221034", font=("times new roman", 13),bg=LightBlack, fg='white').pack(side=BOTTOM, fill=X)
    # =====================================================================================================================================================================================================================================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Employee(self.new_win)
        

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()