
# importing whole module 
from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to 
# retrieve system's time 
from time import strftime 
import time
# creating tkinter window 
root = Tk() 
root.title('Trainer')
root.minsize(width=225, height = 70)
root.configure(background='green4')
root.wm_attributes("-topmost", 1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('240x94+' + str(screen_width - 450) + '+150')
# This function is used to  
# display time on the label

counter = 0
run_id = None
def start(lbl, btn):
    global counter
    global run_id
    global root
    root['background'] = 'green4'
    lbl['background'] = 'green4'
    lbl['foreground'] = 'white'
    if run_id:
        lbl.after_cancel(run_id)
        run_id = None
        
    counter = 0
    def count():
        global counter
        global run_id
        global root
        display = time.strftime('%H:%M:%S', time.gmtime(counter))
        lbl['text']=display
        
        if counter>600:
            root['background'] = 'red3'
            lbl['background'] = 'red3'
            lbl['foreground'] = 'white'
        elif counter > 480:
            root['background'] = 'yellow'
            lbl['background'] = 'yellow'
            lbl['foreground'] = 'black'
        run_id = lbl.after(1000, count)  
        counter += 1
        
    btn['text'] = 'Restart'
    count()

# Styling the label widget so that clock 
# will look more attractive 
counter_label = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'green4', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
counter_label.pack(anchor = 'center')
counter_label['text'] = 'Welcome!!'

start_button = Button(root, text = 'Start',
             command = lambda: start(counter_label, start_button))
start_button.pack()

mainloop() 
