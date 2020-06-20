"""
This is a countdown calender app

written by Fayemi Boluwatife
"""

from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
import time

#today stores the date value of the current day
today = date.today()

#stores the number of times calculate button is clicked
no_of_times_clicked = 0


#================================Functions=======================================================
def exitroot():
    """ to exit the windows """

    #response stores the answer provided by the user
    response = messagebox.askyesno("Quit", "Are you sure you want to exit Countdown Calender?")
    print(response)
    #if yes is clicked --> response = True
    if response == True:
        print("yes")
        root.destroy()
    else:
        print("No")

        
def about_dev():
    """ display information about the developer """

    response = messagebox.showinfo("About", """This application was developed by Fayemi Boluwatife.
Copyright 2020.
Bovage INC
""")
    print(response)
   

def reset():
    """ clears everyone data on the windows """

    name_input.set("")
    date_input.set("")
    message1.set("")
    message2.set("")
    status.set("")
    time.sleep(0.1)
    status_text.configure(fg = "Black")
    status.set("Data cleared")

    
def days_between_dates(date2, date1):
    """ calculate the days between dates """

    global number_of_days
    #time_between has to be converted to string object so as to use method split
    time_between = str(date2 - date1)
    number_of_days = time_between.split(' ')


def convertdate():
    """This coverts today and format date to list  """
    global today
    global format_date1
    global covtd_today
    covtd_today = str(today)
    covtd_today = covtd_today.split(" ")
    
    format_date1 = str(format_date)
    format_date1 = format_date1.split(" ")


def validate_date(d1):
    global format_date
    #to do
    #allow the user to use - or , or !
    # try:
    if d1.find("/") >= 0:
        if d1.count("/") == 2:
            d1_list = d1.split("/") 
            if len(d1_list[2]) == 4: # checks whether the year is written in 20**
                format_date = datetime.strptime(d1, "%d/%m/%Y").date() #converts the string entered to date object
                convertdate()
                if format_date1[0] == covtd_today[0]:
                    format_date = datetime.strptime(d1, "%d/%m/%Y") #converts the string entered to date object
                else:
                    pass
                    
            elif len(d1_list[2]) == 2: # checks whether the year is written in **
                format_date = datetime.strptime(d1, "%d/%m/%y").date() #converts the string entered to date object
                convertdate()
                if format_date1[0] == covtd_today[0]:
                    format_date = datetime.strptime(d1, "%d/%m/%y") #converts the string entered to date object
                else:
                    pass
            
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

    # except ValueError:
        # status_text.configure(fg = "Red")
        # status.set("Type a Valid date!")
        
def display_days():
    global no_of_times_clicked
    global format_date
    global fformat_date
    no_of_times_clicked += 1
    try:
        validate_date(date_box.get())
        days_between_dates(format_date,today)
        
        message1 = "It is " + number_of_days[0] +" days until " + name_box.get() + "."
        
        #to display difference in weeks too
        number_of_weeks = int(number_of_days[0]) // 7
        weeks_days_left = int(number_of_days[0]) % 7
        
        #print(number_of_weeks)
        #print(weeks_days_left)
        
        message2 = f"It is {number_of_weeks} weeks, {weeks_days_left} days until  {name_box.get()}."
        
        #to delete the previous messages if the calculate button has been pressed once
        if no_of_times_clicked > 1:
            message_box1.delete(0,len(message1) + 1)
            message_box2.delete(0,len(message2) + 1)
        else:
            pass
        message_box1.insert(0,message1)
        message_box2.insert(0,message2)
        
        #to store the date that will be typed in stickynote since format_date will be deleted later
        fformat_date = format_date
        #to solve this issue
        #the date typed isn't really deleted cause another variable is used to store the date
        del format_date
        
        status_text.configure(fg = "Black")
        status.set("Done!")
    
    except (NameError, IndexError, TypeError, ValueError):
        status_text.configure(fg = "Red")
        status.set("Type a valid date!!!")
    
##    if int(number_of_days[0]) > 0:
##        message = "It is " + number_of_days[0] +" days until " + name_box.get() + " ."
##        message_box = Message(middle, font = 28, text = message, fg = "Red",anchor = CENTER, bg = "Blue")
##        message_box.grid()
##    else:
##        message =  name_box.get() + "was " + number_of_days[0] + " days ago."
##        message_box = Message(middle, font = 28, text = message, fg = "Red",anchor = CENTER, bg = "Blue")
##        message_box.grid()
##                
##



