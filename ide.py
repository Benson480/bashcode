##from tkinter import *
##root = Tk()
##list = Listbox(root, width=15)
##list.pack()
##for item in range(50):
##    list.insert(END, item)
##
##root.mainloop()

##from tkinter import *
##root = Tk()
##
##def setHeight(canvas, heightStr):
##    height = string.atoi(heightStr)
##    height = height + 21
##    y2 = height - 30
##    if y2 < 21:
##        y2 = 21
##    canvas.coords('poly',
##                  15,20,35,20,35,y2,25,height,5,y2,15,y2,15,20)
##    canvas.coords('line',
##                  15,20,35,20,35,y2,45,y2,25,height,5,y2,15,y2,15,20)
##    canvas = Canvas(root, width=50, height=50, bd=0, highlightthickness=0)
##    canvas.create_polygon(0,0,1,1,2,2,fill='cadetblue', tags='poly')
##    canvas.create_line(0,0,1,1,2,2,0,0, fill='black', tags='line')
##
##    scale = Scale(root, orient=VERTICAL, length=284, from_=0, to=250,
##                  tickinterval=50, command=lambda h, c=canvas:setHeight(c,h))
##    canvas.grid(row=0, column=1, sticky='NWSE')
##    scale.set(100)
##
##root.mainloop()

##from tkinter import *
##root = Tk()
##
##scale=Scale(root, length=284, from_=0, to=250).pack()
##root.mainloop()

##from tkinter import *
##root = Tk()
##root.geometry("400x400")
##frame = Frame(root, height=380, width=380, bg="#7e5b41")
##frame.pack()
##root.mainloop()
##
##fertilizer = input("Enter fertilizer: ")
##
##if fertilizer == "Potassium_Nitrate":
##    Potassium_Nitrate = {'K':38, 'No3':13}
##    for key, value in Potassium_Nitrate.items():
##        print("ppm of", key,'is-', value* 139.53/100)
##
##elif fertilizer == "Calcium_Nitrate":
##    Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
##    for key, value in Calcium_Nitrate.items():
##        print("ppm of", key,'is-', value* 476.74/100)
##


##from tkinter import ttk
##from tkinter import *
##
##root = Tk()
##
##def progress(pb):
##    pb = ttk.Progressbar(
##        root,
##        orient='horizontal',
##        mode='indeterminate',
##        length=600
##        )
##    pb.place(x = 10, y = 25)
##    pb.place(x = 10, y = 25)
##Button(root, text="start progress", command=progress.place(x=10, y=50)
##Button(root, text="stop progress", command=progress).place(x=10, y=75)
##
##root.mainloop() 
##for key, value in Potassium_Nitrate.items():
##    print("ppm of", key,'is-', value* 139.53/100)


##from tkinter import *
##import tkinter.ttk as ttk
##from tkinter import messagebox
##
##
##mainWindow = Tk()
##
##def update_progress_bar():
##    x = barVar.get()
##    if x < 100:
##        barVar.set(x+0.5)
##        mainWindow.after(50, update_progress_bar)
##    else:
##        messagebox.showinfo("Complete!")
##        messagebox.forget()
##
##
##barVar = DoubleVar()
##barVar.set(0)
##bar = ttk.Progressbar(mainWindow, length=200, style='black.Horizontal.TProgressbar', variable=barVar, mode='determinate')
##bar.grid(row=1, column=0)
##button= Button(mainWindow, text='Click', command=update_progress_bar)
##button.grid(row=0, column=0)
##
##mainWindow.mainloop()


##import tkinter as tk
##from tkinter import ttk
##
##root = tk.Tk()
##
##style = ttk.Style(root)
### add label in the layout
##style.layout('text.Horizontal.TProgressbar', 
##             [('Horizontal.Progressbar.trough',
##               {'children': [('Horizontal.Progressbar.pbar',
##                              {'side': 'left', 'sticky': 'ns'})],
##                'sticky': 'nswe'}), 
##              ('Horizontal.Progressbar.label', {'sticky': 'nswe'})])
### set initial text
##style.configure('text.Horizontal.TProgressbar', text='0 %', anchor='center')
### create progressbar
##variable = tk.DoubleVar(root)
##pbar = ttk.Progressbar(root, style='text.Horizontal.TProgressbar', variable=variable)
##pbar.pack()
##
##def increment():
##    pbar.step()  # increment progressbar 
##    style.configure('text.Horizontal.TProgressbar', 
##                    text='{:g} %'.format(variable.get()))  # update label
##    root.after(200, increment)
##    
##increment()
##
##root.mainloop()

