#Participantes: Gaston Moriconi - Lorenzo Re

import os              # Para manejar archivos en distintos sistemas operativos.
from random import *   # Para usar funciones de la libreria random.



#categoria: String Char -> [String]
#Descripcion: Esta funcion recibe la direccion de un archivo cuyo contenido
#va a ser una lista de jugadores, y un caracter('+' para MAYORES DE EDAD o '-' PARA MENORES DE EDAD).
#Luego retorna una lista con aquellos jugadores pertenecientes a la categoria deseada.

def categoria (jugadores_join, categoria):
    jugadores=open(jugadores_join, "r")     #Abro el archivo de jugadores en modo lectura
    jugadores_categoria=[]                  #Lista de jugadores a retornar

    if categoria == '+': #Si deseo lista de mayores
        for linea in jugadores.readlines():         #Recorro el archivo linea por linea
            edad_jugador = (linea.split(','))[1]    #Para saber la edad del jugador
            if edad_jugador >= '18': #Entonces es mayor de edad y lo agrego a la lista
                jugadores_categoria.append(linea[0:-1] if linea[-1] == "\n" else linea) #Al leer linea por linea todas menos la ultima
                                                                                        #tienen un salto de linea("\n") que hay que sacar.
    else: #Entonces deseo los menores de edad
        for linea in jugadores.readlines():
            edad_jugador = (linea.split(','))[1]
            if edad_jugador < '18':
                jugadores_categoria.append(linea[0:-1] if linea[-1]=="\n" else linea)

    jugadores.close() #Cierro el archivo 
    return jugadores_categoria #Y retorno la lista de jugadores pertenecientes a la categoria deseada        



#Para testear esta funcion usaremos unos archivos creados por el equipo donde uno contendra 4 personas
#de las cuales dos seran mayores de edad y dos seran menores. El otro sera un archivo vacio.

def test_categoria():
    jugadores_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "jugadores_test.txt")
    jugadoresV2_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "jugadoresV2_test.txt")
    assert categoria(jugadores_join, '+') == ["GASTON MORICONI,23,Cruz Alta", "LORENZO RE,22,Rosario"]
    assert categoria(jugadores_join, '-') == ["AGUSTINA LOPEZ,17,Rosario","CAMILA GARCIA,16,CABA"]
    assert categoria(jugadoresV2_join, '+') == []
    assert categoria(jugadoresV2_join, '-') == []



#distancias: String -> [String]
#Definicion: Lee un archivo y retorna las lineas del mismo, en este caso se utiliza para 
#obtener las distancias entre ciudades

def distancias(distancias_join):
    distancias = open(distancias_join,"r")  #Abro el archivo en modo lectura
    ciudades = []                           #Defino una lista vacia
    for linea in distancias.readlines():    #Luego recorro el archivo            
        ciudades.append(linea[0:-1] if linea[-1]=="\n" else linea) #Y agrego la distancia a la lista quitando el salto
                                                                    #de linea.

    return ciudades



#Para testear la funcion distancias utilizaremos un archivo donde solo exiten dos distancias

def test_distancias():
    distancias_join = os.path.join(os.path.dirname(os.path.abspath(__file__)),"tests","distancias_test_V2.txt")
    assert distancias(distancias_join) == ["CABA, Rosario, 299.9", "CABA, Santa Fe, 468.5"]



#distancia_entre_jugadores: String String String-> String
#definicion: Recibe dos jugadores y un archivo de distancias, luego devuelve la distancia entre los jugadores
#ingresados

def distancia_entre_jugadores(jugador1, jugador2, distancias_join):
    distancias=open(distancias_join, "r")   #Abro el archivo de distancias en modo lectura
    ciudadJ1=(jugador1.split(','))[2]       #Del jugador 1, me quedo con su ciudad
    ciudadJ2=(jugador2.split(','))[2]       #Del jugador 2, me quedo con su ciudad

    for linea in distancias.readlines():    #Por cada linea
        linea=linea[0:-1] if linea[-1]=="\n" else linea #Para sacar el salto de linea cuando sea necesario
        if (ciudadJ1 in linea) and (ciudadJ2 in linea):#Si en la linea leida estan las ciudades de ambos jugadores
            distancias.close()                          #Entonces termine con la busqueda y cierrro el archivo
            return linea.split(',')[2]                  #Luego retorno su distancia



#Test para la funcion distancia donde distancias_join toma un archivo creado por el equipo
#donde se encuentran algunas distancias.

def test_distancia_entre_jugadores():
    distancias_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "distancias_test.txt")
    assert distancia_entre_jugadores("GASTON MORICONI,23,Cordoba","LORENZO RE,22,Rosario", distancias_join) == " 400.9"
    assert distancia_entre_jugadores("JOSE LOPEZ,40,CABA","JUAN GARCIA,45,Rosario", distancias_join) == " 299.9"



