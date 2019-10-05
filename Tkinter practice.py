
# coding: utf-8

# In[18]:


from tkinter import *
        
w=Tk()
w.title("IIIT Pune Login System")
w.geometry("600x400")
w.resizable(0,0)
w.config(bg="white")
f=Frame(w,bg="white", width=600,height=400,relief="raised",bd=2)
Label(f,text="IIIT PORTAL",fg="green",bg="white").pack()
Label(f,text="Username",fg="black",bg="white").pack(pady=30)
e=Entry(f).pack()
Button(f,text="Next",fg="white",bg="blue").pack(pady=5)

Button(f,text="New User? Sign Up",fg="blue",bg="white",highlightthickness=0).pack(side="bottom")
f.pack(expand=YES,fill=BOTH,padx=100,pady=100)

if e=="admin":
    Label(f,text="Password",fg="black",bg="white").pack(pady=30)
    k=Entry(f).pack()


w.mainloop()

