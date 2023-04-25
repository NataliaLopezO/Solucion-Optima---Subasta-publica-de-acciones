def funcionVR(X, tripleta):
  #calcula la cantidad total recogida por las una asignacion de acciones
  totalAcciones = 0
  for idComprador in range(len(tripleta)):
    pagoXAccion = tripleta[idComprador][0]
    cantAccciones = X[idComprador]
    totalAcciones += cantAccciones * pagoXAccion 

  return totalAcciones

def accionesV(A,B,n,compradores):
  cantidadMinComprador = [i[2] for i in compradores]
  cantidadMaxComprador = [i[1] for i in compradores]
  accionesVenta = A
  asignacionAcciones = []

  for i in range(n):
      j = min(accionesVenta, cantidadMaxComprador[i])
      if j >= cantidadMinComprador[i]:
          asignacionAcciones.append(j)
          accionesVenta -= j
          if accionesVenta == 0:
            break
      else:
          asignacionAcciones.append(0)

  asignacionAcciones.extend([0]*(n-len(asignacionAcciones)))
  precioTotal = funcionVR(asignacionAcciones, compradores)
  respuesta = [precioTotal]+asignacionAcciones

  return respuesta

