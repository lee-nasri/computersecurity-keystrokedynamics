import tkinter
import time
import csv
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#------------------------------ VARIABLE ------------------------------#
start = time.time()
previousKey = ' '
predictionData = []
#------------------------------ VARIABLE ------------------------------#
#------------------------------ CSV ------------------------------#
trainingFile = open('training.csv')
csvreader = csv.reader(trainingFile)
trainingData = []
for row in csvreader:
    trainingData.append([row[0], row[1], float(row[2])])
#------------------------------ CSV ------------------------------#
#------------------------------ GUI ------------------------------#
key_watcher = tkinter.Tk()
key_watcher.title('Keystroke dynamics Biometrics -- Login')
key_watcher.geometry("800x100")

word_repeat_label = tkinter.Label(key_watcher,text="Please type \"emotional themes of longer stories\"")
word_repeat_label.pack()
word_repeat_box = tkinter.Entry(key_watcher)
word_repeat_box.pack()
word_entry_label = tkinter.Label(key_watcher, text="press <Return> after finishing")
word_entry_label.pack()
word_repeat_box.focus()
#------------------------------ GUI ------------------------------#
# pressed() : action if the typing is typing.
def pressed(keyevent):
    global previousKey, start, timescount

    if (keyevent.keysym == 'Return' or keyevent.keysym == 'Tab' ):
        start = time.time()
        previousKey=' '
    else:
        username = "loginuser"
        predictionData.append([username, previousKey + keyevent.char, time.time() - start])
        previousKey = keyevent.char
        start = time.time()

# close window
def close_window():
    key_watcher.destroy()

# if user press return button, this function will predict user's typing behavior.
def press_return(keyevent):
    global predictionData, clf
    word_repeat_box.delete(0, len(word_repeat_box.get()))
    df = pd.DataFrame(predictionData, columns=['subject','key','time'])
    df_avg = avg_dup(df)
    df_pivot = df_avg.pivot(index='subject', columns='key', values = 'time')
    try:
        result = clf.predict(df_pivot[df_pivot.columns[1:]].to_numpy())[0]
        popupwin("You are : " + result)
        predictionData.clear()
    except:
        popupwin("There is some thing wrong. Please try again")
        predictionData.clear()

# training() : train registry typing behavior data with K nearest neightbor
def training():
    global trainingData
    df = pd.DataFrame(trainingData, columns=['subject','key','time'])
    df_avg = avg_dup(df)
    df_pivot = df_avg.pivot(index='subject', columns='key', values = 'time')

    userList = df.subject.unique()
    clf_df = df_pivot
    clf = KNeighborsClassifier(n_neighbors=1)
    clf.fit(clf_df[clf_df.columns[1:]].to_numpy(), userList)
    return clf

# avg_dup average time of duplicate key of each user.
def avg_dup(df):
    df_avg = pd.DataFrame(columns=['subject','key','time'])
    for user in df.subject.unique():
        temp = df[df.subject == user].groupby(['key']).mean()
        temp.insert(0,'subject',[user]*temp.shape[0])
        df_avg = df_avg.append(temp.reset_index())

    return df_avg

# popup window
def popupwin(message):
   top = tkinter.Toplevel(key_watcher)
   top.geometry("400x100")
   label = tkinter.Label(top, text=message)
   label.pack()


clf = training()
#------------------------------ Bind key pressed ------------------------------#
word_repeat_box.bind("<KeyPress>", pressed)
word_repeat_box.bind("<Return>", press_return)
key_watcher.mainloop()
#------------------------------ Bind key pressed ------------------------------#