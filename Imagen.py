import cv2
import numpy as np

class Imagen:
    def __init__(self,arregloColores,tamanoMatriz,numColores,numImagen):
        self.arregloColores = arregloColores
        self.tamanoMatriz = tamanoMatriz
        self.numColores = numColores
        self.numImagen = numImagen
    
    def generarImagen(self):  
        img = cv2.imread('base.jpg',cv2.IMREAD_COLOR)
        #tamanoCelda = int(700/(self.tamanoMatriz + 8))
        tamanoCelda = int(700/(self.tamanoMatriz + 10))+1

        print('Arreglo Colores: ',self.arregloColores)

        #AGREGAR BORDE DE DETECCION
        #cv2.rectangle(img,(2*tamanoCelda,2*tamanoCelda),((self.tamanoMatriz+6)*tamanoCelda,(self.tamanoMatriz+6)*tamanoCelda),(0,0,0),-1)
        cv2.rectangle(img,(2*tamanoCelda,2*tamanoCelda),((self.tamanoMatriz+8)*tamanoCelda,(self.tamanoMatriz+8)*tamanoCelda),(0,0,0),-1)
        
        #AGREGAR BORDE DE IMAGEN
        cv2.rectangle(img,(0,0),(699,699),(0,0,0),1)
        
        cv2.rectangle(img,(4*tamanoCelda,4*tamanoCelda),((self.tamanoMatriz+5+1)*tamanoCelda,(self.tamanoMatriz+5+1)*tamanoCelda),(255,255,255),-1)
        
        
        #AGREGAR COLORES DE REFERENCIA
        if self.numColores == 2:
            colReferencia = np.array([0,0,0])
        elif self.numColores == 4:
            colReferencia = np.array([2,3,4])
        elif self.numColores == 8:
            colReferencia = np.array([0,2,3,4,5,6,7])

        for x in range(colReferencia.size):
            ##SUPERIOR
            pt1 = (tamanoCelda*(((x+1)*2)+1+1) , (2+1)*tamanoCelda)
            pt2 = (tamanoCelda*(((x+1)*2)+2+1) , (3+1)*tamanoCelda)
            col = self.Color(colReferencia[x])
            cv2.rectangle(img,pt1,pt2,col,-1)

            ##DERECHA
            pt1 = ((5+1+self.tamanoMatriz)*tamanoCelda,tamanoCelda*(((x+1)*2)+1+1))
            pt2 = ((6+1+self.tamanoMatriz)*tamanoCelda,tamanoCelda*(((x+1)*2)+2+1))
            col = self.Color(colReferencia[x])
            cv2.rectangle(img,pt1,pt2,col,-1)

            ##INFERIOR
            pt1 = (tamanoCelda*((((x+1)*2)+1) + (self.tamanoMatriz+5-(2*colReferencia.size))),(5+1+self.tamanoMatriz)*tamanoCelda)
            pt2 = (tamanoCelda*((((x+1)*2)+1) + (self.tamanoMatriz+4-(2*colReferencia.size))),(6+1+self.tamanoMatriz)*tamanoCelda)
            col = self.Color(colReferencia[x])
            cv2.rectangle(img,pt1,pt2,col,-1)
                
       #cv2.rectangle(img,(3*tamanoCelda,3*tamanoCelda),((self.tamanoMatriz+5)*tamanoCelda,(self.tamanoMatriz+5)*tamanoCelda),(255,255,255),-1)
        cv2.rectangle(img,(4*tamanoCelda,4*tamanoCelda),((self.tamanoMatriz+6)*tamanoCelda,(self.tamanoMatriz+6)*tamanoCelda),(255,255,255),-1) 
       
        for y in range(self.tamanoMatriz):
            for x in range(self.tamanoMatriz):
                pt1=((x+4+1)*tamanoCelda,(y+4+1)*tamanoCelda)
                pt2=((x+5+1)*tamanoCelda,(y+5+1)*tamanoCelda)
                valorCelda = self.arregloColores[(y*self.tamanoMatriz)+x]
                col = self.Color(valorCelda)
                cv2.rectangle(img,pt1,pt2,col,-1)

        #cv2.imshow('image',img)
        nombreImagen = 'Imagen' + str(self.numImagen)+'.png'
        cv2.imwrite(nombreImagen,img)
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Color(self,valorCelda):
        if valorCelda == 0:
            col = (255,255,255)
        elif valorCelda == 1:
            col = (0,0,0)
        elif valorCelda == 2:
            col = (0,0,255)
        elif valorCelda == 3:
            col = (0,255,0)
        elif valorCelda == 4:
            col = (255,0,0)
        elif valorCelda == 5:
            col = (255,0,255)
        elif valorCelda == 6:
            col = (255,255,0)
        elif valorCelda == 7:
            col = (0,255,255)
            
        return col