##import time
##import tkinter as tk
##import tkinter.ttk as ttk
##
##tuple_1 = tuple(range(1, 25))
##
##def progress_bar_func(style, progress_bar, sequence):
##    root.after(500, update_progress_bar, style, progress_bar, 1, len(sequence))
##
##def update_progress_bar(style, progress_bar, num, limit):
##    if num <= limit:
##        percentage = round(num/limit * 100)  # Calculate percentage.
##        progress_bar.config(value=num)
##        style.configure('text.Horizontal.TProgressbar', text='{:g} %'.format(percentage))
##        num += 1
##        root.after(500, update_progress_bar, style, progress_bar, num, limit)
##
##root = tk.Tk()
##root.geometry("300x300")
##
##style = ttk.Style(root)
##style.layout('text.Horizontal.TProgressbar',
##             [('Horizontal.Progressbar.trough',
##               {'children': [('Horizontal.Progressbar.pbar',
##                              {'side': 'left', 'sticky': 'ns'})],
##                'sticky': 'nswe'}),
##              ('Horizontal.Progressbar.label', {'sticky': ''})])
##style.configure('text.Horizontal.TProgressbar', text='0 %')
##
##progress_bar = ttk.Progressbar(root, style='text.Horizontal.TProgressbar', length=200,
##                               maximum=len(tuple_1), value=0)
##progress_bar.pack()
##
##progress_button = tk.Button(root, text="start",
##                            command=lambda: progress_bar_func(style, progress_bar, tuple_1))
##progress_button.pack()
##
##root.mainloop()

##
##a_number = 0.20
##percentage = "{:.0%}".format(a_number)
##print(percentage)

##
##a_number = 0.20
##percentage = "{:.0%}".format(a_number)
##print(percentage)

volume = 430
t1 = 205
t2 = 60
t3 = 50
t4 = 12
t5 = 1.1
t6 = 60
t7 = 65
t8 = 30
t9 = 20
t10 = 0.04
t11 = 0.63
t12 = 0.75
t13 = 0.57
t14 = 35
t15 = 0

convert = 1000
g1 = t1 * convert
g2 = t2 * convert
g3 = t3 * convert
g4 = t4 * convert
g5 = t5 * convert
g6 = t6 * convert
g7 = t7 * convert
g8 = t8 * convert
g9 = t9 * convert
g10 = t10 * convert
g11 = t11 * convert
g12 = t12 * convert
g13 = t13 * convert
g14 = t14 * convert
g15 = t15 * convert

gm1 = g1 / volume
gm2 = g2 / volume
gm3 = g3 / volume
gm4 = g4 / volume
gm5 = g5 / volume
gm6 = g6 / volume
gm7 = g7 / volume
gm8 = g8 / volume
gm9 = g9 / volume
gm10 = g10 / volume
gm11 = g11 / volume
gm12 = g12 / volume
gm13 = g13 / volume
gm14 = g14 / volume
gm15 = g15 / volume

tno3 = 114.59
tca = 90.58
tammonium = 5.244
tca = 90.58

CalciumS = []
Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
for key, value in Calcium_Nitrate.items():
    if key == 'Ca':
        data1 = round(value * gm1 /100,2)
        print("ppm ca",data1)
        rdata1 = round((data1 * volume) /(10*value),0)
        rca = round((tca* volume) /(10*value),0)
##        print("Probable ca:", rca)
    elif key == 'No3':
        data2 = (value * gm1 /100)
        rdata2 = round((data2 * volume) /(10*value),0)
        rno3 = (data2/tno3*rdata2)
##        print("Probable no3:", rno3)
    elif key == 'N-NH4':
        data3 = value * gm1 /100
        rdata3 = round((data3 * volume) /(10*value),0)
        rammonium = round((tammonium* volume) /(10*value),0)/2
##        print("Probable ammonium:", rammonium)
        Calcium_nitrate = rca + rno3 + rammonium
##        print("Calcium nitrate1-",Calcium_nitrate)
##        print("Calcium nitrate-",rdata3)
        print(max(rdata1, rdata2, rdata3))

