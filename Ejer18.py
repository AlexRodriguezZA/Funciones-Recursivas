#Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
matriz = [[1, 2, 3], #0
          [6, 7, 8], #1
          [11, 12, 13]] #2
           #0  #1  #2  
           
def RecorrerMatriz(mat,x,y):
    if (x<=len(mat)-1):
        print(mat[x][y])
        if (y==len(mat)-1):
            return(RecorrerMatriz(mat,x+1,y-(len(mat)-1)))    
        else:
            return RecorrerMatriz(mat,x,y+1)

print(RecorrerMatriz(matriz,0,0))