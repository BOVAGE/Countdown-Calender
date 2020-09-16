import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
import time,cdsave

class App:

    def __init__(self, root):
        """ initialize attributes and widjets """    
        #today stores the date value of the current day
        #stores the number of times calculate button is clicked
        self.today, self.no_of_times_clicked = date.today(), 0

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
        self.date_box = tk.Entry(top1, textvariable = self.date_input, bd = 3, bg = "powderblue")
        self.date_box.grid(row = 1, column = 1, padx = 3, pady = 3)

        cal_btn = tk.Button(right1, text = "Calculate", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.display_days, fg = "red", bg = "lightblue")
        cal_btn.grid(row = 0, column = 0, padx = 0, pady = 0)

        reset_btn = tk.Button(right2, text = "Reset", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                         command = self.reset, fg = "red", bg = "lightblue")
        reset_btn.grid(row = 0, column = 1)

        self.message1 = tk.StringVar()
        self.message_box1 = tk.Entry(middle, font = 28, bd = 5, textvariable = self.message1,\
                                fg = "Black",bg = "powderblue")
        self.message_box1.grid(row = 1, column = 0, pady = 5)

        self.message2 = tk.StringVar()
        self.message_box2 = tk.Entry(middle, font = 28, bd = 5, textvariable = self.message2, \
                                fg = "Black",bg = "powderblue")
        self.message_box2.grid(row = 2, column = 0, pady = 5)

        difference = tk.Label(middle, font = ("Arial",11,"bold"), text = "Difference",\
                              bg = "White")
        difference.grid(row = 0, column = 1)

        days = tk.Label(middle, font = ("Arial",11,"bold"), text = "In days",\
                        bg = "White")
        days.grid(row = 1, column = 1)

        weeks = tk.Label(middle, font = ("Arial",11,"bold"), text = "In weeks",\
                        bg = "White")
        weeks.grid(row = 2, column = 1)

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
        self.message1.set("")
        self.message2.set("")
        self.status.set("")
        time.sleep(0.1)
        self.status_text.configure(fg = "Black")
        self.status.set("Data cleared")

        
    def days_between_dates(self, date2, date1):
        """ calculate the days between dates """
        
        #has to be converted to string object so as to use method split
        number_of_days = str(date2 - date1).split(" ")
        return number_of_days

    def validate_date(self, d1):
        """ to format date typed correctly """
        #to do
        #allow the user to use - or , or !
        if d1.find("/") >= 0:
            if d1.count("/") == 2:
                d1_list = d1.split("/") 
                if len(d1_list[2]) == 4: # checks whether the year is written in 20**
                    #converts the string entered to date object
                    date_format = datetime.strptime(d1, "%d/%m/%Y").date() 
                    return date_format
                elif len(d1_list[2]) == 2: # checks whether the year is written in **
                    #converts the string entered to date object
                    date_format = datetime.strptime(d1, "%d/%m/%y").date() 
                    return date_format
                elif len(d1_list[2]) == 0 or len(d1_list[2]) == 1:
                    pass
                    # message on status bar
                    # status.set("You did not input the year for the date")
            elif d1.count("/") == 1 or d1.count("/") == 0:
                pass
                # status_text.configure(fg = "Red")
                # status.set("Date typed isn't complete!")
            else:
                pass
                # status_text.configure(fg = "Red")
                # status.set("Type a Valid date!")
        
        elif d1.find("/") <  0:
            pass
            # status_text.configure(fg = "Red")
            # status.set("Ensure '/' is included")
        else:
            pass
            # status_text.configure(fg = "Red")
            # status.set("Type a Valid date!")

            
    def display_days(self):
        """ displays the result to their respective widget """
        
        self.no_of_times_clicked += 1
        try:
            format_date = self.validate_date(self.date_box.get())
            number_of_days = self.days_between_dates(format_date,self.today)
            
            message1 = f"It is {number_of_days[0]} days until {self.name_box.get()}."
            
            #to display difference in weeks too
            number_of_weeks = int(number_of_days[0]) // 7
            weeks_days_left = int(number_of_days[0]) % 7
            
            #print(number_of_weeks)
            print(weeks_days_left)
            
            message2 = \
            f"It is {number_of_weeks} weeks, {weeks_days_left} days until  {self.name_box.get()}."
            
            #to delete the previous messages if the calculate button has been 
            #pressed once
            if self.no_of_times_clicked > 1:
                self.message_box1.delete(0,len(message1) + 1)
                self.message_box2.delete(0,len(message2) + 1)
            else:
                pass
            self.message_box1.insert(0,message1)
            self.message_box2.insert(0,message2)
            
            #to store the date that will be typed in stickynote since format_date 
            #will be deleted later
            fformat_date = format_date
            #to solve this issue
            #the date typed isn't really deleted cause another variable is used to
            #store the date
            del format_date
            
            self.status_text.configure(fg = "Black")
            self.status.set("Done!")
            return fformat_date
        
        except (NameError, IndexError, TypeError, ValueError):
            self.status_text.configure(fg = "Red")
            self.status.set("Type a valid date!!!")

    def save(self):
        """ enables data to be typed on stickynote """
        
        date = self.display_days()
        cdsave.openstickynote()
        time.sleep(2)
        cdsave.writedata(date = date, description = self.name_box.get(), \
                        message = self.message_box1.get() + "\n" + self.message_box2.get())

#=======================================================================================
if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Countdown Calendar")
    root.geometry("310x341+0+0")
    root.resizable(0,0)
    root.iconbitmap(r".\cc.ico") #r indicate raw string [it ignore \ as esc char]
    root.configure(bg = "Red")
    cdcal = App(root)
    root.mainloop()
