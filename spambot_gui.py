from keyboard import press
import pyautogui
import time
import multiprocessing
from tkinter import *

#exit
def stop():
    exit(0)

#spam start
def spam(spam_text, num):
    time.sleep(5)
    for _ in range(int(num)):
        time.sleep(0.3)
        pyautogui.typewrite(spam_text)
        press('enter')

#thread start and updates
def thread(spam_text, num):
    global multi_process
    multi_process = multiprocessing.Process(target=spam, args=(spam_text, num))
    multi_process.daemon = True
    multi_process.start()
    button.config(text="Exit", command=stop)

#help window
def Help():
    window = Tk()
    window.iconbitmap('favicon.ico')
    window.config(background="#2c3e50")
    #window.iconbitmap('favicon.ico')
    window.minsize(800, 130)
    window.maxsize(800, 130)
    window.title("Help")
    Label(window, text="Tool:\n Simple Spam Bot", bg="#2c3e50", fg="white").pack()
    Label(window, text="\nUsage:\nType in the text you want to spam in the first entry box and the number of times(Integer only) in the second entry box both are mandatory\n or the application won't work. Click on the start button and the spam will begin in 5 seconds, point the cursor to the input box in the meantime\n If the spam doesn't begin something must be wrong in the user input. Restart the application and type in valid input", bg="#2c3e50", fg="white").pack()        

if __name__ == "__main__":
    root = Tk()
    root.title("Spam Bot")
    root.iconbitmap('favicon.ico')
    root.config(background="#2c3e50")
    root.minsize(620, 180)
    root.maxsize(620, 180)


    #Top Menu bar
    menu = Menu(root)
    root.config(menu=menu)

    #Submenu
    submenu = Menu(menu)
    menu.add_cascade(label="File", menu=submenu)
    submenu.add_command(label="Exit", command=stop)
    menu.add_command(label="Help", command=Help)

    label = Label(root, text="Enter the Spam text", bg="#2c3e50", fg="white")
    label.grid(row=0, column=0, pady=5)

    spam_text = StringVar()
    text = Entry(root, textvariable=spam_text, bd=1, width=100, bg="#34495e", fg="white")
    text.grid(row=1, column=0, padx=7)

    label2 = Label(root, text="Number of times to spam", bg="#2c3e50", fg="white")
    label2.grid(row=2, column=0, pady=5)

    num = StringVar()
    text2 = Entry(root, textvariable=num, bd=1, width=7, bg="#34495e", fg="white")
    text2.grid(row=3, column=0)

    global button
    button = Button(root, text="Start", width=20, bd=1, bg="#34495e", fg="white", command=lambda: thread(spam_text.get(), num.get()))
    button.grid(row=4, column=0, pady=15)
    root.mainloop()
