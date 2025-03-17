from tkinter import *
from tkinter import ttk, messagebox

class App:
    def __init__(self):
        #Ventana
        self.__root = Tk()
        self.__root.title("Laboratorio IPC2")
        self.__root.iconbitmap('icono.ico')
        self.__root.geometry('300x200')
        self.__root.resizable(False, False)
        
        self.__titulo = Label(self.__root, text="Menú Principal")
        self.__titulo.config(font=('Consolas', 14, 'bold'))
        self.__titulo.pack(pady=5)

        #Botones
        self.__btn_registrar_orden = Button(self.__root, text="Nueva Orden",  command=self.__registrar_orden)
        self.__btn_registrar_orden.pack_propagate(False)
        self.__btn_registrar_orden.config(
            height=1, 
            width=20,
            bg='green2',
            fg='white',
            font=('Consolas', 14, 'bold')
        )
        self.__btn_registrar_orden.pack(pady=5)

        self.__btn_mostrar_ordenes = Button(self.__root, text="Ver Órdenes", command=self.mostrar_ordenes)
        self.__btn_mostrar_ordenes.pack_propagate(False)
        self.__btn_mostrar_ordenes.config(
            height=1, 
            width=20,
            bg='RoyalBlue1',
            fg='white',
            font=('Consolas', 14, 'bold')
        )
        self.__btn_mostrar_ordenes.pack(pady=5)

        self.__btn_salir = Button(self.__root, text="Salir", command=self.__terminar_programa)
        self.__btn_salir.pack_propagate(False)
        self.__btn_salir.config(
            height=1, 
            width=20,
            bg='red',
            fg='white',
            font=('Consolas', 14, 'bold')
        )
        self.__btn_salir.pack(pady=5)

        #Lista para almacenar las órdenes
        self.ordenes = []
        
        self.__root.mainloop()

    def __terminar_programa(self):
        #Pregunta si realmente se quiere cerrar el programa
        #Yes -> True
        #No -> False
        res = messagebox.askyesno('Terminar programa', 'Quieres salir del programa?')
        if res:
            self.__root.destroy() #Cerrar el programa
    
    def __registrar_orden(self):
        #Crea una segunda ventana
        registro = Toplevel(self.__root)
        registro.iconbitmap('icono.ico')
        registro.title("Registrar nueva orden")
        registro.geometry("400x360")
        
        Label(registro, text="Nombre del cliente").pack(pady=5)
        nombre_entry = Entry(registro) #Input para nombre del cliente
        nombre_entry.pack(pady=5)
        
        Label(registro, text="Especialidad de la pizza").pack(pady=5)
        #Lista de opciones que tendrá el selector
        pizzas = ["Pepperoni", "Hawaiana","Vegetariana", "Cuatro Quesos"]
        #Selector
        pizza_combo = ttk.Combobox(registro, values=pizzas)
        pizza_combo.config(state="readonly")
        pizza_combo.pack(pady=5)
        pizza_combo.current(0) #Coloca el primer elemento como default

        #Agrega un elemento Text para mostrar el estado de la orden
        Label(registro, text="Estado de la orden").pack(pady=5)
        estado_orden = Text(registro, height=6, width=40)
        estado_orden.config(state='disable') #Modo disable para que no sea editable
        estado_orden.pack(pady=5)

        #Agregar una pizza a la orden
        lista_pizzas = []
        def agregar_pizza():
            lista_pizzas.append(pizza_combo.get())
            estado_orden.delete(1.0, END) #Elimintar el contenido del inicio al finla
            estado_orden.config(state='normal') #Cambiar a modo normal para editar
            estado_orden.insert(END, f"1 - {lista_pizzas[-1]}\n") #Agregar al final
            estado_orden.config(state='disable') #Regresar a modo disable

        #Eliminar la última pizza agregada
        def eliminar_pizza():
            if lista_pizzas: 
                lista_pizzas.pop() #Eliminar de la lista
                estado_orden.config(state='normal')
                estado_orden.delete("end-2l","end-1l") #Eliminar del Text
                estado_orden.config(state='disable')

        #Registra la orden
        def registrar():
            nombre = nombre_entry.get() #Obtener el nombre ingresado
            if nombre and lista_pizzas:
                self.ordenes.append({"cliente": nombre, "pizza": lista_pizzas}) #Agrega la orden a la lista
                messagebox.showinfo("Éxito", "Orden registrada", parent=registro)
                registro.destroy() #Destruye/cierra la ventana
            else:
                messagebox.showerror("Error", "No se puede registrar la orden", parent=registro)
        
        #Agrupar los botones para ponerlos horizontalmente
        frm = Frame(registro)
        frm.pack(pady=5)
        Button(frm, text="Agregar Pizza", command=agregar_pizza, bg='green2', fg='white', relief=GROOVE).pack(padx=30, side='left')
        Button(frm, text="Eliminar Pizza", command=eliminar_pizza, bg='red', fg='white', relief=GROOVE).pack(padx=30, side='right')

        Button(registro, text="Registrar Orden", command=registrar, bg='RoyalBlue1', fg='white', relief=GROOVE).pack(pady=15)
    
    def mostrar_ordenes(self):
        if not self.ordenes:
            messagebox.showwarning('Ordenes', 'No hay ordenes para mostrar', parent=self.__root)
        else:
            print("Lista de Órdenes:")
            for i, orden in zip(range(1, len(self.ordenes)+1), self.ordenes):
                print(f"No.Orden: {i}")
                print(f"Cliente: {orden['cliente']}")
                print(f"Orden: {orden['pizza']}")
                print("----------------------------------------")

# Iniciar la aplicación
if __name__ == "__main__":
    App()