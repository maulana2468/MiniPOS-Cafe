from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

import admin
import kasir
import usermanager as usmgr


class FirstWindow:
    def __init__(self, main_window):
        main_window.title("Cafe POS Menu")
        main_window.geometry("300x370")
        main_window.resizable(0, 0)

        def keluar():
            msgbox = messagebox.askyesno(title="Keluar", message="Keluar Aplikasi?")
            if msgbox:
                root.destroy()

        main_window.protocol("WM_DELETE_WINDOW", keluar)

        # judul
        title_label = Label(main_window, text="Maul Cafe", font=Font(size=20))
        title_label.pack(pady=50)
        # tombol admin
        admin_button = Button(main_window,
                              text="Admin Menu", height=2, width=12,
                              command=pass_window, font='Calibri 12')
        admin_button.pack(pady=10)
        # tombol kasir
        kasir_button = Button(main_window,
                              text="Kasir Menu", height=2, width=12,
                              command=buka_kasir, font='Calibri 12')
        kasir_button.pack(pady=10)


def buka_kasir():
    root.destroy()
    kasir.main_kasir()


def pass_window():
    global usn, pswd, pass_wndw
    pass_wndw = Toplevel()
    ##pass_wndw.iconbitmap("coffee.ico")
    pass_wndw.title("Login")
    pass_wndw.geometry("400x160")

    # tombol login
    login_window = Button(pass_wndw,
                          text="Masuk", height=2, width=12,
                          command=check_usn_pswd)
    login_window.place(x=250, y=53)
    # login text
    usn_text = Label(pass_wndw, text="Nama Pengguna:", font='Calibri 12')
    usn_text.place(x=52, y=20)
    # login field
    usn = Entry(pass_wndw, width=16)
    usn.place(x=55, y=45)
    # pass text
    pswd_text = Label(pass_wndw, text="Kata Sandi:", font='Calibri 12')
    pswd_text.place(x=52, y=80)
    # pass field
    pswd = Entry(pass_wndw, show="*", width=16)
    pswd.place(x=55, y=105)


def check_usn_pswd():
    global check_window
    if usn.get() == usmgr.usn_admin and pswd.get() == usmgr.passwd_admin:
        messagebox.showinfo(message="Login Sukses!")
        pass_wndw.destroy()
        root.destroy()
        admin.main_admin()
    else:
        messagebox.showwarning(message="Nama Pengguna atau Kata Sandi Salah!")


def main_menu():
    global root
    root = Tk()
    ##root.iconbitmap("coffee.ico")
    FirstWindow(root)
    root.mainloop()
