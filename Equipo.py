class Equipo:
    def __init__(self, nombre:str, ciudad:str, campeonatos:int, sponsor:str):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__campeonatos = campeonatos
        self.__sponsor = sponsor
        self.__jugadores = []

    def get_nombre(self):
        nombre = self.__nombre
        return nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_ciudad(self):
        ciudad = self.__ciudad
        return ciudad
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    
    def get_campeonatos(self):
        campeonatos = self.__campeonatos
        return campeonatos
    def set_campeonatos(self,campeonatos):
        self.__campeonatos = campeonatos

    def get_sponsor(self):
        sponsor = self.__sponsor
        return sponsor
    def set_sponsor(self,sponsor):
        self.__sponsor = sponsor

    #carga masiva inicial
    def get_jugadores(self):
        jugadores = self.__jugadores
        return jugadores
    def set_jugadores(self,jugadores):
        self.__jugadores = jugadores

    
    def __str__(self):
        return "Nombre: "+self.__nombre
    
    def mostrar_datos(self):
        txt = f"Nombre: {self.__nombre}"
        txt += f"\nCiudad: {self.__ciudad}"
        txt += f"\nCampeonatos: {self.__campeonatos}"
        txt += f"\nSponsor: {self.__sponsor}"
        txt += f"\nJugadores: {self.__jugadores}"
        return txt
    
    def contratar_jugador(self, jugador):
        if jugador in self.__jugadores:
            print("El jugador ya esta en el equipo")
        else:
            self.__jugadores.append(jugador)
    
    def despedir_jugador(self, jugador):
        if jugador not in self.__jugadores:
            print("El jugador no esta en el equipo")
        else:
            self.__jugadores.remove(jugador)