NitrateS = []
Potassium_Nitrate = {'K':38, 'No3':13}
for key, value in Potassium_Nitrate.items():
    if key == 'K':
        data4 = (value * gm2 /100)
        rdata4 = round((data4 * volume) /(10*value),0)
    elif key == 'No3':
        data5 = value * gm2 /100
        rdata5 = round((data5 * volume) /(10*value),0)
        print(max(rdata4,rdata5))
        rno31 = round((tno3* volume) /(10*value),0)/4
##        print("Probable:", rno31)


MagnesiumS = []
Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
for key, value in Magnesium_Nitrate.items():
    if key == 'No3':
        data6 = value * gm3 /100
        rdata6=round((data6 * volume) /(10*value),0)
    elif key == 'Mg':
        data7 = (value * gm3 /100)
        rdata7 = round((data7 * volume) /(10*value),0)
        print(max(rdata6,rdata7))

FerillineS = []
Ferilline = {'Fe':6}
for key, value in Ferilline.items():
    data8 = value * gm4 /100
    rdata8=round((data8 * volume) /(10*value),0)
    print(rdata8)
    
BoraxS = []    
Borax = {'B':11}
for key, value in Borax.items():
    data9 = value * gm5 /100
    rdata9=round((data9 * volume) /(10*value),1)
    print(rdata9)
    
sulphateS = []    
Magnesium_sulphate = {'S':14,'Mg':9.1}
for key, value in Magnesium_sulphate.items():
    if key == 'S':
        data10 = value * gm6 /100
        rdata10=round((data10 * volume) /(10*value),0)
    elif key == 'Mg':
        data11 = (value * gm6 /100)
        rdata11=round((data11 * volume) /(10*value),0)
        print(max(rdata10,rdata11))
 

phosphateS = []    
Mono_p_phosphate = {'K':28, 'P':22.5}
for key, value in Mono_p_phosphate.items():
    if key == 'K':
        data12 = value * gm7 /100
        rdata12 =round((data12 * volume) /(10*value),0)
    elif key == 'P':
        data13 = (value * gm7 /100)
        rdata13=round((data13 * volume) /(10*value),0)
        print(max(rdata12, rdata13))

PotassiumS = []    
Potassium_sulphate = {'K':43, 'S':18}
for key, value in Potassium_sulphate.items():
    if key == 'K':
        data14 = value * gm8 /100
        rdata14=round((data14 * volume) /(10*value),0)
    elif key == 'S':
        data15 = (value * gm8 /100)
        rdata15=round((data15 * volume) /(10*value),0)
        print(max(rdata14, rdata15))
            

AmmoniumS = []
Ammonium_sulphate = {'S':24, 'N-NH4':21}
for key, value in Ammonium_sulphate.items():
    if key == 'S':
        data16 = value * gm9 /100
        rdata16=round((data16 * volume) /(10*value),0)
    elif key == 'N-NH4':
        data17 = value * gm9 /100
        rdata17=round((data17 * volume) /(10*value),0)
        print(max(rdata16, rdata17))

Sodium_MolyS = []    
Sodium_Moly = {'Mo':39}
for key, value in Sodium_Moly.items():
    data18 = value * gm10 /100
    rdata18=round((data18 * volume) /(10*value),3)
    print(rdata18)

Mn_chellateS = []    
Mn_chellate = {'Mn':13}
for key, value in Mn_chellate.items():
    data19 = value * gm11 /100
    rdata19=round((data19 * volume) /(10*value),2)
    print(rdata19)


Cu_chellateS = []    
Cu_chellate = {'Cu':14}
for key, value in Cu_chellate.items():
    data20 = value * gm12 /100
    rdata20=round((data20 * volume) /(10*value),2)
    print(rdata20)
    
Zn_chellateS = []    
Zn_chellate = {'Zn':15}
for key, value in Zn_chellate.items():
    data21 = value * gm13 /100
    rdata21=round((data21 * volume) /(10*value),2)
    print(rdata21)

Nitric_acid = {'No3':0.1}
for key, value in Nitric_acid.items():
    if key == 'No3':
        data22 = value * gm14 /100
        rdata22=round((data22 * volume) /(10*value),2)
        print(rdata22)
            
            
Phosphoric_acid = {'P':31.608}
for key, value in Phosphoric_acid.items():
    if key == 'P':
        data23 = value * gm15 /100
        rdata23=round((data23 * volume) /(10*value),2)
        print(rdata23)
##        
##no3 = data2 + data5 + data6 + data17
##ca = data1
##print(no3)
##print(ca)
