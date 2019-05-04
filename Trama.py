import math
from EstructuraTrama import EstructuraTrama
from PatronDeColor import PatronDeColor
from Imagen3 import Imagen

class Trama:
    def __init__(self,contenido,NumTramas,tamanoUtil,BitsPorTrama,numColores,tamanoMatriz):
        self.contenido = contenido
        self.NumTramas = NumTramas
        self.tamanoUtil = tamanoUtil
        self.BitsPorTrama = BitsPorTrama
        self.numColores = numColores
        self.tamanoMatriz = tamanoMatriz
        self.celdaSincro = 0
        #print('Bits contenido: ', self.contenido.size)
        #print('Bits por trama*: ',self.BitsPorTrama)
        #print('Número de tramas: ',self.NumTramas)
        
    def generarTramas(self):
        for x in range(self.NumTramas):
            self.celdaSincro = x%2
            cont = self.contenido[(x*self.BitsPorTrama):((x+1)*self.BitsPorTrama)]
            tramaX = EstructuraTrama(self.NumTramas,x+1,self.BitsPorTrama,self.tamanoUtil,cont)
            print(tramaX.getTrama(),tramaX.getTrama().size)
            patron = PatronDeColor(tramaX.getTrama(),self.numColores,self.tamanoMatriz,self.celdaSincro)
            patron.arregloColores()

            Img = Imagen(patron.arregloColores(),self.tamanoMatriz,self.numColores,x)
            Img.generarImagen()
            
    
        
        

        
