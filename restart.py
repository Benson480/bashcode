##import tkinter as tk
##from tkinter import messagebox
##import os
##
##def restart():
##    global window
##    answer = messagebox.askyesno("Do you want to restart a computer?")
##    if answer == True:
##        os.system("shutdown -r")
##        messagebox.showwarning("Restarting computer!")
##
##window = tk.Tk()
##button = tk.Button(window, text="Quit", bg="red", command=restart)
##button.pack()
##
##window.mainloop()

##from tkinter import *
##from tkinter import messagebox
##import os
##
##root = Tk()
##root.title("Menu")
##root.iconbitmap("myapp.png")
##root.geometry("400x400")
##
##
##my_menu = Menu(root)
##root.config(menu=my_menu)
##
###click command
##
##def our_command():
##    pass
##
##def start_settings():
##    messagebox.showinfo("Going to settings")
##    os.system("start ms-settings:")
##
##def start_chrome():
##    messagebox.showinfo("Starting chrome")
##    os.system("start chrome")
##
##def computer_hibanate():
##    answer = messagebox.askyesno("Are you sure you\nwant to shutdown")
##    if answer == True:
##        messagebox.showwarning("Shutting down the computer!")
##        os.system("shutdown -h")
##def kill_excel():
##    answer = messagebox.askyesno("Are you sure you\nwant to kill excel?")
##    if answer == True:
##        messagebox.showwarning("Shutting down the excel!")
##        os.system("taskkill /f /im excel.exe")
##def restart_computer():
##    answer = messagebox.askyesno("Are you sure you\nwant to restart computer?")
##    if answer == True:
##        messagebox.showwarning("restarting computer!")
##        os.system("shutdown -r")
##
##def destroy_window():
##    answer = messagebox.askyesno("Are you sure you\nwant to Quit the app?")
##    if answer == True:
##        messagebox.showwarning("Closing the application!")
##        root.destroy()
##
###create a menu item
##
##file_menu = Menu(my_menu)
##my_menu.add_cascade(label="File", menu=file_menu)
##file_menu.add_command(label="New...", command=our_command)
##file_menu.add_separator()
##file_menu.add_command(label="Exit", command=destroy_window)
##
###create edit menu item
##edit_menu = Menu(my_menu)
##my_menu.add_cascade(label="Edit", menu=edit_menu)
##edit_menu.add_command(label="Cut", command=our_command)
##edit_menu.add_separator()
##edit_menu.add_command(label="Copy", command=our_command)
##
###Create option menu
##option_menu = Menu(my_menu)
##my_menu.add_cascade(label="Options", menu=option_menu)
##option_menu.add_command(label="Find", command=our_command)
##option_menu.add_separator()
##option_menu.add_command(label="Replace", command=our_command)
##
##help_menu = Menu(my_menu)
##my_menu.add_cascade(label="Help", menu=help_menu)
##help_menu.add_command(label="About app", command=our_command)
##help_menu.add_separator()
##help_menu.add_command(label="App help", command=our_command)
##
##
##frame = Frame(root, height=380, width=380, bg="blue")
##frame.pack(expand=True, fill=BOTH)
##label = Label(frame, text="This is an app for simple task", bg="gray")
##label.pack(expand=True, fill=BOTH)
##s_button = Button(frame, text="settings", bg="green", activebackground="green",
##                     command=start_settings)
##s_button.pack(expand=True)# fill=tk.BOTH)
##c_button = Button(frame, text="chrome", bg="yellow", activebackground="green",
##                     command=start_chrome)
##c_button.pack(expand=True, fill=BOTH)
##
##sh_button = Button(frame, text="Hibenate", bg="red", activebackground="red",
##                     command=computer_hibanate)
##sh_button.pack(expand=True)
##
##ks_button = Button(frame, text="kill excel", bg="red", activebackground="red",
##                     command=kill_excel)
##ks_button.pack(expand=True)
##
##rc_button = Button(frame, text="restart computer", bg="red", activebackground="red",
##                     command=restart_computer)
##rc_button.pack(expand=True)
##root.mainloop()


from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Menu")
root.iconbitmap("myapp.png")
root.geometry("400x400")

canvas = Canvas(root, width = 400, height=400)
canvas.create_oval(10, 10, 100, 100, fill='gray90')
canvas.create_line(105,10,200,105, fill='gray3')
canvas.create_rectangle(205, 10, 300, 105, outline='white', fill='gray50')
canvas.create_bitmap(355, 53, bitmap='questhead')

xy = 10, 105, 100, 200
canvas.create_arc(xy, start=0, extent=270, fill='gray60')
canvas.create_arc(xy, start=270, extent=5, fill='gray70')
canvas.create_arc(xy, start=275, extent=35, fill='gray80')
canvas.create_arc(xy, start=310, extent=49, fill='gray90')

canvas.create_polygon(205, 105, 285, 125, 166, 177, 210, 199, 205, 105, fill='white')
canvas.create_text(350, 150, text='text', fill='blue', font=('Verdana', 36))

img = ImageTk.PhotoImage(file='myapp.png')
canvas.create_image(145, 280, image=img, anchor=CENTER)

frm = Frame(canvas, relief=GROOVE, borderwidth=2)
Label(frm, text="Embedded Frame/Label").pack()
canvas.create_window(285, 280, window=frm, anchor=CENTER)
canvas.pack()




root.mainloop()
