from tkinter import *
import tkinter as tk
from PIL import Image , ImageTk
import time 
from time import sleep
from tkinter import messagebox
from plyer import notification

t=tk.Tk()
t.title("Task-Remainder-Application")
t.geometry("500x400")



#code
def get_remaind():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time.get()

    if  get_title =="" or get_msg =="" or get_time== "":
        messagebox.showerror("Alert","All fields are Mandatory")
    else:
        int_time = int (float(get_time))
        min = int_time * 60
        messagebox.askquestion("Notifier_set","Are you want to Set Notification")
        t.destroy()
        sleep(min)
        notification.notify(title =get_title,
                    message =get_msg,
                    app_icon =None,
                    app_name ="Task_Remainder",
                    timeout =10)
                    
t_main = Label(t,text="* Get your Notification on Time *", font=("cambria",20,'underline'),fg="#be2ed6")
t_main.place(x=70,y=30 , anchor=NW)


#title_label
t_label = Label(t,text="Task Label ", font=("georgia",12),fg="#000000")
t_label.place(x=30,y=80)
#title
title = tk.Entry(t, width="25", font= ("cambria",13),borderwidth="2")
title.place(x=130,y=80)

#msg_label
msg_label = Label(t,text="Description", font=("georgia",12))
msg_label.place(x=30,y=125)

#msg
msg = tk.Entry(t, width="35", font= ("cambria",13),borderwidth="2")
msg.place(x=130,y=120,height=30)

#rem_label
time_label = Label(t,text="Set Time", font=("georgia",12))
time_label.place(x=30,y=170)

#rem
time = tk.Entry(t, width="5", font= ("cambria",13),borderwidth="2")
time.place(x=130,y=170)

#time 
min_label = Label(t,text="Enter the value in minute", font=("cambria",10,'italic'),fg="#808080")
min_label.place(x=189,y=170)

button = Button (t,text="Apply Remainder",font=("georgia",11,'bold' ),fg= "#ffffff", bg="#800080", width=20, relief="ridge",justify="center", command=get_remaind)
button.place(x=140,y=250)




t.resizable(0,0)
t.mainloop()
