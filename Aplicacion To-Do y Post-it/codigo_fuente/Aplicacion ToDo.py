from tkinter import *
from tkcalendar import *
import datetime
#Se usa la funcion datetime para que la fecha del calendario este acorde a la fecha actual
fecha=datetime.datetime.now()
ventana = Tk()
ventana.title("Aplicacion ToDo")
ventana.geometry("750x788")
ventana.configure(bg="#A0E2FF")
#Se cambia el icono de la ventana por uno mas acorde ocn la tematica de la aplicación
icono=ventana.iconbitmap("Icono.ico")
label_titulo= Label(ventana, text=" SELECCIONA LA FECHA EN LA QUE DESEAS COLOCAR LA TAREA",font=("Arial bold",13),bg= "#61b4e8" , relief = GROOVE,borderwidth= 2)
label_titulo.pack(pady=0,side = TOP,fill=X,)
#Se llama a la funcion calendar para que esta genere un calendario del cual se puedan seleccionar los dias y se puedan cambiar los meses y el año
#Se hace uso de esta funcion porque permite que la interfaz sea una poco mas atractiva y permite que la aplicacion sea un mas interactiva
calendario= Calendar(ventana,selectmode="day",year=fecha.year,month=fecha.month,day=fecha.day)
calendario.pack(fill= X,pady=0)

def obtener_fecha():
    """
    configura la label al presionar el boton, y le asigna una nueva cadena de texto
    """
    label1.config(text="La Fecha seleccionada es: "+calendario.get_date())


boton1 = Button(ventana,text = "Seleccionar Fecha",font=("Arial bold",10), command = obtener_fecha,bg = "gray")
boton1.pack(pady=0,fill=X)