#asignar_rival: String [[String]] String Integer-> String
#Descripcion: Toma un jugador, una lista de jugadores, un archivo de distancias y la distancia
#maxima permitida para que dos jugadores puedan enfrentarse.
#Luego le asigna un rival al jugador ingresado y lo retorna

def asignar_rival(jugador, jugadores_lista, distancias_join, distancia_maxima):

    ciudad_jugador=jugador.split(',')[2] #Para saber la ciudad del jugador
    #posibles_rivales contendra aquellos jugadores que sean de la misma ciudad que jugador
    posibles_rivales=list(filter(lambda ciudad:ciudad.split(',')[2]==ciudad_jugador, jugadores_lista))
    #posibles_rivales=[ciudad for ciudad in jugadores_lista if ciudad.split(',')[2]==ciudad_jugador] #Alrededor de 30% más rápida
    #que la que esta comentada arriba. Seguramente se pueda implementar algo más rápido pero no estoy muy seguro como. 

    if jugador in posibles_rivales:     #Para que no haga una asignacion con el propio jugador
        posibles_rivales.remove(jugador) 


    if (len(posibles_rivales) !=0):     #Si la lista de posibles rivales no es vacia
        return choice(posibles_rivales) #retorna un rival al azar.
    else: #Entonces no hay jugadores en la misma ciudad y habra que buscarle al mas cercano
        ciudades_distancias = distancias(distancias_join)
        #posibles_ciudades sera una lista cuyo contenido seran las ciudades que debera ser el rival para 
        #poder enfrentarse al jugador
        posibles_ciudades=list(filter(lambda distancia:float(distancia.split(',')[2])<=float(distancia_maxima) and 
        (ciudad_jugador in distancia.split(',')[0] or ciudad_jugador in distancia.split(',')[1]), ciudades_distancias))

        if(len(posibles_ciudades)!=0):
            for posible_rival in jugadores_lista: #Recorro la lista de jugadores
                posible_rival_ciudad = posible_rival.split(',')[2] #Para saber la ciudad del jugador que estoy leyendo
                for ciudad in posibles_ciudades:    #Por cada ciudad en las posibles ciudades
                    if posible_rival_ciudad in ciudad: #Si la ciudad del posible rival se encuentra en posibles ciudades
                        posibles_rivales.append(posible_rival)#Entonces es un posible rival valido
                        break   #Para no seguir buscando una vez encontrada la ciudad

            if jugador in posibles_rivales:
                posibles_rivales.remove(jugador) 
            
            #Para ordenar a los jugadores por distancias y asignarle el rival mas cercano
            for i in range (0, len(posibles_rivales)):
	            for j in range (0, len(posibles_rivales)):
		            if distancia_entre_jugadores(jugador, posibles_rivales[j], distancias_join) >= distancia_entre_jugadores(jugador, posibles_rivales[i], distancias_join):
			            aux=posibles_rivales[i]
			            posibles_rivales[i]=posibles_rivales[j]
			            posibles_rivales[j]=aux

            #Luego recorre la lista para asegurarse de no asignarle un rival
            #donde haya mas jugadores en la ciudad del mismo.
            for posible_rival in posibles_rivales:
                ciudad_rival = posible_rival.split(',')[2]
                if not(jugadores_por_ciudad(posibles_rivales, ciudad_rival)>1):#Si no hay mas jugadores en la ciudad del rival
                    return posible_rival #Entonces lo retorno

            return jugador #Si sale del ultimo bucle entonces ya no hay rivales y retorno el mismo jugador

        
        else:
            return jugador



#es_numero: char -> Boolean 
#Descripcion: Recibe una cadena de caracteres y devuelve True si es numerico o si lo puede convertir a numerico,
#sino retornara False

def es_numero(char):
    try:
        float(char)
        return True
    except ValueError:
        return False

def test_es_numero():
    assert es_numero("hola") == False
    assert es_numero("245j") == False
    assert es_numero("245") == True
    assert es_numero(455) == True       



#jugadores_por_ciudad: [[String]] String -> Integer
#toma una lista de jugadores y una ciudad, luego retorna cuantos jugadores hay en dicha ciudad

def jugadores_por_ciudad(jugadores, ciudad):
    cantidad=0
    for jugador in jugadores:
        ciudad_jugador = jugador.split(',')[2]
        if (ciudad in ciudad_jugador): 
            cantidad+=1

    return cantidad

