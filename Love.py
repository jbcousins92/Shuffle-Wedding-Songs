# Shuffle-Wedding-Songs
Shuffles through song titles that were on our wedding CD

from tkinter import *
from random import choice

exps = ["Let It Be Me", "I Can't Help Falling in Love With You", "I Want to Hold Your Hand", "Let's Get It On",
        "Let My Love Open the Door", "You Are the Best Thing", "Crazy Beautiful",
        "And I Love Her", "Wouldn't It Be Nice", "Until the End of Time", "Adorn", "Stay With You",
        "Each Day Gets Better", "We Found Love", "How Can I Tell You"]

root = Tk()
root.title("For My Wife")

lb = Label(root, text="KK")
lb.pack(pady=30)

def express():
    lb["text"] = choice(exps)

Button(root, text="PRESS", command=express).pack(pady=20)
root.geometry("350x250+400+400")

root.mainloop()
