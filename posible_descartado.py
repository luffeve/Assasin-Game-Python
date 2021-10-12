#pueden_enfrentarse: String String String Integer --> Boolean
#recibe dos jugadores y un numero que representara la distancia maxima permitida
#para que dos jugadores se puedan enfrentar luego retornara True en caso que los jugadores
#cumplan las condiciones para poder enfrentarse, sino devolvera False.
def pueden_enfrentarse(jugador1, jugador2, distancias_join, distancia_maxima):
    ciudadJ1 = jugador1.split(',')[2]
    ciudadJ2 = jugador2.split(',')[2]

    distancia_entre_jugadores = distancia(jugador1, jugador2, distancias_join)
    if (jugador1==jugador2):
        return False
    else:
        return ((ciudadJ1==ciudadJ2) or (float(distancia_entre_jugadores)<=float(distancia_maxima)))

def test_pueden_enfrentarse():
    distancias_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests", "distancias_test.txt")
    assert pueden_enfrentarse("GASTON MORICONI,23,Cordoba","LORENZO RE,21,Rosario", distancias_join,300) == False
    assert pueden_enfrentarse("GASTON MORICONI,23,Cordoba","LORENZO RE,21,Rosario", distancias_join,500) == True
    assert pueden_enfrentarse("JOSE LOPEZ,40,CABA","JUAN GARAY,43,CABA", distancias_join,100) == True
    assert pueden_enfrentarse("MARIA GONZALEZ,50,CABA","LUCIA SANCHEZ,26,Rosario", distancias_join,200) == False