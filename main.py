from tkinter import *
import random
import mysql.connector as mysql

from turtle import turtle
from reflex import reflex

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")
p1 = PhotoImage(file='./assets/game.png')
consolewindow.iconphoto(False, p1)

connectr = mysql.connect(host="localhost", passwd="admin", user="root")
cursor = connectr.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS VVLCDATABASE")
cursor.execute("USE VVLCDATABASE")
cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERINFO (NAME VARCHAR(30), USERNAME VARCHAR(30), PASSWORD VARCHAR(30), TURTLEWINS LIST, REFLEXSCORE INT)")


def loginer(text=None):
    global over
    loginwindow = Toplevel(consolewindow)
    loginwindow.geometry("300x400")
    uname_var = StringVar()
    passw_var = StringVar()

    spassw_var = StringVar()
    suname_var = StringVar()
    sname_var = StringVar()

    def signinfn():
        global over

        profilelist = cursor.execute("FETCHALL")

        username = uname_var.get()
        password = passw_var.get()

        print("The name is : " + username)
        print("The password is : " + password)

        uname_var.set("")
        passw_var.set("")

        if username in lst and password correct:
            over = username
            loginwindow.quit()
            loginwindow.destroy()

    def signupfn():
        global over

        name = sname_var.get()
        username = suname_var.get()
        password = spassw_var.get()

        print("The name is : " + username)
        print("The password is : " + password)

        suname_var.set("")
        spassw_var.set("")
        sname_var.set("")

        if username not in lst:
            insert profile
            over = username
            loginwindow.quit()
            loginwindow.destroy()


    txtlabel = Label(loginwindow, text=text, justify="center", font=('calibre', 20, 'bold'))
    txtlabel2 = Label(loginwindow, text="Signin", justify="center", font=('calibre', 20, 'bold'))
    txtlabel3 = Label(loginwindow, text="(OR)", justify="center", font=('calibre', 20, 'bold'))
    txtlabel4 = Label(loginwindow, text="Signup", justify="center", font=('calibre', 20, 'bold'))

    uname_label = Label(loginwindow, text='Username')
    uname_entry = Entry(loginwindow, textvariable=uname_var)
    uname_label2 = Label(loginwindow, text='Username')
    uname_entry2 = Entry(loginwindow, textvariable=suname_var)

    name_label = Label(loginwindow, text='Username')
    name_entry = Entry(loginwindow, textvariable=sname_var)

    passw_label = Label(loginwindow, text='Password')
    passw_entry = Entry(loginwindow, textvariable=passw_var, show='*')
    passw_label2 = Label(loginwindow, text='Password')
    passw_entry2 = Entry(loginwindow, textvariable=spassw_var, show='*')

    signin = Button(loginwindow, text="Signin", command=signinfn)
    signup = Button(loginwindow, text="Signin", command=signupfn)

    txtlabel.pack()
    txtlabel2.pack()
    uname_label.pack()
    uname_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    signin.pack()

    txtlabel3.pack()
    txtlabel4.pack()
    uname_label2.pack()
    uname_entry2.pack()
    name_label.pack()
    name_entry.pack()
    passw_label2.pack()
    passw_entry2.pack()
    signup.pack()
    loginwindow.mainloop()
    return over

def turtlegame():
    player1 = loginer(text="Player 1")
    player2 = loginer(text="Player 2")
    turtle.game(player1, player2, consolewindow)

def reflexgame():
    player = loginer(text="Singleplayer")
    reflex.game(1231, consolewindow)

def randomgame():
    randgame = random.choice(["turtle", "reflex"])
    if randgame == "turtle":
        turtlegame()
    elif randgame == "reflex":
        reflexgame()

def exitwindow():
    consolewindow.quit()
    consolewindow.destroy()

def credits():
    window = Toplevel(consolewindow)
    window.geometry("300x300")
    p1 = PhotoImage(file='./assets/game.png')
    window.iconphoto(False, p1)
    window.title("VVLC Creators")
    label1 = Label(window, text="Creators of VVLC", justify="center", font=('calibre', 20, 'bold'))
    label2 = Label(window, text="Vignesh.T.A\nRollno:- 29\n\nV.Viswesh Kissan\nRollno:- 28\n\nV.Lathish\nRollno:- 27\n\nK.Charan\nRollno:- 22")
    label1.pack()
    label2.pack()

def leaderboard():
    window = Toplevel(consolewindow)
    window.geometry("300x500")
    p1 = PhotoImage(file='./assets/trophy.png')
    window.iconphoto(False, p1)
    window.title("VVLC Leaderboard")
    label3 = Label(window, text="Leaderboard", justify="center", font=('calibre', 20, 'bold'))
    label3.pack()
    label4 = Label(window, text="Name       Username        Reflex Score        Turtle Wins")
    label4.pack()
    fetchdatabase
    for i in data:
        label5 = Label(window, text=f"{name}       {Username}        {Reflex Score}        {Turtle Wins}")
        label5.pack()

def documentation():
    window = Toplevel(consolewindow)
    window.geometry("300x600")
    p1 = PhotoImage(file='./assets/documentation.png')
    window.iconphoto(False, p1)
    window.title("VVLC Documentation")
    f = open("documentation.txt")
    fdata = f.read()
    f.close()
    label1 = Label(window, text="Documentation")
    label2 = Label(window, text=fdata)
    label1.pack()
    label2.pack()


turtlebtn = Button(consolewindow, text="Play Turtle Race", command=turtlegame)
turtlebtn.pack()
wcfbtn = Button(consolewindow, text="Play WCF", command=reflexgame)
wcfbtn.pack()
randbtn = Button(consolewindow, text="Random Game", command=randomgame)
randbtn.pack()
creditsbtn = Button(consolewindow, text="Leaderboard", command=leaderboard)
creditsbtn.pack()
leaderboardbtn = Button(consolewindow, text="Credits", command=credits)
leaderboardbtn.pack()
documentationbtn = Button(consolewindow, text="Documentation", command=documentation)
documentationbtn.pack()
exitbtn = Button(consolewindow, text="Exit", command=exitwindow)
exitbtn.pack()

consolewindow.mainloop()
