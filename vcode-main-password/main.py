import tkinter as tk
from tkinter import Menu
import string
import secrets
from tkinter import PhotoImage

mostrar_contraseñas = 0

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Password Generator by Vocadev")
ventana.geometry("400x200")

'''ventana.configure(bg="blue")'''


icono = "bb-img.png"  
ventana.iconbitmap(default = icono)

marco = tk.Frame(ventana, width=400, height=200)
marco.anchor
marco.place(x = 500, y = 500)

color_de_fondo = "lightblue"  # Reemplaza con el color que desees
ventana.configure(bg=color_de_fondo)


# Funciones para las opciones del menú
def abrir_archivo():
    print("Abrir archivo")

def guardar_archivo():
    print("Guardar archivo")

def salir():
    ventana.quit()

def guardar_texto():
    pagina_web = entrada_texto.get()
    contrasena_generada = generar_contrasena()
    with open("nombres.txt", "a") as archivo:
        archivo.write(f"{pagina_web}: {contrasena_generada}\n")

    entrada_texto.delete(0, tk.END)  # Limpia el cuadro de texto

def eliminar_contenido_archivo():
    with open("nombres.txt", "w") as archivo:
        archivo.truncate(0)

with open("nombres.txt", "r") as archivo:
    contenido = archivo.read()

def generar_contrasena():
    longitud = 12  # Puedes ajustar la longitud de la contraseña según tus necesidades
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    contrasena_variable.set(contrasena)
    return contrasena


def mostrar_menu_contrasenas():
    global mostrar_contraseñas
    if mostrar_contraseñas == 0:
        mostrar_contraseñas = 1
        etiqueta.place(x = 200, y = 50)  # Muestra la etiqueta
    else:
        mostrar_contraseñas = 0
        etiqueta.place_forget()  # Oculta la etiqueta


def actualizar_contenido():
    with open("nombres.txt", "r") as archivo:
        contenido = archivo.read()
    texto_variable.set(contenido)
    ventana.after(1000, actualizar_contenido)

mostrar_contraseñas = 0

#Entrada de texto de contraseñas
entrada_texto = tk.Entry(ventana)
entrada_texto.place(x = 12, y = 50)

#menú principal
menu_principal = Menu(ventana)
ventana.config(menu=menu_principal)

#display texto nombres.txt
texto_variable = tk.StringVar()
texto_variable.set(contenido)

# Crea un widget Label para mostrar las contraseñas
etiqueta = tk.Label(ventana, textvariable=texto_variable)
etiqueta.place(x = 200, y = 50)

contrasena_variable = tk.StringVar()

menu_archivo = Menu(menu_principal)
menu_principal.add_cascade(label="Simple Password Generator", menu = menu_archivo)


menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

boton_guardar = tk.Button(ventana, text="Generar Contraseña", command = guardar_texto)
boton_guardar.place(x = 15, y = 20)


boton1 = tk.Button(ventana, text="Menú de Contraseñas", command = mostrar_menu_contrasenas, height = 2)
boton1.place(x = 10, y = 80)


boton_eliminar = tk.Button(ventana, text="Reset de Contraseñas", command=eliminar_contenido_archivo, height=2)
boton_eliminar.place(x=12, y=130)

# Iniciar la actualización del contenido
actualizar_contenido()

ventana.mainloop()