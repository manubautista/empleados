import tkinter as tk
import sqlite3
from tkinter import messagebox
root = tk.Tk()
root.title('Empleados CRUD')
# root.iconbitmap('C:/Users/manub/PycharmProjects/pythonProject/Conocimientos/Tk/icon1.ico')
# ------------------------- FUNCIONES ----------------------------


def conectar():
    bdempleados = sqlite3.connect("EMPLEADOS")
    cursor = bdempleados.cursor()
    try:
        cursor.execute('''
            CREATE TABLE EMPLEADOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(20),
            DNI INTEGER(8) UNIQUE,
            SUELDO INTEGER(10))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito.")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe.")


def salir():
    valor = messagebox.askquestion('¿Salir?', '¿Desea salir de la aplicación?')
    if valor == 'yes':
        root.destroy()


def limpiar():
    miNombre.set('')
    miID.set('')
    miApellido.set('')
    miSueldo.set('')
    miDNI.set('')


def crear():
    bdempleados = sqlite3.connect('EMPLEADOS')
    cursor = bdempleados.cursor()
    datos = miNombre.get(), miApellido.get(), miDNI.get(), miSueldo.get()
    try:
        cursor.execute("INSERT INTO EMPLEADOS VALUES(NULL,?,?,?,?)", datos)
        """cursor.execute("INSERT INTO EMPLEADOS VALUES(NULL, '" + miNombre.get() + "','" + miApellido.get() +
                   "','" + miDNI.get() + "','" + miSueldo.get() + "')")"""
        bdempleados.commit()
        cursor.execute("SELECT * FROM EMPLEADOS ORDER BY ID DESC LIMIT 1")
        nuevo = cursor.fetchall()
        for a in nuevo:
            showid = a[0]
            showname = a[1]
        messagebox.showinfo('BBDD', f'Empleado {showname} insertado en base de datos bajo ID {showid}.')
    except:
        messagebox.showwarning('BBDD', 'Empleado con ese DNI ya existente.')


def leer():
    bdempleados = sqlite3.connect('EMPLEADOS')
    cursor = bdempleados.cursor()
    try:
        cursor.execute("SELECT * FROM EMPLEADOS WHERE ID=" + miID.get())
        elusuario = cursor.fetchall()
        for u in elusuario:
            miID.set(u[0])
            miNombre.set(u[1])
            miApellido.set(u[2])
            miDNI.set(u[3])
            miSueldo.set(u[4])
        bdempleados.commit()
    except:
        messagebox.showwarning('BBDD', 'Empleado no registrado bajo esa ID.')

def actualizar():
    bdempleados = sqlite3.connect('EMPLEADOS')
    cursor = bdempleados.cursor()
    datos = miNombre.get(), miApellido.get(), miDNI.get(), miSueldo.get()
    try:
        cursor.execute("UPDATE EMPLEADOS SET NOMBRE =?, APELLIDO=?, DNI=?, SUELDO=?" +
                       "WHERE ID=" + miID.get(), datos)
        """cursor.execute("UPDATE EMPLEADOS SET NOMBRE='" + miNombre.get() +
                       "', APELLIDO='" + miApellido.get() +
                       "', DNI='" + miDNI.get() +
                       "', SUELDO='" + miSueldo.get() +
                       "' WHERE ID=" + miID.get())"""
        bdempleados.commit()
        messagebox.showinfo('BBDD', 'Registro actualizado con éxito.')
    except:
        messagebox.showwarning('BBDD', 'Ha ocurrido un error compruebe los datos.')


def eliminar():
    bdempleados = sqlite3.connect('EMPLEADOS')
    cursor = bdempleados.cursor()
    try:
        cursor.execute("DELETE FROM EMPLEADOS WHERE ID=" + miID.get())
        bdempleados.commit()
        messagebox.showinfo('BBDD', 'Empleado eliminado con éxito.')
    except:
        messagebox.showwarning('BBDD', 'ID de empleado no encontrada.')

# def crearempleado():
    # cursor = bdempleados.cursor()
    # cursor.execute(f"INSERT INTO EMPLEADOS VALUES('{ID}, {nombre}, {DNI}, {sueldo}')")
    # bdempleados.commit()
# ----------------------MENÚ --------------------


barra = tk.Menu(root)
root.config(menu=barra, width=300, height=300)

bbddMenu = tk.Menu(barra, tearoff=0)
bbddMenu.add_command(label='Conectar', command=conectar)
bbddMenu.add_command(label='Salir', command=salir)

ClearMenu = tk.Menu(barra, tearoff=0)
ClearMenu.add_command(label='Casilleros', command=limpiar)

crudMenu = tk.Menu(barra, tearoff=0)
crudMenu.add_command(label='Create', command=crear)
crudMenu.add_command(label='Read', command=leer)
crudMenu.add_command(label='Update', command=actualizar)
crudMenu.add_command(label='Delete', command=eliminar)

barra.add_cascade(label='BBDD', menu=bbddMenu)
barra.add_cascade(label='Limpiar', menu=ClearMenu)
barra.add_cascade(label='CRUD', menu=crudMenu)

# ------------------------- ENTRYS ----------------------

FrameEntrys = tk.Frame(root)
FrameEntrys.pack()

miID = tk.StringVar()
miNombre = tk.StringVar()
miApellido = tk.StringVar()
miDNI = tk.StringVar()
miSueldo = tk.StringVar()

# ----tkinter Entry ID-----

ID = tk.Entry(FrameEntrys, textvariable=miID)
IDtexto = tk.Label(FrameEntrys, text='ID: ')

ID.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
IDtexto.grid(row=0, column=0, padx=10, pady=10)

# ----tkinter Entry Nombre-----

nombre = tk.Entry(FrameEntrys, textvariable=miNombre)
nombretexto = tk.Label(FrameEntrys, text='Nombre: ')

nombre.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
nombretexto.grid(row=1, column=0, padx=10, pady=10)

# ----tkinter Entry Apellido-----

apellido = tk.Entry(FrameEntrys, textvariable=miApellido)
apellidotexto = tk.Label(FrameEntrys, text='Apellido: ')

apellido.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
apellidotexto.grid(row=2, column=0, padx=10, pady=10)

# ----tkinter Entry DNI-----

DNI = tk.Entry(FrameEntrys, textvariable=miDNI)
DNItexto = tk.Label(FrameEntrys, text='DNI: ')

DNI.grid(row=3, column=1, padx=10, pady=10)
DNItexto.grid(row=3, column=0, padx=10, pady=10)

# ----tkinter Entry Sueldo-----

sueldo = tk.Entry(FrameEntrys, textvariable=miSueldo)
sueldotexto = tk.Label(FrameEntrys, text='Sueldo: ')

sueldo.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
sueldotexto.grid(row=4, column=0, padx=10, pady=10)

# -------------------- BOTONES ------------------

FrameBotones = tk.Frame(root)
FrameBotones.pack()

crear = tk.Button(FrameBotones, text='Crear', command=crear)
crear.grid(row=0, column=0, padx=10, pady=10)

leer = tk.Button(FrameBotones, text='Leer', command=leer)
leer.grid(row=0, column=1, padx=10, pady=10)

actualizar = tk.Button(FrameBotones, text='Actualizar', command=actualizar)
actualizar.grid(row=0, column=2, padx=10, pady=10)

borrar = tk.Button(FrameBotones, text='Borrar', command=eliminar)
borrar.grid(row=0, column=3, padx=10, pady=10)


root.mainloop()
