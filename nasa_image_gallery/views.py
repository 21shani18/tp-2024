# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')
def login_page(request):
<<<<<<< HEAD
        return render(request, 'registration/login.html')


# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
   
   images = services_nasa_image_gallery.getAllImages()
   
   
   favourite_list = services_nasa_image_gallery.getAllFavouritesByUser(request)if request.user.is_authenticated else[]

   return images, favourite_list   
=======
    return render(request, 'registration/login.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages
    favourite_list = services_nasa_image_gallery.getAllFavouritesByUser(request) if request.user.is_authenticated else [] 
    return images, favourite_list
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a


# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
<<<<<<< HEAD
   
    
    images,favourite_list=getAllImagesAndFavouriteList(request)

=======
    images,favourite_list=getAllImagesAndFavouriteList(request)
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )


# función utilizada en el buscador.
def search(request):
<<<<<<< HEAD
 # Obtén el mensaje de búsqueda del POST request  
     images, favourite_list = getAllImagesAndFavouriteList(request)
     search_msg = request.POST.get('query', '')
    

=======
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')
    if not search_msg:
        return redirect('nombre_de_la_url_a_dirigir')
    filtered_images = [image for image in images if search_msg.lower() in image.title.lower()]
    return render (request,'search_results.html', {'images':filtered_images})
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.
     
    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.
     if not search_msg:
        return redirect('nombre_de_la_url_a_redirigir')
     filtered_images = [image for image in images if search_msg.lower() in image.title.lower()]
     return render(request, 'search_results.html', {'images': filtered_images})

   

# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = services_nasa_image_gallery.getAllFavouritesByUser(request)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    services_nasa_image_gallery.saveFavourite(request)
    return redirect('home')


@login_required
def deleteFavourite(request):
    services_nasa_image_gallery.deleteFavourite(request)
    return redirect('favoritos')


@login_required
def exit(request):
    logout(request)
<<<<<<< HEAD
    return redirect('home')
=======
    return redirect ('home')
>>>>>>> 9db2d5d53ab831c73b86cc1f11b1ec1a00228d2a
