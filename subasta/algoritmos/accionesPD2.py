def accionesPD2(A,B,n,ofertas,M):

    #la matriz está rellena de diccionarios en donde el total indica el total mas optimo para el subproblema que representa esa posicion de la matriz
    # y cantAcciones es la cantidad de acciones que tomo de ese subproblema para llegar a ese total
    matriz = [[{'total': 0, 'cantAcciones':0} for x in range(0,A+1, M)] for y in range(n+1)]
    indice = int(A/M)
    for oferta in range(1, n+1):
        for acciones in range(1, indice+1):

            total = matriz[oferta-1][acciones]['total']
            cantAcciones = 0

            if ofertas[oferta-1][1] < M and acciones == 1:
                total = ofertas[oferta-1][0]
                cantAcciones = 1
            else:

                for accionesTomadas in range(int(ofertas[oferta-1][2]/M), min(acciones, int(ofertas[oferta-1][1]/M))+1):
                    
                    totalMaximo = ofertas[oferta-1][0]*accionesTomadas*M + matriz[oferta-1][acciones-accionesTomadas]['total']
                    
                    if totalMaximo > total:
                        total = totalMaximo
                        cantAcciones = accionesTomadas
                    
            
            matriz[oferta][acciones] = {'total': total, 'cantAcciones':cantAcciones}

    #para encontrar la asignacion optima recorremos la matriz desde el ultimo elemento
    asignacion = []
    oferta = n-1
    accion = indice

    for i in range(n-1, -1, -1):   
        asignacion.insert( 0, matriz[oferta+1][accion]['cantAcciones']*M)
        accion -= int(asignacion[0]/M)
        oferta -= 1



    return [matriz[n][indice]['total']]+asignacion

