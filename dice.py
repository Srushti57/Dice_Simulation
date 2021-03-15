import  tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.title('Dice Simulator')
root.configure(bg='pink3')

label = tkinter.Label(root, text='', font=('Helvetica', 260))

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}', bg='rosybrown4')
    label.pack()

btn = tkinter.Button(root, text='roll dice', command=roll , font=('',30), bg='rosybrown1')
btn.pack()



root.mainloop()