#=======================================================================================
root = Tk()
root.title("Countdown Calender")
root.geometry("310x331")
root.resizable(0,0)
root.iconbitmap(r".\cc.ico")
root.configure(bg = "Red")


#====================Menu bar ==============================#
menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
helpmenu = Menu(menubar, tearoff = 0)
aboutmenu = Menu(menubar, tearoff = 0)

filemenu.add_command(label = "Open")
filemenu.add_command(label = "Save")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exitroot)

helpmenu.add_command(label = "Help Docs")
helpmenu.add_command(label = "Help Demo")#,command = Help)

menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "Help", menu = helpmenu)
menubar.add_command(label = "About", command = about_dev) 

root.config(menu = menubar)


#====================Widgets ==============================#
#---------------------Frames----------------------------------------------------------
top1 = Frame(root, width = 290, height = 75, bd = 8, relief = "groove", bg = "White")
top1.grid(row = 1, column = 0, columnspan = 2, pady = 10, padx = 10, sticky = "WE")

right1 = Frame(root, width = 100, height = 75, bd = 0, relief = "groove", bg = "White")
right1.grid(row = 2, column = 0, columnspan = 2, pady = 0, padx = 10, sticky = "E" )

middle = Frame(root, width = 290, height = 75, bd = 8, relief = "groove", bg = "White")
middle.grid(row = 3, column = 0, columnspan = 2, pady = 10,padx = 10, sticky = "WE")

right2 = Frame(root, width = 100, height = 75, bd = 0, relief = "groove", bg = "White")
right2.grid(row = 4, column = 0, columnspan = 2, pady = 0, padx = 10, sticky = "E" )


#-------------------------------------------------------------------------------------------
name = Label(top1, font = ("Arial",10), text = "Description: ", fg = "black", bg = "White")
name.grid(row = 0, column = 0, padx = 3, pady = 3)

date1 = Label(top1, font = ("Arial",10), text = "Date: ",fg = "black",width = 9, bg = "White")
date1.grid(row = 0, column = 1, padx = 3, pady = 3)

name_input = StringVar()
name_box = Entry(top1, textvariable = name_input, bd = 3, bg = "powderblue", exportselection = 0)
name_box.grid(row = 1, column = 0, padx = 3, pady = 3)

date_input = StringVar()
date_box = Entry(top1, textvariable = date_input, bd = 3, bg = "powderblue")
date_box.grid(row = 1, column = 1, padx = 3, pady = 3)

cal_btn = Button(right1, text = "Calculate", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                 command = display_days, fg = "red", bg = "lightblue")
cal_btn.grid(row = 0, column = 0, padx = 0, pady = 0)

reset_btn = Button(right2, text = "Reset", bd = 5 , relief = "raise", width = 13, cursor = "dotbox", \
                 command = reset, fg = "red", bg = "lightblue")
reset_btn.grid(row = 0, column = 1)

message1 = StringVar()
message_box1 = Entry(middle, font = 28, bd = 5, textvariable = message1, fg = "Black",bg = "powderblue")
message_box1.grid(row = 1, column = 0, pady = 5)

message2 = StringVar()
message_box2 = Entry(middle, font = 28, bd = 5, textvariable = message2, fg = "Black",bg = "powderblue")
message_box2.grid(row = 2, column = 0)

difference = Label(middle, font = ("Arial",11,"bold"), text = "Difference", bg = "White")
difference.grid(row = 0, column = 1)

days = Label(middle, font = ("Arial",11,"bold"), text = "In days", bg = "White")
days.grid(row = 1, column = 1)

weeks = Label(middle, font = ("Arial",11,"bold"), text = "In weeks", bg = "White")
weeks.grid(row = 2, column = 1)

status = StringVar()
status_text = Label(root, font = ("Arial",10), textvariable = status, relief = "sunken", anchor = "e", width = "38", \
                    bg = "White", fg = "Red", bd = 3)
status_text.grid(row = 5, column = 0, padx = 0)

root.mainloop()

