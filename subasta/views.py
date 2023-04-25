from django.shortcuts import render
from .algoritmos.accionesFB import *
from .algoritmos.accionesV import *
from .algoritmos.accionesPD1 import *
from .algoritmos.accionesPD2 import *
from .algoritmos.entradaSalida import *
import os


# Create your views here.

def app_inicial(request):
    resultado=[]

    if(request.method=='POST' and request.FILES):
        file = request.FILES['file']
        rutaArchivo = save_file_to_project(file)
        parametros = leerInstrucciones(rutaArchivo)
        A = parametros[0] 
        B = parametros[1]
        n = parametros[2]
        compradores = parametros[3]

        algoritmo = request.POST['algoritmo']

        M = 1

        if algoritmo == 'FB':
            resultado = accionesFB(A,B,n,compradores)

        if algoritmo == 'V':
            resultado = accionesV(A,B,n,compradores)

        if algoritmo == 'D1':
            resultado = accionesPD1(A,B,n,compradores)

        if algoritmo == 'D2':
            M = parametros[4]
            resultado = accionesPD2(A,B,n,compradores,M)
        
        escribirSalida(resultado, file.name, algoritmo)
        print(resultado)

        resultadoDiccionario = {
            'ganancia': resultado[0],
            'asignacion': resultado[1:]
        }

        parametrosDiccionario = {
            'A': A,
            'B': B,
            'n': n,
            'ofertas': compradores 
        }


        return render(request, 'index.html',{'solucion': resultadoDiccionario, 'parametros': parametrosDiccionario, 'M':M, 'algoritmo': algoritmo , 'nombre': file.name , 'isPOST': True})
    
    return render(request, 'index.html', {'isPOST': False})



def save_file_to_project(file):
    # Define la ruta donde deseas guardar el archivo
    directory = 'subasta/archivos/entradas'
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, file.name)
    # Abre el archivo en modo binario
    with open(path, 'wb') as f:
        # Lee los datos del archivo y escríbelos en el archivo nuevo
        for chunk in file.chunks():
            f.write(chunk)
    # Devuelve la ruta completa del archivo guardado
    return os.path.abspath(path)
