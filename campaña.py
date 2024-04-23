from anuncio import Video, Display, Social

class Campaña:
    def __init__(self, nombre, anuncios):
        self.nombre = nombre
        self.anuncios = anuncios

    def __str__(self):
        anuncios_por_tipo = self.contar_anuncios()
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {anuncios_por_tipo}"

    def contar_anuncios(self):
        contador = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self.anuncios:
            if isinstance(anuncio, Video):
                contador["Video"] += 1
            elif isinstance(anuncio, Display):
                contador["Display"] += 1
            elif isinstance(anuncio, Social):
                contador["Social"] += 1
        return ", ".join([f"{value} {key}" for key, value in contador.items()])
