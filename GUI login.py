from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

def SignIn():
    username=user.get()
    password=pasw.get()
    file="D:\\Kuliah UNEJ\\Semester 2\\Algo 2\\database.txt"
    opn = open(file)
    List =  opn.readlines()
    Data = []
    sukses = False
    for i in List:
        Data.append(i.strip())
    for i in range(0,len(List),2):
        if username == Data[i]:
            if password == Data[i+1]:
                sukses = True
                messagebox.showinfo("Sign in", "Sign in berhasi")
                break
            else :
                  messagebox.showerror("Gagal", "Password anda tidak valid")



def signup_command():
    window=Toplevel(root)
    window.title("Login")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False,False)

    def SignUp():
        username=user.get()
        password=pasw.get()
        confirm_password=conf_pasw.get()
        file="D:\\Kuliah UNEJ\\Semester 2\\Algo 2\\database.txt"

        if password==confirm_password:
        
            opn = open(file,"a")
            opn.write(f"{username}\n{password}\n")
            opn.close()

            messagebox.showinfo("Sign up", "Sign up berhasil")
            window.destroy()

        else:
            messagebox.showerror("Gagal", "Password anda tidak valid")

    def sign():
        window.destroy()


    img = PhotoImage(file="D:\\Kuliah UNEJ\\Semester 2\\Algo 2\\login2.png")
    Label(window,image=img,bg='white').place(x=50,y=50)

    frame=Frame(window,width=350,height=390,bg="#fff")
    frame.place(x=480,y=50)

    heading=Label(frame,text="Sign up",fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100,y=5)

#Input Username
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name=user.get()
        if name == "":
            user.insert(0, "Username")

    user = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30,y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295, height=2,bg="black").place(x=25,y=107)

#Input Password
    def on_enter(e):
        pasw.delete(0, "end")

    def on_leave(e):
        password=pasw.get()
        if password == "":
            pasw.insert(0, "Password")

    pasw = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    pasw.place(x=30,y=150)
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", on_enter)
    pasw.bind("<FocusOut>", on_leave)

    Frame(frame,width=295, height=2,bg="black").place(x=25,y=177)

#Input Konfirmasi pasword
    def on_enter(e):
        conf_pasw.delete(0, "end")

    def on_leave(e):
        password=conf_pasw.get()
        if password == "":
            conf_pasw.insert(0, "Confirm Password")

    conf_pasw = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    conf_pasw.place(x=30,y=220)
    conf_pasw.insert(0, "Confirm Password")
    conf_pasw.bind("<FocusIn>", on_enter)
    conf_pasw.bind("<FocusOut>", on_leave)

    Frame(frame,width=295, height=2,bg="black").place(x=25,y=247)

    #Button
    Button(frame,width=39,pady=7,text="Sign up", bg="#57a1f8",fg="white",border=0,command=SignUp).place(x=35,y=280)
    label=Label(frame,text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=90,y=340)

    sign_in = Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8")
    sign_in.place(x=200,y=340)
    window.mainloop()

###################################################################

img = PhotoImage(file="D:\\Kuliah UNEJ\\Semester 2\\Algo 2\\login.png")
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="#57a1f8",bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100,y=5)

#Input Username
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0, "Username")

user = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30,y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2,bg="black").place(x=25,y=107)

#Input Password
def on_enter(e):
    pasw.delete(0, "end")

def on_leave(e):
    password=pasw.get()
    if password == "":
        pasw.insert(0, "Password")

pasw = Entry(frame,width=25,fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
pasw.place(x=30,y=150)
pasw.insert(0, "Password")
pasw.bind("<FocusIn>", on_enter)
pasw.bind("<FocusOut>", on_leave)

Frame(frame,width=295, height=2,bg="black").place(x=25,y=177)

#Button
Button(frame,width=39,pady=7,text="Sign up", bg="#57a1f8",fg="white",border=0,command=SignIn).place(x=35,y=204)
label=Label(frame,text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signup_command)
sign_up.place(x=215,y=270)
root.mainloop()