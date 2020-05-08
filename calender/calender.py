from tkinter import *
import calendar


def showCalender():
    new_gui = Tk()

    new_gui.configure(background="white")

    new_gui.title("Calender")

    new_gui.geometry("600x655")

    get_year = int(year_field.get())

    calender_content = calendar.calendar(get_year)

    calender_year = Label(new_gui, text=calender_content, font="Consolas 10 bold")

    calender_year.grid(row=5, column=1, padx=10, pady=10)

    new_gui.mainloop()


if __name__ == "__main__":
    gui = Tk()

    gui.config(background="white")

    gui.title("Calendar")

    gui.geometry("640x280")

    calender = Label(gui, text="Calendar", bg="White", font=("times", 28, 'bold'))

    year = Label(gui, text="Enter Year", bg="white")

    year_field = Entry(gui)

    show = Button(gui, text="Show Calendar", fg="Black", bg="light green", command=showCalender)

    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    calender.grid(row=1, column=3)

    year.grid(row=2, column=2)

    year_field.grid(row=2, column=3, padx=20)

    show.grid(row=4, column=1,padx=20, pady=20)

    Exit.grid(row=6, column=3)

    gui.mainloop()