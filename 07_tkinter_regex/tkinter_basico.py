from tkinter import * #Importar la librería tkinter
from tkinter import filedialog, messagebox

root = Tk() #Instanciar un nuevo objeto de ventana principal
root.title('Laboratorio IPC2') #Título de la ventana
root.iconbitmap('icono.ico') #Cambiar el icono de la ventana
root.geometry('300x300') #Tamaño de la ventana
root.resizable(False, False) #True -> Cambiar el tamaño de la ventana | False -> Fijar el tamaño de la ventana
root.config(bg='lightblue') #Configuraciones de la ventana, en este caso el color de fondo


################################################## LABEL ##################################################
lbl = Label(root, text='Widgets Básicos')
#Personalizar o configurar el elemento
lbl.config(
    justify=CENTER,
    bg='lightblue',
    font=('default',14,'bold')
)
lbl.pack(side='top', pady=40) #Mostrar y posicionar el objeto en la ventana
lbl.pack_propagate(0)

lbl2 = Label(root, text='Nombre')
lbl2.config(
    justify=CENTER,
    bg='lightblue',
    font=('default',12,'normal')
)
lbl2.place(x=35, y=90)#Mostrar y posicionar el objeto en la ventana diferente de pack()


################################################## ENTRY ##################################################
entry = Entry(root, width=25)
entry.place(x=110, y=90, height=25)
# entry.get() #Recuperar el valor ingresado


################################################## BUTTON ##################################################
def saludar():
    if not (nombre := entry.get()): 
        #Si no se ingreso ningún nombre en el Entry
        nombre = 'Estudiante'
    #Ventana emergente para mostrar información
    messagebox.showinfo(message=f'Hola {nombre}', title='Saludos', parent=root) 

#text -> Texto a mostrar en el botón
#command -> función a ejecutar cuando se haga click en el botón
btn = Button(root, text='Saludar', command=saludar)
btn.config(
    width=20,
    relief='solid',
    font=('default', 14, 'normal')
)
btn.place(x=35, y=150)

def leer_archivo():
    #initialdir -> directorio que abrirá por defecto
    #filetypes -> Tipos de archivo que se puede abrir
    file = filedialog.askopenfile(
        title='Abrir archivo',
        initialdir='./',
        filetypes=(
            ('Archivo txt', '*.txt'), 
            ('Todos los archivos', '*.*')
        )
    )

    if file:
        contenido = file.read()
        print(contenido)
        file.close()

    #################### Si lo que queremos es preguntar por el archivo pero leerlo después ####################
    '''
    file = filedialog.askopenfilename(
        title='Abrir archivo',
        initialdir='./',
        filetypes=(
            ('Archivo txt', '*.txt'), 
            ('Todos los archivos', '*.*')
        )
    )

    if file != '' or file is not None:
        with open(file, mode='r', encoding='UTF-8') as f:
            print(f.read())
    '''

btn2 = Button(root, text='Leer archivo', command=leer_archivo)
btn2.config(
    width=20,
    relief='solid',
    font=('default', 14, 'normal')
)
btn2.place(x=35, y=220)

root.mainloop() #Loop para ejecutar el programa


################################################## Posicionar Elementos ##################################################

# https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/

