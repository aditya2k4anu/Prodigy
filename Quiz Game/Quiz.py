from tkinter import *
from tkinter import ttk
c = 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
jack = ttk.Frame(a)


def quiz(c):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")

    Label(frame1, text="Who designed the National Flag of India?", font=(
        "Arial", 20, "bold"), foreground="red").grid(row=2, column=2)
    Button(frame1, text="Rabindra Nath Tagore", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=a_wrong).grid(row=3, column=1)
    Button(frame1, text="Pingalli Venkayya", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=a_correct).grid(row=3, column=2)
    Button(frame1, text="Suman Chandra", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=a_wrong).grid(row=3, column=3)

    Label(frame2, text="Name the National Reptile of India?", font=(
        "Arial", 20, "bold"), foreground="red").grid(row=2, column=2)
    Button(frame2, text="King cobra", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=b_correct).grid(row=3, column=1)
    Button(frame2, text="Anaconda", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=b_wrong).grid(row=3, column=2)
    Button(frame2, text="Black Mamba", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=b_wrong).grid(row=3, column=3)

    Label(frame3, text="Name the largest mammal?", font=(
        "Arial", 20, "bold"), foreground="red").grid(row=2, column=2)
    Button(frame3, text="Elephant", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=c_wrong).grid(row=3, column=1)
    Button(frame3, text="Blue Whale", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=c_correct).grid(row=3, column=2)
    Button(frame3, text="Dolphin", font=("Arial", 15, "bold"), background="yellow",
           foreground="red", command=c_wrong).grid(row=3, column=3)

    Label(frame4, text="Name the largest planet of our Solar System?",
          font=("Arial", 20, "bold"), foreground="red").grid(row=2, column=2)
    Button(frame4, text="Saturn", font=("Arial", 15, "bold"), background="yellow",
           foreground="red", command=d_wrong).grid(row=3, column=1)
    Button(frame4, text="pluto", font=("Arial", 15, "bold"), background="yellow",
           foreground="red", command=d_wrong).grid(row=3, column=2)
    Button(frame4, text="Jupiter", font=("Arial", 15, "bold"), background="yellow",
           foreground="red", command=d_correct).grid(row=3, column=3)

    Label(frame5, text="How many years are there in one Millenium?", font=(
        "Arial", 20, "bold"), foreground="red").grid(row=2, column=2)
    Button(frame5, text="10200 years", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=e_wrong).grid(row=3, column=1)
    Button(frame5, text="1000 years", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=e_correct).grid(row=3, column=2)
    Button(frame5, text="2500 years", font=("Arial", 15, "bold"),
           background="yellow", foreground="red", command=e_wrong).grid(row=3, column=3)


def a_correct():
    Label(frame1, text="correct", font=("Arial", 30, "bold"),
          background="green", foreground="white").grid(row=4, column=2)
    Label(frame1, text="Marks Obtained: 1", font=("Arial", 20, "bold"), foreground="Purple").grid(row=1, column=3)


def a_wrong():
    Label(frame1, text="Incorrect", font=("Arial", 30, "bold"),
          background="red", foreground="white").grid(row=4, column=2)
    Label(frame1, text="Marks Obtained: 0", font=("Arial", 20, "bold")
          , foreground="purple").grid(row=1, column=3)


def b_correct():
    Label(frame2, text="correct", font=("Arial", 30, "bold"),
          background="green", foreground="white").grid(row=4, column=2)
    Label(frame2, text="Marks Obtained: 1", font=("Arial", 20, "bold"), foreground="Purple").grid(row=1, column=3)


def b_wrong():
    Label(frame2, text="Incorrect", font=("Arial", 30, "bold"),
          background="red", foreground="white").grid(row=4, column=2)
    Label(frame2, text="Marks Obtained: 0", font=("Arial", 20, "bold"), foreground="purple").grid(row=1, column=3)


def c_correct():
    Label(frame3, text="correct", font=("Arial", 30, "bold"),
          background="green", foreground="white").grid(row=4, column=2)
    Label(frame3, text="Marks Obtained: 1", font=("Arial", 20, "bold"),
           foreground="Purple").grid(row=1, column=3)


def c_wrong():
    Label(frame3, text="Incorrect", font=("Arial", 30, "bold"),
          background="red", foreground="white").grid(row=4, column=2)
    Label(frame3, text="Marks Obtained: 0", font=("Arial", 20, "bold"),
           foreground="purple").grid(row=1, column=3)


def d_correct():
    Label(frame4, text="correct", font=("Arial", 30, "bold"),
          background="green", foreground="white").grid(row=4, column=2)
    Label(frame4, text="Marks Obtained: 1", font=("Arial", 20, "bold"),
           foreground="Purple").grid(row=1, column=3)


def d_wrong():
    Label(frame4, text="Incorrect", font=("Arial", 30, "bold"),
          background="red", foreground="white").grid(row=4, column=2)
    Label(frame4, text="Marks Obtained: 0", font=("Arial", 20, "bold"),
           foreground="purple").grid(row=1, column=3)


def e_correct():
    Label(frame5, text="correct", font=("Arial", 30, "bold"),
          background="green", foreground="white").grid(row=4, column=2)
    Label(frame5, text="Marks Obtained: 1", font=("Arial", 20, "bold"),
           foreground="Purple").grid(row=1, column=3)


def e_wrong():
    Label(frame5, text="Incorrect", font=("Arial", 30, "bold"),
          background="red", foreground="white").grid(row=4, column=2)
    Label(frame5, text="Marks Obtained: 0", font=("Arial", 20, "bold"),
           foreground="purple").grid(row=1, column=3)


quiz(c)
a.pack()
a.mainloop()
