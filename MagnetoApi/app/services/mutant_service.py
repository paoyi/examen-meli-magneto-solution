from .split_string import SplitString
from ..models.base_adn import BaseAdn

class MutantService:
    def __init__(self):
        print("instancia creada de MutantService")

    def Is_mutant(self, dna):
        count = 0
        matrix = self.__Convert_to_matrix(dna)
        for sequence in BaseAdn:
            if(self.__Iterator_initial(sequence,matrix)):
                count+=1
        if(count>1):
            return True
        else:
            return False

    def __Convert_to_matrix(self, dna): 
        matrixResult = []
        ss = SplitString()
        for word in dna:
            arr = ss.split(word)
            matrixResult.append(arr)
        return matrixResult
                    

    def __Iterator_initial(self, sequence,matrix):
        size = len(matrix[0]) 
        for i in range(0,size):	
            for j in range(0,size):
                if (sequence[0] == matrix[i][j]):
                    finish=self.__Options_iterator(matrix,i,j,sequence)	
                    if (finish==True):	
                        return finish

    def __Options_iterator(self,matrix,i,j,sequence):
        typesOfSearch = {
            1:"forma Horizontal",
            2:"forma Vertical",
            3:"forma Diagonal Inferior Izquierda",
            4:"forma Diagonal Inferior Derecha"
        }
        newword=sequence[1:]  #quitamos la letra inicial de la secuencia
        for x in range(1,5):  #recorremos las 4 formas de busqueda
            validationResult=self.__Options_search(x,i,j,matrix,newword)	#llamamos la recursion
            if (validationResult==True):	#si es verdadero, signifia que se hallo la palabra
                print("La secuencia {0} esta ubicada en la posicion ({1},{2}) {3}".format(sequence,i+1,j+1,typesOfSearch[x]))	#imprimimos el mensaje
                return validationResult	#retornamos que la encontramos, para evitar que se siga con las demas posibles formas de hallarla
			

    def __Options_search(self,op,i,j,matrix,sequence):
        if len(sequence)==0:	#solo cuando la funcion llege a la ultima letra, se detendra la recursion
            result=True	
            return result
        else:	#esta sera la  recursiva, para las cuatro posibles maneras de hallar la secuencia
            if (op==1):	#manera 1
                i=i
                j=j+1
            elif (op==2): #manera 2
                i=i+1
                j=j
            elif (op==3): #manera 3
                i=i+1
                j=j-1
            elif (op==4): #manera 4
                i=i+1
                j=j+1

            try:	
                if matrix[i][j]==sequence[0]:
                    nueva=sequence[1:]
                    a=self.__Options_search(op,i,j,matrix,nueva)	
                    if a==True:
                        return a
                else:
                    result=False
                    return result
            except:
                result=False
                return result