import tkinter as tk
from tkinter import messagebox
from datetime import date
from dateutil import relativedelta
import cdsave
import tkcalendar as tkc

class App:

    def __init__(self, root):
        """ initialize attributes and widjets """    
        #today stores the date value of the current day
        #stores the number of times calculate button is clicked
        self.today, self.no_of_times_clicked = date.today(), 0
        print(self.today)
        #====================Menu bar ==============================#
        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff = 0)
        helpmenu = tk.Menu(menubar, tearoff = 0)
        aboutmenu = tk.Menu(menubar, tearoff = 0)

        filemenu.add_command(label = "Open")
        filemenu.add_command(label = "Save", command = self.save)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.exitroot)

        helpmenu.add_command(label = "Help Docs")
        helpmenu.add_command(label = "Help Demo")#,command = Help)

        menubar.add_cascade(label = "File", menu = filemenu)
        menubar.add_cascade(label = "Help", menu = helpmenu)
        menubar.add_command(label = "About", command = self.about_dev) 

        root.config(menu = menubar)


        #====================Widgets ==============================#
        #---------------------Frames----------------------------------------------------------
        top1 = tk.Frame(root, width = 290, height = 75, bd = 8, relief = "groove",\
                        bg = "White")
        top1.grid(row = 1, column = 0, columnspan = 2, pady = 10, padx = 10,\
                  sticky = "WE")

        right1 = tk.Frame(root, width = 100, height = 75, bd = 0, relief = "groove",\
                          bg = "White")
        right1.grid(row = 2, column = 0, columnspan = 2, pady = 0, padx = 10,\
                    sticky = "E" )

        middle = tk.Frame(root, width = 290, height = 75, bd = 8, relief = "groove",\
                          bg = "White")
        middle.grid(row = 3, column = 0, columnspan = 2, pady = 10,padx = 10,\
                    sticky = "WE")

        right2 = tk.Frame(root, width = 100, height = 75, bd = 0, relief = "groove",\
                          bg = "White")
        right2.grid(row = 4, column = 0, columnspan = 2, pady = 0, padx = 10,\
                    sticky = "E" )


        #-------------------------------------------------------------------------------------------
        name = tk.Label(top1, font = ("Arial",10), text = "Description: ", fg = "black", bg = "White")
        name.grid(row = 0, column = 0, padx = 3, pady = 3)

        date1 = tk.Label(top1, font = ("Arial",10), text = "Date: ",fg = "black",width = 9, bg = "White")
        date1.grid(row = 0, column = 1, padx = 3, pady = 3)

        self.name_input = tk.StringVar()
        self.name_box = tk.Entry(top1, textvariable = self.name_input, bd = 3, bg = "powderblue", exportselection = 0)
        self.name_box.grid(row = 1, column = 0, padx = 3, pady = 3)

        self.date_input = tk.StringVar()
        self.date_box = tkc.DateEntry(top1, textvariable = self.date_input, bd = 3, bg = "powderblue",
                        date_pattern = "d/m/y", firstweekday = "sunday")
        self.date_box.grid(row = 1, column = 1, padx = 3, pady = 3)

        cal_btn = tk.Button(right1, text = "Calculate", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.display_days, fg = "red", bg = "lightblue")
        cal_btn.grid(row = 0, column = 0, padx = 0, pady = 0)

        reset_btn = tk.Button(right2, text = "Reset", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.reset, fg = "red", bg = "lightblue")
        reset_btn.grid(row = 0, column = 1)

        differenceall = tk.Label(middle, font = ("Arial",11,"normal"),
                      text = "Difference(years, months, weeks, days)",\
                      bg = "White")
        differenceall.grid(row = 0, column = 0)

        self.message1 = tk.StringVar()
        self.message_box1 = tk.Entry(middle, font = 28, bd = 5, textvariable = self.message1,\
                                fg = "Black",bg = "powderblue", width = 28)
        self.message_box1.grid(row = 1, column = 0, pady = 5, sticky = "w")

        differenced = tk.Label(middle, font = ("Arial",11,"normal"),
                      text = "Difference(days)", 
                      bg = "White")
        differenced.grid(row = 2, column = 0, sticky = "w")

        self.message2 = tk.StringVar()
        self.message_box2 = tk.Entry(middle, font = 28, bd = 5, textvariable = self.message2, \
                                fg = "Black",bg = "powderblue", width = 28)
        self.message_box2.grid(row = 3, column = 0, pady = 5, sticky = "w")

        self.status = tk.StringVar()
        self.status_text = tk.Label(root, font = ("Arial",10), textvariable = self.status,\
                               relief = "sunken", anchor = "e", width = "38", bg = "White", fg = "Red", bd = 3)
        self.status_text.grid(row = 5, column = 0, padx = 0)

    #================================Functions=======================================================
    def exitroot(self):
        """ to exit the windows """

        #response stores the answer provided by the user
        response = messagebox.askyesno("Quit", "Are you sure you want to exit \
        Countdown Calender?", icon = "warning")
        print(response)
        #yes is clicked --> response = True
        if response == True:
            print("yes")
            root.destroy()
        else:
            print("No")

            
    def about_dev(self):
        """ to display information about the developer """

        response = messagebox.showinfo("About", 
        """This application was developed by Fayemi Boluwatife.
    Copyright 2020.
    Bovage INC
    """, icon = "info")
        print(response)
       

    def reset(self):
        """ clears all data on the windows """

        self.name_input.set("")
        self.date_input.set("")
        self.date_box.set_date(self.today)
        self.message1.set("")
        self.message2.set("")
        self.status.set("")
        self.status_text.configure(fg = "Black")
        self.status.set("Data cleared")

        
    def diff_between_dates(self, date_2, date_1):
        """ calculate the days between dates """
        diff_bet_days = (date_2 - date_1).days
        difference = relativedelta.relativedelta(date_2, date_1)
        diff_years = difference.years
        diff_months = difference.months
        diff_weeks = difference.weeks
        if difference.days % 7 == 0:
            diff_days = 0
        elif difference.days < 7:
            diff_days = difference.days
        elif difference.days > 7:
            diff_days = difference.days - (diff_weeks * 7)
        return diff_years, diff_months, diff_weeks, diff_days, diff_bet_days

    def check_plurality(self, message, quantity, pluword = "days", singword = "day"):
        """ returns a new string with correct syntax in terms of plurality """
        if int(quantity) <= 1:
            c_message = message.replace(pluword, singword)
            return c_message
        else:
            return message
        
    def display_days(self):
        """ displays the result to their respective widget """      
        self.no_of_times_clicked += 1
        print(self.date_box.get_date())
        if self.date_box.get_date() != self.today:
            diff = self.diff_between_dates(self.date_box.get_date(), self.today)
            print(diff)
            message1 = f"It is {diff[0]} years, {diff[1]} months, {diff[2]} weeks, {diff[3]} days until {self.name_box.get()}."
            message1 = self.check_plurality(pluword = "years", quantity = diff[0], message = message1, singword = "year") 
            message1 = self.check_plurality(pluword = "months", quantity = diff[1], message = message1, singword = "month")
            message1 = self.check_plurality(pluword = "weeks", quantity = diff[2], message = message1, singword = "week")
            message1 = self.check_plurality(pluword = "days", quantity = diff[3], message = message1, singword = "day")

            message2 = f"It is {diff[4]} days until {self.name_box.get()}."
            message2 = self.check_plurality(message2, diff[4])
        else:
            message1 = "Same dates."
            message2 = message1
        #do nothing
        #to delete the previous messages if the calculate button has been 
        #pressed once
        if self.no_of_times_clicked > 1:
            self.message_box1.delete(0,"end")
            self.message_box2.delete(0,"end")
        else:
            pass
        self.message_box1.insert(0,message1)
        self.message_box2.insert(0,message2)
        self.status_text.configure(fg = "Black")
        self.status.set("Done!")
        #to store the date that will be typed in stickynote 
        return self.date_box.get_date()

    def save(self):
        """ enables data to be typed on stickynote """
        date = self.display_days()
        cdsave.openstickynote()
        cdsave.writedata(date = date, description = self.name_box.get(), \
                        message = self.message_box1.get() + "\n" + self.message_box2.get())

#=======================================================================================
if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Countdown Calendar")
    root.geometry("310x365+0+0")
    root.resizable(0,0)
    root.iconbitmap(r".\cc.ico") #r indicate raw string [it ignore \ as esc char]
    root.configure(bg = "Red")
    cdcal = App(root)
    root.mainloop()
