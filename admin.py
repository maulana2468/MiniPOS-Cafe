from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import menu
import usermanager


class Admin:
    def __init__(self, admin_window):
        admin_window.title("Admin Menu")
        admin_window.geometry("400x500")
        admin_window.resizable(0, 0)

        def keluar():
            pil = messagebox.askyesno(title="Keluar", message="Keluar dari Menu Admin?")
            if pil:
                admin_window.destroy()
                menu.main_menu()

        admin_window.protocol("WM_DELETE_WINDOW", keluar)

        # tombol insert
        insert_button = Button(admin_window,
                               text="Tambah Data", height=2, width=12,
                               command=insert)
        insert_button.place(x=50, y=275)
        # tombol delete
        delete_button = Button(admin_window,
                               text="Hapus Data", height=2, width=12,
                               command=delete)
        delete_button.place(x=50, y=330)
        # update delete
        update_button = Button(admin_window,
                               text="Update Data", height=2, width=12,
                               command=update)
        update_button.place(x=50, y=385)
        # tombol edit pengguna
        edit_button = Button(admin_window,
                             text="Edit\nAdministrator", height=2, width=12,
                             command=editadmin)
        edit_button.place(x=250, y=275)

        # table
        global table
        table = ttk.Treeview(admin_window)
        table["columns"] = ("ID Menu", "Nama", "Harga")

        # scrollbar
        vsb = ttk.Scrollbar(admin_window, orient="vertical", command=table.yview)
        vsb.place(x=320, y=25, height=227)

        table.column("#0", width=0, stretch=NO)
        table.column("ID Menu", anchor=W, width=90)
        table.column("Nama", anchor=W, width=90)
        table.column("Harga", anchor=W, width=90)

        table.heading("#0", text="")
        table.heading("ID Menu", text="ID Menu", anchor=W)
        table.heading("Nama", text="Nama", anchor=W)
        table.heading("Harga", text="Harga", anchor=W)

        select()


def update_table():
    for i in table.get_children():
        table.delete(i)
    select()


def select():
    db_connect = mysql_connect()
    cursor = db_connect.cursor()
    sql = "SELECT * FROM menu_minuman"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        table.insert(parent='', index='end', values=data)
    table.pack(pady=25)


def insert():
    global id_field, nama_field, harga_field
    insert_window = Toplevel()
    insert_window.geometry("350x200")
    insert_window.iconbitmap("coffee.ico")
    insert_window.title("Tambah Menu")
    # id label
    id_text = Label(insert_window, text="ID Menu:", font='Calibri 10 bold')
    id_text.place(x=30, y=30)
    # nama label
    nama_text = Label(insert_window, text="Nama Menu:", font='Calibri 10 bold')
    nama_text.place(x=30, y=80)
    # harga label
    harga_text = Label(insert_window, text="Harga (Rp):", font='Calibri 10 bold')
    harga_text.place(x=30, y=130)
    # id field
    id_field = Entry(insert_window, width=12)
    id_field.place(x=30, y=50)
    # nama field
    nama_field = Entry(insert_window, width=12)
    nama_field.place(x=30, y=100)
    # harga field
    harga_field = Entry(insert_window, width=12)
    harga_field.place(x=30, y=150)
    # tombol tambah
    add_button = Button(insert_window,
                        text="Tambah", height=2, width=12,
                        command=add_listener)
    add_button.place(x=225, y=75)


def delete():
    global delete_field
    delete_window = Toplevel()
    delete_window.geometry("350x150")
    delete_window.iconbitmap("coffee.ico")
    delete_window.title("Hapus Menu")
    # delete label
    delete_text = Label(delete_window, text="ID Menu yang akan dihapus:", font='Calibri 10 bold')
    delete_text.place(x=30, y=50)
    # delete field
    delete_field = Entry(delete_window, width=12)
    delete_field.place(x=32, y=70)
    # tombol delete
    add_button = Button(delete_window,
                        text="Hapus", height=2, width=12,
                        command=del_listener)
    add_button.place(x=215, y=50)


def update():
    global id_field_upd, nama_field_upd, harga_field_upd
    update_window = Toplevel()
    update_window.geometry("350x200")
    update_window.iconbitmap("coffee.ico")
    update_window.title("Update Menu")
    # id label
    id_text = Label(update_window, text="ID Menu yang diupdate:", font='Calibri 10 bold')
    id_text.place(x=30, y=30)
    # nama label
    nama_text = Label(update_window, text="Nama Menu:", font='Calibri 10 bold')
    nama_text.place(x=30, y=80)
    # harga label
    harga_text = Label(update_window, text="Harga (Rp):", font='Calibri 10 bold')
    harga_text.place(x=30, y=130)
    # id field
    id_field_upd = Entry(update_window, width=12)
    id_field_upd.place(x=30, y=50)
    # nama field
    nama_field_upd = Entry(update_window, width=12)
    nama_field_upd.place(x=30, y=100)
    # harga field
    harga_field_upd = Entry(update_window, width=12)
    harga_field_upd.place(x=30, y=150)
    # tombol tambah
    upd_button = Button(update_window,
                        text="Update", height=2, width=12,
                        command=upd_listener)
    upd_button.place(x=225, y=75)


