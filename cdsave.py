import pyautogui as pg

def openstickynote():
    pg.hotkey("winleft")
    pg.typewrite("Sticky Note\n")


def writedata(date, description, message):
    pg.typewrite(str(date) + "\n")
    pg.typewrite(str(description) + "\n")
    pg.typewrite(str(message) + "\n")
    
    
