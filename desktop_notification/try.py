from tkinter  import * 
import time 
import sys 
root= Tk()
root.titel('Notification')
label= Label(root, text='ALeart!', fg='Red', font="Arial").pack()
label2= Label(root, text='Take a break  ' , fg='Red', font="Arial").pack()
btn= Button(root, text='exit ' , command=sys.exit()).pack()

time.sleep(3600)


root.mainloop()