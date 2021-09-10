# Odd or Even GUI App - Check if the number inputed by the user is Odd or Even
from tkinter import *
from tkinter import messagebox

# GUI Codes for:
# GUI Labels
window = Tk()
mainlabel = Label(window, text="Odd or Even App", font=("Optima", 31))
mainlabel.pack(pady = 10)
subLabel = Label(window, text="Input any number of your choosing", fg="silver", font=("Optima",18, "italic"))
subLabel.pack()
# GUI text entry
numberEntry = Entry(window, textvariable="Enter number here", bg="white", fg="black") # Ask the user
numberEntry.pack(pady=5)

# function button!
def oddEven():
    numberInput = numberEntry.get() # Fetch user input
    # Pseudocode:
    # if user input is not a number / integer throw an error msg..
    # if user input is valid then:
    # divide the number by 2 and take it's modulo, if modulo / remainder is equals to 0 (Even!)
    # Otherwise (Odd!): because a modulo / remainder more than 1 mo result siya to Odd
    if not (numberInput.isnumeric()): # error trap if input is not a number = Invalid
        messagebox.showwarning("Error", "Invalid input!")
    elif (int(numberInput) % 2) == 0:
        messagebox.showinfo("Information", "Even Number")
    else:
        messagebox.showinfo("Information", "Odd Number")
# GUI button
btn1 = Button(window, text="Check", fg="white", font=("Optima",18), command=oddEven)
btn1.pack(pady = 10)

# GUI title & size
window.title("GUI")
window.geometry("350x250")
# Run the APP
window.mainloop()

# credits to docs.python.org // tkinter module documentation