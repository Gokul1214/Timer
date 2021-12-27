import pygubu
import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import os

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "TIMER.ui")


class TimerApp:

    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', parent)
        builder.connect_callbacks(self)
        self.hour_entry = builder.get_object('hour_entry', parent)
        self.min_entry = builder.get_object('min_entry', parent)
        self.sec_entry = builder.get_object('sec_entry', parent)
        self.hour_entry.insert(0, "0")
        self.min_entry.insert(0, '0')
        self.sec_entry.insert(0, '0')
        self.flag = -1

    #The stop button
    def pause(self):
        #sets flag to 0 to stop the loop in calculate
        self.flag = 0

    #The start button
    def calculate(self):
        temp = 0
        self.flag = -1

        temp_hour = temp_min = temp_sec = 0

        try:
            # the input provided by the user is
            # stored in here: temp
            temp_hour = int(self.hour_entry.get()) * 3600
            temp_min = int(self.min_entry.get()) * 60
            temp_sec = int(self.sec_entry.get())

            if (temp_hour >= 0) & (temp_min >= 0) & (temp_sec >= 0):
                temp = temp_hour + temp_min + temp_sec
            else:
                messagebox.showerror("Error", "Please type in only POSITIVE numeric values")
                self.hour_entry.delete(0, END)
                self.min_entry.delete(0, END)
                self.sec_entry.delete(0, END)

                self.hour_entry.insert(0, '0')
                self.min_entry.insert(0, '0')
                self.sec_entry.insert(0, '0')
                return

        #Must display error message when user inputs characters
        except:
            messagebox.showerror("Error", "Please type in only POSITIVE numeric values")
            self.hour_entry.delete(0, END)
            self.min_entry.delete(0, END)
            self.sec_entry.delete(0, END)

            self.hour_entry.insert(0, '0')
            self.min_entry.insert(0, '0')
            self.sec_entry.insert(0, '0')
            return

        #decrements the temp value and diplays it onto the GUI

        while (temp > -1) & (self.flag == -1):

            print(temp)
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            min, sec = divmod(temp, 60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hour = 0
            if min > 60:
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hour, min = divmod(min, 60)

            #old values in the GUI need to be delted
            self.hour_entry.delete(0, END)
            self.min_entry.delete(0, END)
            self.sec_entry.delete(0, END)

            #New time values are stored here
            self.hour_entry.insert(0, str(hour))
            self.min_entry.insert(0, str(min))
            self.sec_entry.insert(0, str(sec))

            #have a message box window open here to display message when timer ends
            if(temp == 0):
                messagebox.showinfo("Info", "The timer has ended!!!!")
            print(int(self.sec_entry.get()))

            #updates the GUI with new values
            root.update()
            time.sleep(1)

            temp -= 1

    def run(self):
        self.mainwindow.mainloop()

root = tk.Tk()
app = TimerApp(root)
#Runs the window
app.run()

