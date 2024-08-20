class Jugadores:
    def __init__(self, nombre, nacionalidad, estatura):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__estatura = estatura

    def get_nombre(self):
        nombre = self.__nombre
        return nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        nacionalidad = self.__nacionalidad
        return nacionalidad
    def set_nacionalidad(self,nacionalidad):
        self.__nacionalidad = nacionalidad

    def get_estatura(self):
        estatura = self.__estatura
        return estatura
    def set_estatura(self,estatura):
        self.__estatura = estatura
    

    def __str__(self):
        return "Nombre: "+self.__nombre
    
    def datos_jugador(self):
        txt = f"Nombre: {self.__nombre}"
        txt += f"\nNacionalidad: {self.__nacionalidad}"
        txt += f"\nEstatura: {self.__estatura}"
        return txt