def funcionVR(X, tripleta):
  #calcula la cantidad total recogida por las una asignacion de acciones
  totalAcciones = 0
  for idComprador in range(len(tripleta)):
    pagoXAccion = tripleta[idComprador][0]
    cantAccciones = X[idComprador]
    totalAcciones += cantAccciones * pagoXAccion 

  return totalAcciones

def accionesFB(A, B, n, tripleta):

  valores = [i[1] for i in tripleta]
  soluciones = []

  for i in range(1, 2**n,2):
  
    binario = bin(i)[2:].zfill(n)
    suma = 0
    asignacionDeAcciones = []

    #hacemos un for de n-1 porque el ultimo valor respresenta al gobierno, el cual se calcula diferente: A- sum(las acciones compradas por los otros compradores)
    for j in range(n-1):
        if binario[j] == '1':
            #suma las acciones que se van dando sin contar la del gobierno y las concatena a combinacion
            suma += valores[j]
            asignacionDeAcciones.append(valores[j])
        else:
            #si en la combinacion que se esta evaluando hay un 0, esas acciones de ese comprador no se tienen en cuenta por lo tanto ponemos 0 indicando que no vamos a tomar ninguna accion de ese comprador
            asignacionDeAcciones.append(0)

    #recordar que suma tiene solo la cantidad de acciones dadas a todos los compradores sin contar la del gobierno
    
    if suma <= A :
        #este if va a agregar solo las combinaciones que si son posibles para el problema y añade al final de la combinacion lo que le corresponde al gobierno
        valor = A - suma
        asignacionDeAcciones.append(valor)
        #cuando la asignacion de acciones está lista se agrega a la lista de las posibles soluciones
        soluciones.append(asignacionDeAcciones)

  #Aqui empieza el codigo para encontrar la maxima asignacion de acciones
  totalMaximo = 0
  for solucion in soluciones:
     #a cada posible solucion le calculo su ganancia
     total = funcionVR(solucion, tripleta)
     #encuentra la mayor ganancia y guarda la x que genera esa ganancia
     if total > totalMaximo:
        totalMaximo = total
        asignacionMaxima = solucion

  #devuelve una lista donde el primer valor es la ganancia y el resto es la asignacion de las acciones 
  respuesta = [totalMaximo]+asignacionMaxima
  
  return respuesta

                                            

                                    


