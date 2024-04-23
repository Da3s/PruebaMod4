from campaña import Campaña
from anuncio import Video

def main():
    try:
        anuncio_video = Video(20) 
        mi_campaña = Campaña("Mi Campaña", [anuncio_video])

        nuevo_nombre = input("Introduce nombre para la campaña: ")
        nuevo_subtipo = input("Introduce subtipo para el anuncio: ")

        mi_campaña.nombre = nuevo_nombre
        anuncio_video.sub_tipo = nuevo_subtipo

    except Exception as e:
        with open("error.log", "a") as file:
            file.write(str(e))

if __name__ == "__main__":
    main()