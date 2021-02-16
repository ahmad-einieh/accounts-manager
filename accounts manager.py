from tkinter import*
import tkinter.messagebox as tmsg
import csv
import webbrowser
#############################
root = Tk()
root.geometry("900x450")
root.resizable(0, 0)
root.title("Accounts Manager")
root.configure(background="yellow")
################################

'''

by: ahmad eineih

'''


def submit():
    with open("one.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([websitename.get(), username.get(), passValue.get(
        ), emailValue.get(), phoneValue.get(), info.get()])


def about():
    tmsg.showinfo(
        "About me", "my name is ahmad, I am form syria, You can communicate with me on abomoaz3375@gmail.com")


def mygithub():
    webbrowser.open_new(r"https://github.com/ahmad-prog")


def mypaypal():
    webbrowser.open_new(r"https://paypal.me/progahmad?locale.x=ar_EG")


##########################
'''
try:
    file = open("one.csv")
    reader = csv.reader(file)
    lines = len(list(reader))
    if lines >= 1:
        pass
    else:
        with open("one.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(['website_name', 'username', 'password',
                             'email', 'phone', 'more_inforamtion'])
except:
    print("error")

'''
##############################


# labelling the main components
Label(root,  text="    you can fill your information and save it:) ",
      font="lucida 20 bold", pady=10, background="yellow").grid(row=0, column=3, sticky='EW')
Label(root, font="lucida 20 bold", pady=10, background="yellow").grid(
    row=0, column=4, sticky='EW')
#################################
Label(root, background="yellow").grid(row=1, column=3)
Label(root, text="you must enter your colum name in first time: ",
      background="yellow").grid(row=1, column=4)
############################
Label(root, background="yellow").grid(row=2, column=3)
Label(root, background="yellow").grid(row=2, column=4)
############################
Label(root, text="Website name\t \t -",
      font="lucida 15 bold", padx=10, background="yellow").grid(row=3, column=3)
Label(root, text="Username\t \t -", font="lucida 15 bold",
      padx=10, background="yellow").grid(row=4, column=3)
Label(root, text="Password\t \t -", font="lucida 15 bold",
      background="yellow").grid(row=5, column=3)
Label(root, text="E-mail address\t \t -",
      font="lucida 15 bold", padx=10, background="yellow").grid(row=6, column=3)
Label(root, text="Phone number\t \t -",
      font="lucida 15 bold", padx=10, background="yellow").grid(row=7, column=3)
Label(root, text="more informations\t \t -",
      font="lucida 15 bold", padx=10, background="yellow").grid(row=8, column=3)

# creating some variable values

username = StringVar()
passValue = StringVar()
emailValue = StringVar()
phoneValue = StringVar()
info = StringVar()
websitename = StringVar()

# creating entry widgets

Entry(root, textvariable=websitename, width=45).grid(row=3, column=4)
Entry(root, textvariable=username, width=45).grid(row=4, column=4)
Entry(root, textvariable=passValue, width=45, show="*").grid(row=5, column=4)
Entry(root, textvariable=emailValue, width=45).grid(row=6, column=4)
Entry(root, textvariable=phoneValue, width=45).grid(row=7, column=4)
Entry(root, textvariable=info, width=45).grid(row=8, column=4)

# creating buttons for submission data
Label(root, background="yellow").grid(row=9, column=4)
Button(root, text="Submit", command=submit, width=7,
       font='sans 16 bold', background="gray").grid(row=10, column=4)

#####################
Label(root, background="yellow").grid(row=11, column=3)
Label(root, background="yellow").grid(row=11, column=4)
####################
photo = PhotoImage(file="paypal1.png")
Button(root, image=photo, command=mypaypal,
       background="gray").grid(row=12, column=3)
#################
photo1 = PhotoImage(file="github-logo.png")
Button(root, image=photo1, command=mygithub,
       background="gray").grid(row=12, column=4)
#################

# creating menu

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="about me", command=about)
m1.add_command(label="MyGitHub", command=mygithub)
m1.add_command(label="MyPaypal", command=mypaypal)
m1.add_separator()
m1.add_command(label="Exit", command=exit)
mainmenu.add_cascade(label="MORE", menu=m1)
root.config(menu=mainmenu)

root.mainloop()
