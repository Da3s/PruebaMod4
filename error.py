class SubTipoInvalidoException(Exception):
    def __init__(self, mensaje="El subtipo no es válido para este tipo de anuncio."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class LargoExcedidoException(Exception):
    def __init__(self, mensaje="El nombre de la campaña supera los 250 caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class Error(Exception):
    pass