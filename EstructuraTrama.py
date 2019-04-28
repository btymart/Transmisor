import numpy as np
import math
import crc16
import random

class EstructuraTrama:
        def __init__(self,numeroTramas,numeroTrama,BitsPorTrama,longitudCU,cargaUtil):
                
            self.numeroTramas = self.aBinario(numeroTramas,8)
            self.numeroTrama = self.aBinario(numeroTrama,8)
            self.cargaUtil = cargaUtil
            self.longitudCU = self.aBinario(cargaUtil.size,longitudCU)
            self.bitsRelleno = BitsPorTrama-cargaUtil.size
            self.CRC = self.aBinario(crc16.crc16xmodem(self.cargaUtil),16)

            print('Tramas: ',self.numeroTramas.size, self.numeroTramas)
            print('Numero de trama: ',self.numeroTrama.size,self.numeroTrama)
            print('Longitud carga util: ',self.longitudCU.size,self.longitudCU)
            print('Carga util: ',self.cargaUtil.size)
            print('Relleno: ',self.bitsRelleno)
            print('CRC: ', self.CRC.size,self.CRC,type(self.CRC),self.CRC.dtype)
            
        def aBinario(self,numero,nbits):
            nb = '{0:0'+str(nbits)+'b}'
            nb = nb.format(numero)
            nb = list(nb)
            nb = np.array(nb)
            nb = nb.astype(int)
            return nb

        def getTrama(self):
                if self.bitsRelleno > 0:
                        relleno = [random.randint(0,1) for _ in range(self.bitsRelleno)]
                        relleno = np.array(relleno)

                        trama = np.concatenate((self.numeroTramas,
                                                self.numeroTrama,
                                                self.longitudCU,
                                                self.cargaUtil,
                                                relleno,
                                                self.CRC), axis=None)
                else:
                        trama = np.concatenate((self.numeroTramas,
                                                self.numeroTrama,
                                                self.longitudCU,
                                                self.cargaUtil,
                                                self.CRC), axis=None)
                    
                return trama
                    
                    
            
            
