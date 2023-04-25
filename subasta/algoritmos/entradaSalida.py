import os

def leerInstrucciones(nombreArchivo):
  aux = []

  with open(nombreArchivo, "r") as archivo:
    lineas = archivo.readlines()
    aux = []
    for linea in lineas:    
      if(linea[-1]=="\n"):
        nuevalinea = linea[:len(linea)-1]
        aux.append(nuevalinea)
      else:
        aux.append(linea)

    A = int(aux[0])
    B = int(aux[1])
    n = int(aux[2])
    compradores = []

    #procesar las tuplas
    for comprador in range(0,n):
      tripleta = [int(i) for i in aux[3+comprador].split(',')]
      compradores.append(tripleta)

    if n+4 == len(aux) :
      M = int(aux[n+3])
      return A, B, n, compradores, M

  return A, B, n, compradores


def escribirSalida(salidas, nombre, algoritmo):
  path = os.path.join("subasta/archivos/salidas", "salida_"+algoritmo+"_"+nombre+".txt")
  archivo = open(path, "w")
  
  for salida in salidas:
    archivo.write(str(salida)+"\n")

  archivo.close()
