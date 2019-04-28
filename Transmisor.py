from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from time import sleep

import cv2
import tkinter as tkk
import sys
import numpy
import math 
from Archivo import Archivo
from Trama import Trama

arch = Archivo('','')


class Interfaz:
    def __init__(self):
        self.Interfaz = Tk()
        self.Interfaz.state('zoomed')
        self.Interfaz.configure(bg='#636363')
        
        #SELECCION DE ARCHIVO
        self.seleccionarArchivo = Button(self.Interfaz,text="Seleccionar Archivo", command=self.abrirArchivo).place(relx=0.1,rely=0.1)

        #PATRONES POR SEGUNDO
        self.etiqueta = Label(text="Patrones por segundo: ").place(relx=0.1,rely=0.15)
        self.patronesPorSegundo = ttk.Combobox(state="readonly", values=[5,10,15,20])
        self.patronesPorSegundo.place(relx=0.2,rely=0.15)
        self.patronesPorSegundo.current(0)

        #TAMAÑO DE LA MATRIZ
        self.etiqueta2 = Label(text="Tamaño de la matriz: ").place(relx=0.1,rely=0.2)
        self.tamanoMatriz = ttk.Combobox(state="readonly", values=[8,10,12,14,16,100])
        self.tamanoMatriz.place(relx=0.2,rely=0.2)
        self.tamanoMatriz.current(0)
        
        #NUMERO DE COLORES
        self.etiqueta3 = Label(text="Número de colores").place(relx=0.1,rely=0.25)
        self.numeroColores = ttk.Combobox(state="readonly", values=["2","4","8"])
        self.numeroColores.place(relx=0.2,rely=0.25)
        self.numeroColores.current(0)
        
        self.transmitir = Button(self.Interfaz,text="Comenzar visualziación",command=self.InicioTransmision).place(relx=0.1,rely=0.3)

        #self.scrolledtext1 = st.ScrolledText(self.Interfaz, width=30, height=20)
        #self.scrolledtext1.place(relx=0.1, rely=0.35)

        #PRUEBA DE IMAGEN EN LABEL
        self.l1 = tkk.Label(self.Interfaz, text="   ", borderwidth=4, relief="groove")
        self.l1.place(relx=0.4,rely=0.005,width=700, height=700)
        
        self.Interfaz.mainloop()
        
    def abrirArchivo(self):
            nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            if nombrearch!='':
                Bytes = numpy.fromfile(nombrearch, dtype = "uint8")
                Bits = numpy.unpackbits(Bytes)
                
                arch.contenido = Bits
                arch.nombreArchivo = nombrearch
                self.scrolledtext1.delete("1.0",END) 
                self.scrolledtext1.insert("1.0", arch.contenido)
                print(arch.contenido.size)
            
    def InicioTransmision(self):
        cont = arch.contenido
        pps = int(self.patronesPorSegundo.get())
        tam = int(self.tamanoMatriz.get())
        col = int(self.numeroColores.get())
        
        #print(cont[0:24],cont[0:24].size)
        #print(cont[24:48],cont[24:48].size)
        #print(cont[0:48],cont[0:48].size)
        BitsPorTrama = int((((tam*tam)-3)*math.log2(col))-32)
        NumBits = cont.size
        tamanoUtil = math.ceil(math.log2(BitsPorTrama))
        BitsPorTrama = BitsPorTrama - tamanoUtil
        NumTramas = math.ceil(NumBits/BitsPorTrama)
        
        print('Bits contenido: ', NumBits)
        print('Bits por trama*: ', BitsPorTrama)
        print('Número de tramas: ', NumTramas)
        print('Número de celdas: ', int((tam*tam)-3))
        print('********************************************************')
        tramas = Trama(cont,NumTramas,tamanoUtil,BitsPorTrama,col,tam)
        tramas.generarTramas()

        x=0
        try:
            while True:
                if x < NumTramas: 
                    print('Mostrando trama ',x)
                    nombreImagen = 'Imagen'+str(x)+'.png'
                    img = PhotoImage(file = nombreImagen)
                    self.l1.configure(image = img)
                    self.Interfaz.update()
                    sleep(1/pps)
                    x+=1
                elif x==NumTramas:
                    x=0
        except KeyboardInterrupt:
            pass
            x=NumTramas+2
        x=NumTramas+2
        
        #img = PhotoImage(file=nombreImagen)
        #self.l1 = ttk.Label(self.Interfaz,image=img)
        #self.l1.place(relx=0.4,rely=0.005,width=702, height=702)
        #
            
aplicacion1=Interfaz()


