# capa de servicio/lógica de negocio

from ..transport import transport
from ..dao import repositories
from ..generic import mapper
from django.contrib.auth import get_user

def getAllImages(input=None):
    # obtiene un listado de imágenes desde transport.py y lo guarda en un json_collection.
    # ¡OJO! el parámetro 'input' indica si se debe buscar por un valor introducido en el buscador.
    json_collection = transport.getAllImages(input)

    images = []

    # recorre el listado de objetos JSON, lo transforma en una NASACard y lo agrega en el listado de images. Ayuda: ver mapper.py.
    for obj in json_collection:
<<<<<<< HEAD
        image = mapper.fromRequestIntoNASACard(obj)
        images.append(image)

=======
        image = mapper.fromRepositoryIntoNASACard(obj)
        images.append(image)
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
    return images
    
     # recorre el listado de objetos JSON, lo transforma en una NASACard y lo agrega en el listado de images. Ayuda: ver mapper.py.

   


def getImagesBySearchInputLike(input):
    return getAllImages(input)


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
<<<<<<< HEAD
    fav =  mapper.fromTemplateIntoNASACard(request) # transformamos un request del template en una NASACard.
    
    fav.user = get_user(request) # le seteamos el usuario correspondiente.
    
=======
    fav = mapper.fromTemplateIntoNASACard(request) # transformamos un request del template en una NASACard.
    fav.user = get_user(request) # le seteamos el usuario correspondiente.
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a

    return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados en el template 'favourites.html'
def getAllFavouritesByUser(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = repositories.getAllFavouritesByUser(user) # buscamos desde el repositorio TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
<<<<<<< HEAD
            nasa_card = mapper.fromRepositoryIntoNASACard(favourite)# transformamos cada favorito en una NASACard, y lo almacenamos en nasa_card.
=======
            nasa_card = mapper.fromRepositoryIntoNASACard(favourite) # transformamos cada favorito en una NASACard, y lo almacenamos en nasa_card.
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
            mapped_favourites.append(nasa_card)

        return mapped_favourites


def deleteFavourite(request):
    #favId = request.POST.get('id')
    #return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
<<<<<<< HEAD

=======
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId)
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
