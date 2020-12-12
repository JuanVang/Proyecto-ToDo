import tkinter 
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import datetime
import os
import requests 
from bs4 import BeautifulSoup
from tkinter import messagebox
def main_menu():
    #Se usa la funcion datetime para que la fecha del calendario este acorde a la fecha actual
    fecha=datetime.datetime.now()
    ventana = Tk()
    ventana.title("Aplicacion ToDo")
    ventana.geometry("750x675")
    ventana.configure(bg="#A0E2FF")
    #Se cambia el icono de la ventana por uno mas acorde ocn la tematica de la aplicación
    ventana.iconbitmap("Icono.ico")

    notebook=ttk.Notebook(ventana)
    notebook.pack(fill=X)

    pestana1=ttk.Frame(notebook)
    pestana2=ttk.Frame(notebook)
    pestana3=ttk.Frame(notebook)    
    notebook.add(pestana1,text="Asignar tareas")
    notebook.add(pestana2,text="Tareas")
    notebook.add(pestana3,text="Pomodoro")


    label_titulo= Label(pestana1, text=" SELECCIONA LA FECHA EN LA QUE DESEAS COLOCAR LA TAREA",font=("Lucida console",13),bg= "#61b4e8" , relief = GROOVE,borderwidth= 2)
    label_titulo.pack(pady=0,side = TOP,fill=X,)
    #Se llama a la funcion calendar para que esta genere un calendario del cual se puedan seleccionar los dias y se puedan cambiar los meses y el año
    #Se hace uso de esta funcion porque permite que la interfaz sea una poco mas atractiva y permite que la aplicacion sea un mas interactiva
    calendario= Calendar(pestana1,selectmode="day",year=fecha.year,month=fecha.month,day=fecha.day)
    calendario.pack(fill= X,pady=2)

    def obtener_fecha():
        """
        configura la label al presionar el boton, y le asigna una nueva cadena de texto
        """
        label1.config(text="La Fecha seleccionada es: "+calendario.get_date())


    boton1 = Button(pestana1,text = "Seleccionar Fecha",font=("Lucida console",10), command = obtener_fecha,bg = "gray")
    boton1.pack(pady=2,fill=X)


    label1 =Label(pestana1, text="La fecha seleccionada es:",font=("Lucida console",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
    label1.pack(pady=0,fill=X)

    label_nombre_tarea=Label(pestana1,text="Tarea a Realizar",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    label_nombre_tarea.pack(pady=2,fill=X)
    
    entrada_nombre_tarea=Entry(pestana1,bd=2,bg="#A0E2FF",justify=CENTER,width=10)
    entrada_nombre_tarea.pack(pady=0,fill=X)

    label_lista_tareas=Label(pestana1,text="Hora de inicio (Formato 12 horas)",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    label_lista_tareas.pack(pady=2,fill= X)
    
    l_hor=Label(pestana1,text="Hora",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    l_hor.pack(pady=0,fill=X)
    numero_label=Spinbox(pestana1, from_=1,to= 12,bg="#A0E2FF",justify=CENTER,width=10)
    numero_label.pack(pady=0,fill=X)
    l_hor_2=Label(pestana1,text="Minuto",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    l_hor_2.pack(pady=0,fill=X)
    numero_label_2=Spinbox(pestana1, from_=0, to= 59,bg="#A0E2FF",justify=CENTER,width=10)
    numero_label_2.pack(pady=0,fill=X)

    #Se crea una variable asociada al menu AM-PM
    variable2=StringVar(pestana1)
    variable2.set("AM")
    #Se crea una lista con las oopciones que va a tener el menu 
    opciones_tareas=["AM","PM"]
    menu= OptionMenu(pestana1,variable2,*opciones_tareas)
    menu.config(width=8,bg="gray")
    menu.pack(pady=0,fill=X)

    label_final_tarea=Label(pestana1,text="Hora para finalizar la tarea (Formato de 12 horas) ",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    label_final_tarea.pack(pady=0,fill=X)

    l_hor_f=Label(pestana1,text="Hora",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    l_hor_f.pack(pady=0,fill=X)
    numero_label_hora_f=Spinbox(pestana1, from_=1,to= 12,bg="#A0E2FF",justify=CENTER,width=10)
    numero_label_hora_f.pack(pady=0,fill=X)
    l_hor_f_2=Label(pestana1,text="Minuto",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    l_hor_f_2.pack(pady=0,fill=X)
    numero_label_hora_f_2=Spinbox(pestana1, from_=0, to= 59,bg="#A0E2FF",justify=CENTER,width=10)
    numero_label_hora_f_2.pack(pady=0,fill=X)

    #Se crea una variable asociada al menu2 AM-PM 
    variable3=StringVar(pestana1)
    variable3.set("AM")
    #Se crea una lista con las opciones que va a tener el menu
    opciones_tareas=["AM","PM"]
    menu= OptionMenu(pestana1,variable3,*opciones_tareas)
    menu.config(width=8,bg="gray")
    menu.pack(pady=0,fill=X)

    label_prioridad=Label(pestana1,text="Seleccione la prioridad de su tarea",font=("Lucida console",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
    label_prioridad.pack(pady=2,fill=X)

    variable4=StringVar(pestana1)
    variable4.set("Prioridad alta")
    opciones_prioridad=["Prioridad alta","Prioridad media","Prioridad baja"]
    menu_prioridad=OptionMenu(pestana1,variable4,*opciones_prioridad)
    menu_prioridad.config(width=8,bg="#A0E2FF")
    menu_prioridad.pack(pady=0,fill=X)
    #tabla que le permite al usuario ver sus tareas
    tabla_tareas=ttk.Treeview(pestana2)
    
    tabla_tareas['columns']=("Tarea","Fecha","Hora Inicio","Hora Fin")

    tabla_tareas.column("#0",width=120,stretch=NO)
    tabla_tareas.column("Tarea",anchor=W,width=120)
    tabla_tareas.column("Fecha",anchor=W,width=80)
    tabla_tareas.column("Hora Inicio",anchor=W,width=80)
    tabla_tareas.column("Hora Fin",anchor=W,width=80)

    tabla_tareas.heading("#0",text="Tarea",anchor=W)
    tabla_tareas.heading("Tarea",text="Fecha",anchor=W)
    tabla_tareas.heading("Fecha",text="Hora inicio",anchor=W)
    tabla_tareas.heading("Hora Inicio",text="Hora Fin",anchor=W)
    tabla_tareas.heading("Hora Fin",text="Prioridad",anchor=W)
    

    tabla_tareas.pack(pady=20)

    def añadir_tareas():
        """
        esta funcion es la base de la aplicacion pues es la que introduce los datos sobre la tarea del usuario en la tabla
        """
        tabla_tareas.insert(parent='',index='end',text=entrada_nombre_tarea.get(),values=(calendario.get_date(),numero_label.get()+" y "+numero_label_2.get()+" "+variable2.get(),numero_label_hora_f.get()+" y "+numero_label_hora_f_2.get()+" "+variable3.get(),variable4.get()))
        

    boton_anadir=Button(pestana1,text="Añadir Tarea",font=("Lucida console",8), bg = "gray",command=añadir_tareas)
    boton_anadir.pack(pady=2,fill=X)

    def sacar_info_pomodoro():
        #Este web scraper saca informacion de un blog sobre el metodo pomodoro, se procuro sacar la informacion mas importante.
        url = "https://lecturaagil.com/como-ser-mas-productivo-con-la-tecnica-del-pomodoro/"
        pagina= requests.get(url)
        soup= BeautifulSoup(pagina.content,"html.parser")
        pomodoro= soup.find_all("p")
        textofin=[]
        texto=""
        for pom in range(0,len(pomodoro)):
            if pomodoro[pom].string == None:
                continue
            else:
                textofin+=[pomodoro[pom].string]
        for item in range(3,len(textofin)-11):
            if textofin[item] == '\xa0':
                continue
            else:
                texto+=textofin[item]
    
        messagebox.showinfo(message=texto,title="Info")

    Boton_info_pomodoro=Button(pestana3,text="Info sobre metodo pomodoro",command=sacar_info_pomodoro)
    Boton_info_pomodoro.pack()

    ventana.mainloop()
#Menu para iniciar sesion
def iniciar_sesion():
    global menu_log
    menu_log= Toplevel(log_win)
    menu_log.geometry("450x300")
    menu_log.title("Inicio de sesion")
    menu_log.iconbitmap("Icono.ico")
    menu_log.configure(bg="#A0E2FF")

    Label_init=Label(menu_log,text="Introduzca sus datos",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2)
    Label_init.pack(pady=5,fill=X)

    global verificar_nombre
    global verificar_contrasena

    verificar_nombre=StringVar()
    verificar_contrasena=StringVar()

    global nombre_usuario_entrada
    global contrasena_usuario_entrada

    Label_nombre=Label(menu_log,text="Usuario",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2)
    Label_nombre.pack(pady=5,fill=X)

    nombre_usuario_entrada=Entry(menu_log,textvariable=verificar_nombre)
    nombre_usuario_entrada.pack(pady=5)

    Label_contra=Label(menu_log,text="Contraseña",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2)
    Label_contra.pack(pady=5,fill=X)

    contrasena_usuario_entrada=Entry(menu_log,textvariable=verificar_contrasena,show="*")
    contrasena_usuario_entrada.pack(pady=5)

    boton_init=Button(menu_log,text="Iniciar Sesión",borderwidth= 2,width=30,font=("Lucida console",13),bg= "#61b4e8",command=verificar_login)
    boton_init.pack(pady=5,fill=X)
#funcion para verificar que el usuario este registrado 
def verificar_login():
    usuario1=verificar_nombre.get()
    contrasena1=verificar_contrasena.get()
    nombre_usuario_entrada.delete(0,END)
    contrasena_usuario_entrada.delete(0,END)
    lista_archivos = os.listdir()
    if usuario1 in lista_archivos:
        archivo1=open(usuario1,"r")
        verificar=archivo1.read().splitlines()
        if contrasena1 in verificar:
            logeo_correcto()
        else:
            contraseña_no_reconocida()
    else:
        usuario_no_encontrado()
#ventana que se abre al logearse correctamente
def logeo_correcto():
    global pantalla_logeo_correcto
    pantalla_logeo_correcto = Toplevel(menu_log)
    pantalla_logeo_correcto.title("Completado")
    pantalla_logeo_correcto.geometry("250x80")
    pantalla_logeo_correcto.configure(bg="green")
    Label(pantalla_logeo_correcto,text="Logeo exitoso",bg="green",font=("Lucida console",13)).pack(pady=10)
    Button(pantalla_logeo_correcto,text="Aceptar",command=borrar_logeo_exitoso).pack(pady=5,fill=X)
#cierra el menu de login y abre la ventana principal de la aplicacion
def borrar_logeo_exitoso():
    pantalla_logeo_correcto.destroy()
    menu_log.destroy()
    main_menu()
#menu que se abre al no encontrar la contraseña correcta
def contraseña_no_reconocida():
    global pantalla_contraseña_no_reconocida
    pantalla_contraseña_no_reconocida = Toplevel(log_win)
    pantalla_contraseña_no_reconocida.title("Completado")
    pantalla_contraseña_no_reconocida.geometry("250x80")
    pantalla_contraseña_no_reconocida.configure(bg="red")
    Label(pantalla_contraseña_no_reconocida,text="Contraseña invalida",bg="red",font=("Lucida console",13)).pack(pady=10,fill=X)
    Button(pantalla_contraseña_no_reconocida,text="Aceptar",command=borrar_contraseña_no_reconocida).pack(pady=5,fill=X)
#funcion que se ejecuta para cerrar el menu login
def borrar_contraseña_no_reconocida():
    pantalla_contraseña_no_reconocida.destroy()
#menu usuario no encontrado
def usuario_no_encontrado():
    global pantalla_usuario_no_encontrado
    pantalla_usuario_no_encontrado= Toplevel(log_win)
    pantalla_usuario_no_encontrado.title("Completado")
    pantalla_usuario_no_encontrado.geometry("250x80")
    pantalla_usuario_no_encontrado.configure(bg="red")
    Label(pantalla_usuario_no_encontrado,text="Usuario no encontrado",bg="red",font=("Lucida console",13)).pack()
    Button(pantalla_usuario_no_encontrado,text="Aceptar",command=borrar_usuario_no_encontrado).pack()
#funcion que se ejecuta para cerrar la ventana que se genera al no encontrar un usuario
def borrar_usuario_no_encontrado():
    pantalla_usuario_no_encontrado.destroy()
#Menu de registro para nuevos usuarios  
def Registro():
    global menu_regis
    menu_regis=Toplevel(log_win)
    menu_regis.title("Registro")
    menu_regis.geometry("450x300")
    menu_regis.configure(bg="#A0E2FF")
    menu_regis.iconbitmap("Icono.ico")

    global nombre_usuario
    global contrasena
    global entrada_nombre_usuario
    global entrada_contrasena

    nombre_usuario=StringVar()
    contrasena=StringVar()

    labe_tit=Label(menu_regis,text="Ingrese nombre de usuario y contraseña",borderwidth= 2,width=30,font=("Lucida console",13),bg= "#61b4e8")
    labe_tit.pack(pady=5,fill=BOTH)

    Label_nom_usu_=Label(menu_regis,text="Nombre de usuario",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2)
    Label_nom_usu_.pack(pady=5,fill=X)

    entrada_nombre_usuario=Entry(menu_regis,textvariable=nombre_usuario)
    entrada_nombre_usuario.pack(pady=5)

    Label_contra_=Label(menu_regis,text="Contraseña",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2)
    Label_contra_.pack(pady=5,fill=X)

    entrada_contrasena=Entry(menu_regis,textvariable=contrasena,show="*")
    entrada_contrasena.pack(pady=5)

    boton_registrar=Button(menu_regis,text="Registrarse",borderwidth= 2,width=30,font=("Lucida console",13),bg= "#61b4e8",command=registrar_usuario)
    boton_registrar.pack(pady=5)
#Crea un documento con el nombre de usuario y la contraseña en la carpeta del proyecto
def registrar_usuario():

    info_username=entrada_nombre_usuario.get()
    info_contrasena=entrada_contrasena.get()

    file=open(info_username,"w")
    file.write(info_username + "\n")
    file.write(info_contrasena)
    file.close()

    entrada_nombre_usuario.delete(0,END)
    entrada_contrasena.delete(0,END)

    Label(menu_regis,text="Registro exitoso",fg="green",font=("Lucida console",13),bg="#A0E2FF").pack(pady=2)
#Menu principal de Login
def Menu_main_cuenta():
    global log_win
    log_win= Tk()
    log_win.title("Aplicacion ToDo")
    log_win.geometry("400x400")
    log_win.configure(bg="#A0E2FF")
    log_win.iconbitmap("Icono.ico")

    label_inicio_sesion=Label(log_win,text="Menu principal",font=("Lucida console",13),bg= "#61b4e8" , relief = GROOVE,borderwidth= 2,width=300,height=3)
    label_inicio_sesion.pack(pady=2,fill=X)

    Logo=PhotoImage(file="Logo-ToDO.png")
    Logo=Logo.subsample(2,2)
    label_logo=Label(image=Logo)
    label_logo.pack()

    boton_inicio_sesion=Button(log_win,text="Iniciar Sesion",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2,command=iniciar_sesion)
    boton_inicio_sesion.pack(pady=15,fill=X)

    boton_registrarse=Button(log_win,text="Registrarse",font=("Lucida console",13),bg= "#61b4e8",borderwidth= 2,width=30,height=2,command=Registro)
    boton_registrarse.pack(pady=15,fill=X)

    log_win.mainloop()


Menu_main_cuenta()