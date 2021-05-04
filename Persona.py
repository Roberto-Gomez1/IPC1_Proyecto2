#PARA NO PERDER LA REFERENCIA A JAVA USAMOS CLASES
class Persona:
    # NUESTRO NUEVO CONSTRUCTO
    # __init__ sera nuestro metodo que se ejecuta al crear un objeto
    # self, hace referencia al objeto actual    
    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getUsuario(self):
        return self.usuario
    
    def getContraseña(self):
        return self.contraseña


    # METODOS SET
    # Creamos nuestros metodos para setear la informacion, usando el self y el parametro
    def setUsuario(self, usuario):
        self.usuario = usuario
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
