def accionesPD1(A,B,n,ofertas):

    #la matriz está rellena de diccionarios en donde el total indica el total mas optimo para el subproblema que representa esa posicion de la matriz
    # y cantAcciones es la cantidad de acciones que tomo de ese subproblema para llegar a ese total
    matriz = [[{'total': 0, 'cantAcciones':0} for x in range(A+1)] for y in range(n+1)]

    for oferta in range(1, n+1):
        for acciones in range(1, A+1):

            total = matriz[oferta-1][acciones]['total']
            cantAcciones = 0

            for accionesTomadas in range(ofertas[oferta-1][2], min(acciones, ofertas[oferta-1][1])+1):
                
                totalMaximo = ofertas[oferta-1][0]*accionesTomadas + matriz[oferta-1][acciones-accionesTomadas]['total']
                
                if totalMaximo > total:
                    total = totalMaximo
                    cantAcciones = accionesTomadas 

            matriz[oferta][acciones] = {'total': total, 'cantAcciones':cantAcciones}

    #para encontrar la asignacion optima recorremos la matriz desde el ultimo elemento
    asignacion = []
    oferta = n-1
    accion = A

    for i in range(n-1, -1, -1):   
        asignacion.insert( 0,matriz[oferta+1][accion]['cantAcciones'])
        accion -= asignacion[0]
        oferta -= 1



    return [matriz[n][A]['total']]+asignacion


