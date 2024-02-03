from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

y = [0]

fig, ax = plt.subplots(figsize=(10, 5))

ax.stairs(y, linewidth=2)
ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1))  
#ax.grid(True)  

def actualizar_grafico():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    for palabra in contenido_texto.split():
       
        for caracter in palabra:
            
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            valores_numericos.extend([int(bit) for bit in caracter_binario])

    nueva_data = valores_numericos
    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1)) 
    #ax.grid(True)  
    ax.stairs(nueva_data, linewidth=2)
    
    
    for i in range(0, len(nueva_data)+2, 8):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)
       
 

    canvas.draw()

def actualizar_grafico1():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    for palabra in contenido_texto.split():
        for caracter in palabra:
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            valores_numericos.extend([int(bit) if bit == '0' else -1 for bit in caracter_binario])

    nueva_data = valores_numericos
    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1)) 
    #ax.grid(True)  
    ax.stairs(nueva_data, linewidth=2)
    
    for i in range(0, len(nueva_data)+2, 8):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)


  
    canvas.draw()

def actualizar_grafico2():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    for palabra in contenido_texto.split():
        for caracter in palabra:
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            valores_numericos.extend([int(bit) if bit == '1' else -1 for bit in caracter_binario])

    nueva_data = valores_numericos
    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1))  
    #ax.grid(True)  
    ax.stairs(nueva_data, linewidth=2)
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    
    for i in range(0, len(nueva_data)+2, 8):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)


  
    canvas.draw()


def actualizar_grafico3():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    for palabra in contenido_texto.split():
        for caracter in palabra:
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            valores_numericos.extend([int(bit) if bit == '1' else -1 for bit in caracter_binario])

    nueva_data = valores_numericos
    nueva_data_interpolada = []

    for i in range(len(nueva_data) - 1):
        nueva_data_interpolada.extend([nueva_data[i], 0] if nueva_data[i] != 0 else [0])

    nueva_data_interpolada.append(nueva_data[-1]) 

    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1))
    ax.stairs(nueva_data_interpolada, linewidth=2)
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1)

    for i in range(0, len(nueva_data_interpolada) + 2, 16):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)

  

    canvas.draw()

def actualizar_grafico4():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    alternar_signo = 1  

    for palabra in contenido_texto.split():
        for caracter in palabra:
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            for bit in caracter_binario:
                if bit == '1':
                    valores_numericos.append(alternar_signo)
                    alternar_signo *= -1 
                else:
                    valores_numericos.append(0)

    nueva_data = valores_numericos
    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1))  
    ax.stairs(nueva_data, linewidth=2)
    
    for i in range(0, len(nueva_data) + 2, 8):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)


    canvas.draw()

def actualizar_grafico5():
    contenido_texto = cuadrotexto.get("1.0", "end-1c")
    valores_numericos = []

    alternar = 1  

    for palabra in contenido_texto.split():
        for caracter in palabra:
            caracter_binario = bin(ord(caracter))[2:].zfill(8)
            
            for bit in caracter_binario:
                if bit == '0':
                    valores_numericos.append(alternar)
                    alternar *= -1  
                else:
                    valores_numericos.append(0) 

    nueva_data = valores_numericos
    ax.clear()
    ax.set(ylim=(-1.5, 1.5), yticks=np.arange(-1, 1.5), xticks=np.arange(0, 0 , 1))  
    ax.stairs(nueva_data, linewidth=2)
    
    for i in range(0, len(nueva_data) + 2, 8):
        ax.axvline(x=i, color='black', linestyle='--', linewidth=1.5)

    

    canvas.draw()

ventana = Tk()
ventana.geometry("1300x500")
ventana.iconbitmap('l001.ico')
ventana.title("SEÑALES EN BANDA BASE")
ventana.configure(bg="white")
ventana.resizable(False, False)

frame = Frame(ventana, bg='white')
frame.pack()

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=LEFT, padx=5, pady=5)

etiqueta = Label(frame, text="\n")
etiqueta.pack(side=TOP, padx=5, pady=5)
etiqueta.configure(bg="white")

etiqueta = Label(frame, text="Hola,por favor ingresa el texto\npara poder graficarlo")
etiqueta.pack(side=TOP, padx=5, pady=5)
etiqueta.configure(bg="white")


cuadrotexto = Text(frame, width=20, height=1)
cuadrotexto.pack(side=TOP, padx=15, pady=5)

etiqueta = Label(frame, text="\n")
etiqueta.pack(side=TOP, padx=5, pady=5)
etiqueta.configure(bg="white")

boton = Button(frame, width=20, height=1,text="UNIPOLAR POSITIVO", command=actualizar_grafico)
boton.pack(side=TOP, padx=5, pady=5)
boton = Button(frame, width=20, height=1,text="UNIPOLAR NEGATIVO", command=actualizar_grafico1)
boton.pack(side=TOP, padx=5, pady=5)  
boton = Button(frame, width=20, height=1,text="POLAR NRZ", command=actualizar_grafico2)
boton.pack(side=TOP, padx=5, pady=5)
boton = Button(frame, width=20, height=1,text="POLAR RZ", command=actualizar_grafico3)
boton.pack(side=TOP, padx=5, pady=5)
boton = Button(frame, width=20, height=1,text="BIPOLAR 1", command=actualizar_grafico4)
boton.pack(side=TOP, padx=5, pady=5)
boton = Button(frame, width=20, height=1,text="BIPOLAR 0", command=actualizar_grafico5)
boton.pack(side=TOP, padx=5, pady=5)

etiqueta = Label(frame, text="©HenryArevalo")
etiqueta.pack(side=BOTTOM, padx=5, pady=5)
etiqueta.configure(bg="white")

ventana.mainloop()
