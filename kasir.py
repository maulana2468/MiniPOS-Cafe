from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import menu


class Kasir:
    def __init__(self, kasir_window):
        kasir_window.title("Kasir")
        kasir_window.geometry("450x580")
        kasir_window.resizable(0, 0)

        def keluar():
            kasir_window.destroy()
            menu.main_menu()

        kasir_window.protocol("WM_DELETE_WINDOW", keluar)

        # menu label
        menu_label = Label(kasir_window, text="Nama Menu")
        menu_label.place(x=60, y=40)
        # harga label
        harga_label = Label(kasir_window, text="Harga Menu")
        harga_label.place(x=60, y=70)
        # qty label
        qty_label = Label(kasir_window, text="QTY")
        qty_label.place(x=60, y=100)
        # menu combobox
        global menu_combobox
        opsi_menu = []
        menu_combobox = ttk.Combobox(kasir_window, value=selected_menu(opsi_menu))
        menu_combobox.place(x=240, y=40)
        # harga field
        global harga_field
        harga_field = Text(kasir_window, width=17, height=1)
        harga_field.place(x=240, y=70)
        harga_field.config(state=DISABLED)
        # qty field
        global qty_field
        qty_field = Text(kasir_window, width=17, height=1)
        qty_field.place(x=240, y=100)
        # tombol list
        add_button = Button(kasir_window,
                            text="Tambah List", height=2, width=45, font='Calibri 10 bold',
                            command=list_button)
        add_button.pack(pady=130)
        # table list
        global table
        table = ttk.Treeview(kasir_window, height=7)
        table["columns"] = ("Nama", "Harga", "QTY", "Subtotal")
        # scrollbar
        vsb = ttk.Scrollbar(kasir_window, orient="vertical", command=table.yview)
        vsb.place(x=370, y=190, height=167)

        table.column("#0", width=0, stretch=NO)
        table.column("Nama", anchor=W, width=90)
        table.column("Harga", anchor=W, width=70)
        table.column("QTY", anchor=W, width=50)
        table.column("Subtotal", anchor=W, width=90)

        table.heading("#0", text="")
        table.heading("Nama", text="Nama", anchor=W)
        table.heading("Harga", text="Harga", anchor=W)
        table.heading("QTY", text="QTY", anchor=W)
        table.heading("Subtotal", text="Subtotal", anchor=W)

        table.place(x=60, y=190)

        # total harga label
        total_harga_label = Label(kasir_window, text="Total Harga")
        total_harga_label.place(x=60, y=380)
        # total harga field
        global total_harga_field
        total_harga_field = Text(kasir_window, width=17, height=1)
        total_harga_field.place(x=240, y=380)
        total_harga_field.config(state=DISABLED)
        # totsl bayar label
        total_bayar_label = Label(kasir_window, text="Total Bayar")
        total_bayar_label.place(x=60, y=410)
        # total bayar field
        global total_bayar_field
        total_bayar_field = Text(kasir_window, width=17, height=1)
        total_bayar_field.place(x=240, y=410)
        # tombol bayar
        tombol_bayar = Button(kasir_window,
                              text="Bayar", height=2, width=19, font='Calibri 10 bold',
                              command=hasil_kembalian)
        tombol_bayar.place(x=240, y=440)
        # kembalian label
        kembalian_label = Label(kasir_window, text="Kembalian")
        kembalian_label.place(x=60, y=500)
        # kembalian field
        global kembalian_field
        kembalian_field = Text(kasir_window, width=17, height=1, state=DISABLED)
        kembalian_field.place(x=240, y=500)

        menu_combobox.bind('<<ComboboxSelected>>', harga_field_upd)


def harga_field_upd(event):
    global target
    target = menu_combobox.get()
    db_connect = mysql_connect()
    cursor = db_connect.cursor()
    sql = "SELECT harga FROM menu_minuman WHERE nama=%s"
    val = (target,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    harga_field.config(state=NORMAL)
    harga_field.delete(1.0, "end")
    harga_field.insert(1.0, result)
    harga_field.config(state=DISABLED)


def hasil_kembalian():
    bayar = total_bayar_field.get("1.0", 'end-1c')
    harga = total_harga_field.get("1.0", 'end-1c')
    kembalian = int(bayar) - int(harga)
    if kembalian < 0:
        messagebox.showwarning(title="Kesalahan", message="Uang Tidak Cukup")
    else:
        kembalian_field.config(state=NORMAL)
        kembalian_field.delete(1.0, "end")
        kembalian_field.insert(1.0, kembalian)
        kembalian_field.config(state=DISABLED)


price = 0


def list_button():
    global price
    harga = harga_field.get("1.0", 'end-1c')
    qty = qty_field.get("1.0", 'end-1c')
    sub = int(harga) * int(qty)

    table.insert(parent='', index='end', values=(target, harga, qty, sub))

    target_price = sub
    price = price + int(target_price)
    total_harga_field.config(state=NORMAL)
    total_harga_field.delete(1.0, "end")
    total_harga_field.insert(1.0, price)
    total_harga_field.config(state=DISABLED)


def selected_menu(opsi_menu):
    db_connect = mysql_connect()
    cursor = db_connect.cursor()
    sql = "SELECT nama FROM menu_minuman"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        opsi_menu.append(data[0])
    return opsi_menu


def mysql_connect():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="database_cafe")
    return db


def main_kasir():
    kasir = Tk()
    kasir.iconbitmap("coffee.ico")
    Kasir(kasir)
    kasir.mainloop()
