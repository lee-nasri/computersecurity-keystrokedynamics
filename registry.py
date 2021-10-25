import tkinter
import time
import csv

#------------------------------ VARIABLE ------------------------------#
start = time.time()
previousKey = ' '
#------------------------------ VARIABLE ------------------------------#
#------------------------------ CSV ------------------------------#
trainingFile = open('training.csv', 'a')
writer = csv.writer(trainingFile)
#------------------------------ CSV ------------------------------#
#------------------------------ GUI ------------------------------#
key_watcher = tkinter.Tk()
key_watcher.title('Keystroke dynamics Biometrics -- Register')
key_watcher.geometry("800x100")

word_press_label = tkinter.Label(key_watcher,text="Please fill out the information. Press the <Return> button after it's done.")
word_press_label.pack()
word_entry_label = tkinter.Label(key_watcher, text="Who are you: ")
word_entry_label.pack(side=tkinter.LEFT)
word_entry_box = tkinter.Entry(key_watcher)
word_entry_box.pack(side=tkinter.LEFT)
word_repeat_label = tkinter.Label(key_watcher,text="Please type \"emotional themes of longer stories\" : ")
word_repeat_label.pack(side=tkinter.LEFT)
word_repeat_box = tkinter.Entry(key_watcher)
word_repeat_box.pack(side=tkinter.LEFT)
word_entry_box.focus()
#------------------------------ GUI ------------------------------#

def pressed(keyevent):
    global previousKey, start, timescount

    if (keyevent.keysym == 'Return' or keyevent.keysym == 'Tab' ):
        start = time.time()
        previousKey=' '
    else:
        username = word_entry_box.get()
        writer.writerow([username, previousKey + keyevent.char, time.time() - start])
        previousKey = keyevent.char
        start = time.time()

def press_return(keyevent):
    key_watcher.destroy()


#------------------------------ Bind key pressed ------------------------------#
word_repeat_box.bind("<KeyPress>", pressed)
word_repeat_box.bind("<Return>", press_return)
word_entry_box.bind("<Return>", press_return)
key_watcher.mainloop()
#------------------------------ Bind key pressed ------------------------------#
trainingFile.close()