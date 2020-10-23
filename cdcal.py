import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from dateutil.relativedelta import relativedelta
import cdsave
import tkcalendar as tkc

class App:

    def __init__(self, root):
        """ initialize attributes and widjets """    
        #store the number of times calculate buttons are clicked
        self.no_of_times_clicked: int = 0
        self.no_of_times_clicked2: int = 0
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
        helpmenu.add_command(label = "Help Demo")#,command = help)

        menubar.add_cascade(label = "File", menu = filemenu)
        menubar.add_cascade(label = "Help", menu = helpmenu)
        menubar.add_command(label = "About", command = self.about_dev) 

        root.config(menu = menubar)

        tab_control = ttk.Notebook(root)
        tab_control.grid(row = 0, column = 0)
        tab1 = ttk.Frame(tab_control, width = 300, height = 500)
        tab2 = ttk.Frame(tab_control, width = 300, height = 500)
        tab_control.add(tab1, text = "Difference between dates")
        tab_control.add(tab2, text = "Add or subtract dates")

        #====================Tab1==============================#
        #---------------------Frames----------------------------------------------------------
        top1 = tk.Frame(tab1, width = 290, height = 75, bd = 8, relief = "groove",\
                        bg = "White")
        top1.grid(row = 1, column = 0, columnspan = 2, pady = 10, padx = 10,\
                  sticky = "WE")

        right1 = tk.Frame(tab1, width = 100, height = 75, bd = 0, relief = "groove",\
                          bg = "White")
        right1.grid(row = 2, column = 0, columnspan = 2, pady = 0, padx = 10,\
                    sticky = "E" )

        middle = tk.Frame(tab1, width = 290, height = 75, bd = 8, relief = "groove",\
                          bg = "White")
        middle.grid(row = 3, column = 0, columnspan = 2, pady = 10,padx = 10,\
                    sticky = "WE")

        right2 = tk.Frame(tab1, width = 100, height = 75, bd = 0, relief = "groove",\
                          bg = "White")
        right2.grid(row = 4, column = 0, columnspan = 2, pady = 0, padx = 10,\
                    sticky = "E" )


        #-------------------------------------------------------------------------------------------
        name = tk.Label(top1, font = ("Arial",10), text = "Description: ", fg = "black", bg = "White")
        name.grid(row = 0, column = 0, padx = 3, pady = 3)

        self.name_input = tk.StringVar()
        self.name_box = tk.Entry(top1, textvariable = self.name_input, bd = 3, bg = "powderblue", exportselection = 0)
        self.name_box.grid(row = 0, column = 1, padx = 3, pady = 3)

        date1 = tk.Label(top1, font = ("Arial",10), text = "From: ",fg = "black",width = 9, bg = "White")
        date1.grid(row = 1, column = 0, padx = 3, pady = 3)

        date2 = tk.Label(top1, font = ("Arial",10), text = "To: ",fg = "black",width = 9, bg = "White")
        date2.grid(row = 1, column = 1, padx = 3, pady = 3)


        self.date_input1 = tk.StringVar()
        self.date_box1 = tkc.DateEntry(top1, textvariable = self.date_input1, bd = 3, bg = "powderblue",
                        date_pattern = "d/m/y", firstweekday = "sunday", selectbackground = "red",
                                       justify = "center")
        self.date_box1.grid(row = 2, column = 0, padx = 3, pady = 3)
        
        self.date_input2 = tk.StringVar()
        self.date_box2 = tkc.DateEntry(top1, textvariable = self.date_input2, bd = 3, bg = "powderblue",
                        date_pattern = "d/m/y", firstweekday = "sunday", selectbackground = "red", justify = "center")
        self.date_box2.grid(row = 2, column = 1, padx = 3, pady = 3)

        cal_btn = tk.Button(right1, text = "Calculate", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.display_diff, fg = "red", bg = "lightblue")
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
        self.status_text = tk.Label(tab1, font = ("Arial",10), textvariable = self.status,\
                               relief = "sunken", anchor = "e", width = "38", bg = "White", fg = "Red", bd = 3)
        self.status_text.grid(row = 5, column = 0, padx = 0)

        #====================Tab2==============================#
        from_lbl = tk.Label(tab2, text = "From ", font = ("Arial",10), fg = "black")
        from_lbl.grid(row = 0, column = 0)

        self.from_date = tkc.DateEntry(tab2, bd = 3, bg = "powderblue", date_pattern = "d/m/y",
                                  firstweekday = "sunday", selectbackground = "red", justify = "center")
        self.from_date.grid(row = 0, column = 1)

        self.operation = tk.StringVar(value = "add")
        
        add_option = tk.Radiobutton(tab2, variable = self.operation, value = "add")
        add_option.grid(row = 0, column = 2)

        add_lbl = tk.Label(tab2, text = "Add", font = ("Arial", 10), fg = "black", anchor = "w")
        add_lbl.grid(row = 0, column = 3)

        sub_option = tk.Radiobutton(tab2, variable = self.operation, value = "subtract")
        sub_option.grid(row = 0, column = 4)

        sub_lbl = tk.Label(tab2, text = "Subtract", font = ("Arial", 10), fg = "black", anchor = "w")
        sub_lbl.grid(row = 0, column = 5)

        year_lbl = tk.Label(tab2, text = "Year(s)", font = ("Arial", 10), fg = "black", anchor = "w")
        year_lbl.grid(row = 1, column = 0, sticky = "w")

        self.year_input = tk.IntVar(value = 0)
        self.year_box = ttk.Spinbox(tab2, textvariable = self.year_input, from_ = 0, to = 999, width = 4)
        self.year_box.grid(row = 1, column = 1)

        month_lbl = tk.Label(tab2, text = "Month(s)", font = ("Arial", 10), fg = "black", anchor = "w")
        month_lbl.grid(row = 1, column = 2)

        self.month_input = tk.IntVar(value = 0)
        self.month_box = ttk.Spinbox(tab2, textvariable = self.month_input, from_ = 0, to = 999, width = 4)
        self.month_box.grid(row = 1, column = 3)


        day_lbl = tk.Label(tab2, text = "Day(s)", font = ("Arial", 10), fg = "black", anchor = "w")
        day_lbl.grid(row = 1, column = 4)

        self.day_input = tk.IntVar(value = 0)
        self.day_box = ttk.Spinbox(tab2, textvariable = self.day_input, from_ = 0, to = 999, width = 4)
        self.day_box.grid(row = 1, column = 5)

        date_lbl = tk.Label(tab2, text = "Date", font = ("Arial", 10), fg = "black", anchor = "w")
        date_lbl.grid(row = 2, column = 0)

        self.date_box = tk.Entry(tab2, bg = "powderblue", fg = "black", font = ("Arial", 10), width = 45)
        self.date_box.grid(row = 3, column = 0, columnspan = 5)

        right1 = tk.Frame(tab2, width = 100, height = 75, bd = 0, relief = "groove",\
                          bg = "White")
        right1.grid(row = 4, column = 0, columnspan = 5, pady = 0, padx = 10,\
                    sticky = "E" )

        cal_btn = tk.Button(right1, text = "Calculate", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.display_date, fg = "red", bg = "lightblue")
        cal_btn.grid(row = 0, column = 0, padx = 0, pady = 0)
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
        self.date_box1.set_date(date.today())
        self.date_box2.set_date(date.today())
        self.message1.set("")
        self.message2.set("")
        self.status.set("")
        self.status_text.configure(fg = "Black")
        self.status.set("Data cleared")

        
    def diff_between_dates(self, date_2, date_1) -> tuple :
        """ calculate the days between dates """
        
        diff_bet_days = (date_2 - date_1).days

        difference = relativedelta(date_2, date_1)
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

    def addorsub(self, date: date, years: str, months: str, days: str, operation: str) -> date:
        """ adds or subtracts year(s), month(s) or day(s) to a date """
        
        try:
            years = int(years)
            months = int(months)
            days = int(days)
            print(type(date))
            if operation.title() == "Add":
                result = date + relativedelta(years = years, months = months, days = days)
                return result
            else:
                result = date + relativedelta(years = -years, months = -months, days = -days)
                return result
        except ValueError:
            pass            

    def check_plurality(self, message: str, quantity: int, pluword: str = "days", singword: str = "day") -> str:
        """ returns a new string with correct syntax in terms of plurality """
        if int(quantity) <= 1:
            c_message = message.replace(pluword, singword)
            return c_message
        else:
            return message
        
    def display_diff(self):
        """ displays the result to their respective widget """      
        self.no_of_times_clicked += 1
        print(self.date_box1.get_date())
        if self.date_box1.get_date() != self.date_box2.get_date():
            diff = self.diff_between_dates(self.date_box2.get_date(), self.date_box1.get_date())
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
        return self.date_box1.get_date(), self.date_box2.get_date()

    def display_date(self):
        """ displays the result to self.date_box entry of tab2 """
        self.no_of_times_clicked2 += 1
        answer = self.addorsub(self.from_date.get_date(), self.year_box.get(), self.month_box.get(),
                               self.day_box.get(), self.operation.get())
        print(type(answer))
        message = answer.strftime("%A,%B %d, %Y")
        if self.no_of_times_clicked2 > 1:
            self.date_box.delete(0,"end")
        else:
            pass
        self.date_box.insert(0,message)
        
    def save(self):
        """ enables data to be typed on stickynote """
        date = self.display_diff()
        cdsave.openstickynote()
        cdsave.writedata(date = date, description = self.name_box.get(), \
                        message = self.message_box1.get() + "\n" + self.message_box2.get())

#=======================================================================================
if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Countdown Calendar")
    root.geometry("310x390+0+0")
    root.resizable(1,1)
    root.iconbitmap(r".\cc.ico") #r indicate raw string [it ignore \ as esc char]
    root.configure(bg = "Red")
    cdcal = App(root)
    root.mainloop()
