import numpy as np
import math
import cv2

class PatronDeColor:
    def __init__(self,trama,numColores,tamanoMatriz,celdaSincro):
        self.trama = trama
        self.numColores = numColores
        self.tamanoMatriz = tamanoMatriz
        self.celdaSincro = celdaSincro

    def arregloColores(self):
                            #Dos 
        Colores = np.array([[[0,0],     #Blanco         El último digito de cada arreglo representa un color
                            [1,1]],     #Negro

                            #Cuatro 
                            [[0,0,1],   #Negro
                             [0,1,2],   #Rojo
                             [1,0,3],   #Verde
                             [1,1,4]],  #Azul

                            #Ocho
                            [[0,0,0,0],     #Blanco
                             [0,0,1,1],     #Negro
                             [0,1,0,2],     #Rojo
                             [0,1,1,3],     #Verde
                             [1,0,0,4],     #Azul
                             [1,0,1,5],     #Magenta
                             [1,1,0,6],     #Cian
                             [1,1,1,7]]])   #Amarillo

        indice = int(math.log2(self.numColores))
        numCeldas = int(self.trama.size/indice)
        #print('Celdas: **',numCeldas)
        arregloColor = np.array([])
        
        for x in range(numCeldas):
            color = Colores[indice-1]
            color = np.array(color)
            celda = self.trama[(x*indice):((x+1)*indice)]
            for y in range(color.shape[0]):
                if np.array_equal(color[y][0:indice],celda):
                                  if arregloColor.size > 0:
                                      arregloColor = np.concatenate((arregloColor,color[y][-1]),axis=None)
                                  else:
                                      arregloColor = color[y][-1]

        #Agregando la celda de sincronización
        arregloColor = np.insert(arregloColor,0,self.celdaSincro)
        arregloColor = np.insert(arregloColor,self.tamanoMatriz-1,self.celdaSincro)
        arregloColor = np.concatenate((arregloColor,self.celdaSincro),axis=None)
        
        #print('Arreglo de colores: ',arregloColor,arregloColor.size)
        return arregloColor
        
