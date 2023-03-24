from PIL import ImageTk, Image
from tkinter import *

root = Tk()
root.geometry("600x400")
root.configure(bg="olive drab")

# dice = ImageTk.PhotoImage(Image.open ( "dice.png"))

lblTitle = Label(root, text="Akshay's Roll the Dice Game", bg="olive drab", fg="snow", font=("Curlz MT", 19, "bold", "italic")).place(relx=0.5,rely=0.075,anchor=CENTER)

lblPlayer1 = Label(root, text="Player 1", bg="dark olive green", fg="snow").place(relx=0.2,rely=0.2,anchor=CENTER)

lblPlayer2 = Label(root, text="Player 2", bg="dark olive green", fg="snow").place(relx=0.8,rely=0.2,anchor=CENTER)

lblScoreP1 = Label(root, bg="olive drab").place(relx=0.2,rely=0.4,anchor=CENTER)

lblScoreP2 = Label(root, bg="olive drab").place(relx=0.8,rely=0.4,anchor=CENTER)

lblRoll = Label(root, bg="olive drab").place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()