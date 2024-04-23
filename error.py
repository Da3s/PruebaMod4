class SubTipoInvalidoError(Exception):
    def __init__(self, mensaje, subtipo):
        self.mensaje = mensaje
        self.subtipo = subtipo

class LargoExcedidoException(Exception):
    def __init__(self, mensaje="El nombre de la campaña supera los 250 caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class Error(Exception):
    pass