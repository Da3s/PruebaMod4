from error import SubTipoInvalidoError
from abc import ABC, abstractmethod

class Anuncio:
    SUB_TIPOS = ()
    
    def __init__(self, alto: int, ancho: int, sub_tipo: str, url_archivo: str, url_click: str):
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__sub_tipo = sub_tipo
        self.__url_archivo = url_archivo
        self.__url_clic = url_click
    
    # todos los getter *************************************************************************
    
    # getter alto    
    @property
    def alto(self):
        return self.__alto
    
    # getter ancho
    @property
    def ancho(self):
        return self.__ancho
    
    # getter sub_tipo    
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
     # getter establecer_url_archivo
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    # getter url_clic
    @property
    def url_clic(self):
        return self.__url_clic
    
    # fin getter *******************************************************************************
    
    # todos los setter
    
    # setter alto
    @alto.setter
    def metodo(self, alto):
        self.__alto = alto if alto > 0 else 1
        
    # setter ancho
    @ancho.setter
    def metodo(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
        
    # setter sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str):
        try:
            if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
                raise SubTipoInvalidoError(f"El subtipo '{sub_tipo}' no es válido para este tipo de anuncio.", sub_tipo)
            else:
                self.__sub_tipo = sub_tipo
        except SubTipoInvalidoError as stie:
            print("Error: {stie}", stie.subtipo)

    # Setter establecer_url_archivo
    @url_archivo.setter
    def url_archivo(self, nueva_url_archivo: str):
        self.__url_archivo = nueva_url_archivo
        
     # setter url_clic
    @url_clic.setter
    def url_clic(self, nueva_url_clic: str):
        self.__url_clic = nueva_url_clic

    # fin de los setter **************************************************************************

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos():
        print("Formato Video:")
        print("****************")
        for video in Video.SUB_TIPOS:
            print(f"- {video}")
        print("Formato Display:")
        print("****************")
        for display in Display.SUB_TIPOS:
            print(f"- {display}")
        print("Formato Social:")
        print("****************")
        for social in Social.SUB_TIPOS:
            print(f"- {social}")

    # establecer_url_archivo
    def establecer_url_archivo(self, nueva_url_archivo: str):
        self.url_archivo = nueva_url_archivo
        
    # establecer_url_clic
    def establecer_url_clic(self, nueva_url_clic: str):
        self.url_clic = nueva_url_clic

# *******************************************************************************
# clase Video

class Video(Anuncio):
    FORMATO = "Video"
    # Tupla video
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, sub_tipo: str, url_archivo: str, url_click: str, duracion: int):
        super().__init__(1, 1, sub_tipo, url_archivo, url_click) 
        self.__duracion = duracion if duracion > 0 else 5
        
    # getter alto    
    @property
    def alto(self):
        return self.__alto
    
    # getter ancho
    @property
    def ancho(self):
        return self.__ancho
    
    # setter alto
    @alto.setter
    def metodo(self, alto):
       pass
        
    # setter ancho
    @ancho.setter
    def metodo(self, ancho):
        pass
        
    # getter duracion
    @property
    def duracion(self):
        return self.__duracion    
        
    # setter duracion
    @duracion.setter
    def duracion(self, duracion: int):
        self.__duracion = duracion if duracion > 0 else 5

    def modificar_duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self.duracion = nueva_duracion
        else:
            self.duracion = 5
            
    def comprimir_anuncio(self):
        print('COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN')

    def redimensionar_anuncio(self):
        print('RECORTE DE VIDEO NO IMPLEMENTADO AÚN')

# *******************************************************************************
# clase Display

class Display(Anuncio):
    FORMATO = "Display"
    # Tupla video
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        print('COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN')

    def redimensionar_anuncio(self):
        print('REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN')

# *******************************************************************************
# clase Social

class Social(Anuncio):
    FORMATO = "Social"
    # Tupla video
    SUB_TIPOS = ("facebook", "linkedin")
    
    def comprimir_anuncio(self):
        print('COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN')

    def redimensionar_anuncio(self):
        print('REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN')
        
        
