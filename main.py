from tkinter import *
import customtkinter as ctk
from tkinter import ttk


start_button_active = True


def start():
    global start_button_active
    start_button_active = True
    duration = int(slider.get())
    btn_start.place_forget()
    btn_stop.place(relx=0.48, rely=0.9, anchor=CENTER)
    while duration:
        if start_button_active == True:
            m, s = divmod(int(duration), 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            count_digit['text'] = min_sec_format
            count_digit.update()
            root.after(1000)
            duration -= 1
        else:
            Time()
            return


def stop():
    global start_button_active
    start_button_active = False
    btn_stop.place_forget()
    btn_start.place(relx=0.48, rely=0.9, anchor=CENTER)


def Time():
    duration = int(slider.get())
    m, s = divmod(int(duration), 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    count_digit['text'] = min_sec_format
    count_digit.update()


def sliderChanged(event):
    Time()


root = Tk()
print("Hello World!")
root.title('Confidence')
root.geometry('480x480')
root.iconbitmap("source/cat.ico")
root.configure(background="#1fab67")

count_digit = Label(root, text='00:00', font="Arial 30", background="#1fab67")
count_digit.place(relx=0.48, rely=0.8, anchor=CENTER)


slider = ctk.CTkSlider(master=root, from_=600, to=7200, number_of_steps=22, progress_color="#04e300",
                       button_color="#09ba0f", button_hover_color="#09ba0f", command=sliderChanged)

slider.pack()
Time()

font = ctk.CTkFont(family='Bryndan Write', size=18)

btn_start = ctk.CTkButton(root, text='Посадить', fg_color="#34d989", hover_color="#e5f0a3", font=font,
                     text_color="white", border_color="black", border_width=2, command=start)
btn_start.place(relx=0.48, rely=0.9, anchor=CENTER)

btn_stop = ctk.CTkButton(root, text='Остановить', fg_color="#34d989", hover_color="#e5f0a3", font=font,
                     text_color="white", border_color="black", border_width=2, command=stop)

root.mainloop()