def test_jugadores_por_ciudad():
    assert jugadores_por_ciudad(["GASTON MORICONI, 23, Cordoba", "LORENZO RE, 22, Rosario"], "Rosario") == 1
    assert jugadores_por_ciudad(["GASTON MORICONI, 23, Cordoba", "LORENZO RE, 22, Rosario"], "Cordoba") == 1
    assert jugadores_por_ciudad(["GASTON MORICONI, 23, Cordoba", "LORENZO RE, 22, Rosario"], "CABA") == 0
    assert jugadores_por_ciudad([], "Rosario") == 0



# comenzar_juego: None -> None
#Definicion: Pide los datos de entrada y luego ejecuta las funciones que llevan adelante el juego

def comenzar_juego():

    #--------------PIDO LOS DATOS DE ENTRADA------------------
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))          # Para mantener una compatibilidad entre S.O.
    while True:                                                       # Hasta que ingrese un archivo de jugadores valido
        jugadores_nombre = input("Ingrese el nombre del archivo de jugadores: ")
        jugadores_join = os.path.join(THIS_FOLDER, jugadores_nombre)
        if os.path.isfile(jugadores_join):
            break                                                     
    while True:                                                       # Hasta que ingrese un archivo de distancias valido 
        distancias_nombre = input("Ingrese el nombre del archivo de distancias: ")
        distancias_join = os.path.join(THIS_FOLDER, distancias_nombre)
        if os.path.isfile(distancias_join):
            break

    while True:                                                       # Hasta que ingrese un valor valido para distancia
        distancia_permitida = input("Ingrese la distancia maxima permitida: ")
        if es_numero(distancia_permitida):
            break  
    
    jugadores_mayores = categoria(jugadores_join, '+')                #Para obtener los mayores de edad
    jugadores_menores = categoria(jugadores_join, '-')                #Para obtener los menores de edad

    #Para llevar adelante los enfrentamientos
    proceso_batallas(jugadores_mayores, distancias_join, distancia_permitida)
    proceso_batallas(jugadores_menores, distancias_join, distancia_permitida, "resultados.txt")
    
    print("El juego ha terminado y los resultados han sido guardados")



#proceso_batallas: String String Float String -> None
#Esta funcion recibe una lista de jugadores, la direccion del archivo de distancias y la distancia maxima
#permitida y se encarga de hacer los enfrentamientos y luego escribir el archivo de salida cuyo nombre sera ingresado tambien 
#como parametro

def proceso_batallas(jugadores, distancias_join, distancia_maxima, resultados_join=""):
    if (resultados_join==""): #Entonces se creara y abrira para escritura
        resultados = open("resultados.txt", "w")
        resultados.write("JUGADORES MAYORES\n")
    else: #Entonces se abrira para escribir al final del archivo
        resultados = open("resultados.txt", "a")
        resultados.write("\nJUGADORES MENORES\n")

    ganadores_regionales=[]         #Para almacenar a los ganadores regionales
    while len(jugadores)>1:         #Mientras haya jugadores para enfrentar
        jugador1=choice(jugadores)#Selecciono el jugador1 al azar
        jugador2=asignar_rival(jugador1, jugadores, distancias_join, distancia_maxima) #Le asigno un rival
        
        if (jugador1==jugador2): #Entonces no se le puede asignar un contrincante
            ganador=jugador1    #Y es ganador en su zona
            nombre_ganador=ganador.split(',')[0]
            jugadores.remove(ganador) #Para borrarlo de la lista de jugadores
            ganadores_regionales.append(nombre_ganador) #Para luego escribirlo en el archivo

        else:
            ganador = choice([jugador1, jugador2]) #Elijo un ganador al azar
            #obtengo sus nombres para escribir el archivo
            nombre_ganador=ganador.split(',')[0]
            if (ganador == jugador1):
                nombre_perdedor = jugador2.split(',')[0]
                jugadores.remove(jugador2)
                resultados.write(nombre_ganador.title()+ " ELIMINO A " +nombre_perdedor.title()+"\n")
            else: #entonces el ganador es jugador2
                nombre_perdedor = jugador1.split(',')[0]
                jugadores.remove(jugador1)
                resultados.write(nombre_ganador.title()+ " ELIMINO A " +nombre_perdedor.title()+"\n")

    #Luego escribo la informacion del ganador o ganadores
    if(len(ganadores_regionales)>=1):
        for jugador in ganadores_regionales:
            resultados.write(jugador+" Es el ganador en su region\n")

        for jugador in jugadores:
            nombre_jugador = jugador.split(',')[0]
            resultados.write(nombre_jugador+" Es el ganador en su region\n")
    else:#Entonces hay un unico ganador
        ganador_final = jugadores[0]
        nombre_ganador_final = ganador_final.split(',')[0]
        resultados.write(nombre_ganador_final+" ES EL UNICO GANADOR\n")

    resultados.close()



if __name__ == "__main__":
   comenzar_juego()