def add_listener():
    try:
        db_connect = mysql_connect()
        cursor = db_connect.cursor()
        id = id_field.get()
        nama = nama_field.get()
        harga = harga_field.get()
        sql = "INSERT INTO menu_minuman VALUES (%s, %s, %s)"
        val = (id, nama, harga)
        cursor.execute(sql, val)
        db_connect.commit()
        update_table()
        messagebox.showinfo(title="Sukses", message="Menu Berhasil Ditambah!")
    except Exception as e:
        messagebox.showerror(title="Kesalahan", message="Terjadi Kesalahan:\n\n" + str(e))


def del_listener():
    try:
        db_connect = mysql_connect()
        cursor = db_connect.cursor()
        id = delete_field.get()
        sql = "DELETE FROM menu_minuman WHERE id_menu=%s"
        val = (id,)
        cursor.execute(sql, val)
        db_connect.commit()
        update_table()
        messagebox.showinfo(title="Sukses", message="Menu Berhasil Dihapus!")
    except:
        messagebox.showerror(title="Kesalahan", message="Terjadi Kesalahan")


def upd_listener():
    try:
        db_connect = mysql_connect()
        cursor = db_connect.cursor()
        id = id_field_upd.get()
        nama = nama_field_upd.get()
        harga = harga_field_upd.get()
        sql = "UPDATE menu_minuman SET nama=%s, harga=%s WHERE id_menu=%s"
        val = (nama, harga, id)
        cursor.execute(sql, val)
        db_connect.commit()
        update_table()
        messagebox.showinfo(title="Sukses", message="Menu Berhasil Diupdate!")
    except Exception as e:
        messagebox.showerror(title="Kesalahan", message="Terjadi Kesalahan:\n\n" + str(e))


def editadmin():
    edit_admin = Toplevel()
    edit_admin.geometry("350x350")
    edit_admin.iconbitmap("coffee.ico")
    edit_admin.title("Edit Administrator")
    global usn_lama_text, passwd_lama_text, usn_baru_text, passwd_baru_text
    # usnlamalabel
    usn_lama_label = Label(edit_admin, text="Nama Pengguna Lama:", font='Calibri 10 bold')
    usn_lama_label.place(x=50, y=50)
    # usnlamatext
    usn_lama_text = Entry(edit_admin, width=16)
    usn_lama_text.place(x=50, y=70)
    # passwdlamalabel
    passwd_lama_label = Label(edit_admin, text="Kata Sandi Lama:", font='Calibri 10 bold')
    passwd_lama_label.place(x=50, y=110)
    # passwdlamatext
    passwd_lama_text = Entry(edit_admin, show="*", width=16)
    passwd_lama_text.place(x=50, y=130)

    # usnbarulabel
    usn_baru_label = Label(edit_admin, text="Nama Pengguna Baru:", font='Calibri 10 bold')
    usn_baru_label.place(x=50, y=170)
    # usnbarutext
    usn_baru_text = Entry(edit_admin, width=16)
    usn_baru_text.place(x=50, y=190)
    # passwdbarulabel
    passwd_baru_label = Label(edit_admin, text="Kata Sandi Baru:", font='Calibri 10 bold')
    passwd_baru_label.place(x=50, y=230)
    # passwdbarutext
    passwd_baru_text = Entry(edit_admin, show="*", width=16)
    passwd_baru_text.place(x=50, y=250)

    # button
    edit_admin_button = Button(edit_admin,
                               text="Edit", height=2, width=12,
                               command=edit_admin_listener)
    edit_admin_button.place(x=210, y=140)


def edit_admin_listener():
    usnlama = usn_lama_text.get()
    pswdlama = passwd_lama_text.get()
    if usnlama != usermanager.usn_admin or pswdlama != usermanager.passwd_admin:
        messagebox.showerror(title="Kesalahan", message="Nama Pengguna/Kata Sandi Lama Salah")
    else:
        usermanager.usn_admin = usn_baru_text.get()
        usermanager.passwd_admin = passwd_baru_text.get()
        messagebox.showinfo(title="Sukses",
                            message="Nama Pengguna/Kata Sandi Berhasil Diganti\n\nKeluar Dari Menu Admin")
        admin.destroy()
        menu.main_menu()


def mysql_connect():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="database_cafe")
    return db


def main_admin():
    global admin
    admin = Tk()
    admin.iconbitmap("coffee.ico")
    mysql_connect()
    Admin(admin)
    admin.mainloop()