label1 =Label(ventana, text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label1.pack(pady=0,fill=X)

label_lista_tareas=Label(ventana,text="Hora de inicio (Formato 12 horas)",font=("Arial bold",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
label_lista_tareas.pack(pady=0,fill= X)

hora_inicio_tarea=Entry(ventana,bd=2,bg="#A0E2FF",justify=CENTER)
hora_inicio_tarea.pack(pady=0,fill=X)

#Se crea una variable asociada al menu AM-PM
variable2=StringVar(ventana)
variable2.set("AM")
#Se crea una lista con las oopciones que va a tener el menu 
opciones_tareas=["AM","PM"]
menu= OptionMenu(ventana,variable2,*opciones_tareas)
menu.config(width=10,bg="#A0E2FF")
menu.pack(pady=0,fill=X)

label_final_tarea=Label(ventana,text="Hora para finalizar la tarea (Formato de 12 horas) ",font=("Arial bold",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
label_final_tarea.pack(pady=0,fill=X)

hora_final_tarea=Entry(ventana,bd=2,bg="#A0E2FF",justify=CENTER,width=10)
hora_final_tarea.pack(pady=0,fill=X)

#Se crea una variable asociada al menu2 AM-PM 
variable3=StringVar(ventana)
variable3.set("AM")
#Se crea una lista con las opciones que va a tener el menu
opciones_tareas=["AM","PM"]
menu= OptionMenu(ventana,variable3,*opciones_tareas)
menu.config(width=10,bg="#A0E2FF")
menu.pack(pady=0,fill=X)

def limpiar_cuadros():

    """
    Borra los datos escritos en las 2 entradas anteriores en un rango de 0 a 100 caracteres
    """
    hora_inicio_tarea.delete(0,100)
    hora_final_tarea.delete(0,100)


boton_anadir=Button(ventana,text="Limpiar entradas",font=("Arial bold",8), bg = "gray",command=limpiar_cuadros)
boton_anadir.pack(pady=0,fill=X)

label_nombre_tarea=Label(ventana,text="Tarea a Realizar",font=("Arial bold",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
label_nombre_tarea.pack(pady=0,fill=X)
#Se crea una variable asociada al menu de tareas 
variable=StringVar(ventana)
variable.set("Estudiar")
#Se crea una lista con las tareas disponibles hasta el momento, (se espera que en la proxima version tenga un repertorio mas amplio de tareas)
opciones_tareas=["Estudiar","Ejercitarse", "Leer", "Comer", "Dormir", "Bañarse","Limpiar hogar","Lavar platos"]
menu= OptionMenu(ventana,variable,*opciones_tareas)
menu.config(width=10,bg="#A0E2FF")
menu.pack(pady=0,fill=X)


label3=Label(ventana, text="Seleccione una casilla para anotar su tarea (max 5)",font=("Arial bold",10),bg="#61b4e8",relief = GROOVE,borderwidth= 2)
label3.pack(pady=0,fill=X)

#Esta spinbox es la que determina en que label se va a ubicar la tarea seleccionada
numero_label=Spinbox(ventana, from_=1, to= 5,bg="#A0E2FF",justify=CENTER,width=10)
numero_label.pack(pady=0,fill=X)

#Por el momento esta funcion y el programa se encuentran limitados a un maximo de 5 tareas
def colocar_tarea():

    """
    Esta funcion obtiene un caracter generado por la spinbox en un rango de 1 a 5, dependiendo del caracter, la tarea se posicionaen una label distita.
    """

    numero=numero_label.get()

    if numero == "1":
        label_tarea1.config(text="Para la fecha "+calendario.get_date()+" tiene como tarea "+variable.get()+ " desde las "+hora_inicio_tarea.get()+ " "+variable2.get()+" hasta las "+hora_final_tarea.get()+" "+variable3.get(),bg="#A0E2FF")
    elif numero == "2":
        label_tarea2.config(text="Para la fecha "+calendario.get_date()+" tiene como tarea "+variable.get()+" desde las "+hora_inicio_tarea.get()+ " "+variable2.get()+" hasta las "+hora_final_tarea.get()+" "+variable3.get(),bg="#A0E2FF")
    elif numero == "3":
        label_tarea3.config(text="Para la fecha "+calendario.get_date()+" tiene como tarea "+variable.get()+" desde las "+hora_inicio_tarea.get()+ " "+variable2.get()+" hasta las "+hora_final_tarea.get()+" "+variable3.get(),bg="#A0E2FF")
    elif numero == "4":
        label_tarea4.config(text="Para la fecha "+calendario.get_date()+" tiene como tarea "+variable.get()+" desde las "+hora_inicio_tarea.get()+ " "+variable2.get()+" hasta las "+hora_final_tarea.get()+" "+variable3.get(),bg="#A0E2FF")
    elif numero == "5":
        label_tarea5.config(text="Para la fecha "+calendario.get_date()+" tiene como tarea "+variable.get()+" desde las "+hora_inicio_tarea.get()+ " "+variable2.get()+" hasta las "+hora_final_tarea.get()+" "+variable3.get(),bg="#A0E2FF")


boton_anadir=Button(ventana,text="Añadir Tarea",font=("Arial bold",8), bg = "gray",command=colocar_tarea)
boton_anadir.pack(pady=0,fill=X)

label_tarea1=Label(ventana,text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label_tarea1.pack(pady=0,fill=X)


def borrar():
    """
    Cambia la cadena de texto de la label a una cadena vacia y cambia el color de fondo de la label
    """
    #Se cambia el color a un verde claro para representar que la tarea fue completada con exito
    label_tarea1.config(text="",bg="#9DF9B7")

   

boton_completar1=Button(ventana,text="Completar tarea",font=("Arial bold",8), bg = "gray",command=borrar)
boton_completar1.pack(pady=0,fill=X)

label_tarea2=Label(ventana,text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label_tarea2.pack(pady=0,fill=X)

def borrar2():
    """
    Cambia la cadena de texto de la label a una cadena vacia y cambia el color de fondo de la label
    """
    label_tarea2.config(text="",bg="#9DF9B7")
    

boton_completar2=Button(ventana,text="Completar tarea",font=("Arial bold",8), bg = "gray",command=borrar2)
boton_completar2.pack(pady=0,fill=X)

label_tarea3=Label(ventana,text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label_tarea3.pack(pady=0,fill=X)

def borrar3():
    """
    Cambia la cadena de texto de la label a una cadena vacia y cambia el color de fondo de la label
    """
    label_tarea3.config(text="",bg="#9DF9B7")
    

boton_completar3=Button(ventana,text="Completar tarea",font=("Arial bold",8), bg = "gray",command=borrar3)
boton_completar3.pack(pady=0,fill=X)


label_tarea4=Label(ventana,text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label_tarea4.pack(pady=0,fill=X)

def borrar4():
    """
    Cambia la cadena de texto de la label a una cadena vacia y cambia el color de fondo de la label
    """
    label_tarea4.config(text="",bg="#9DF9B7")
    

boton_completar4=Button(ventana,text="Completar tarea",font=("Arial bold",8), bg = "gray",command=borrar4)
boton_completar4.pack(pady=0,fill=X)


label_tarea5=Label(ventana,text="",font=("Arial bold",10),bg="#A0E2FF",relief = SUNKEN,borderwidth= 2)
label_tarea5.pack(pady=0,fill=X)

def borrar5():

    """
    Cambia la cadena de texto de la label a una cadena vacia y cambia el color de fondo de la label
    """
    label_tarea5.config(text="",bg="#9DF9B7")

boton_completar5=Button(ventana,text="Completar tarea",font=("Arial bold",8), bg = "gray",command=borrar5)
boton_completar5.pack(pady=0,fill=X)


ventana.mainloop()