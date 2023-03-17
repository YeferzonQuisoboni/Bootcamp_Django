from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City, Comment

from .forms import CommentForm

#import libreria de todos los paises

# Create your views here.
def index(request):
    cities = City.objects.all()

    return render(request, 'cities.html', {'cities':cities})


def get_city(request, id):
    city = City.objects.get(id=id)

    comments = Comment.objects.filter(city=id) # 3. se trae los comentarios (objetos) de la ciudad que corresponda al id de la idad que se recibe por parametro

    comment_form = CommentForm() # 1 Se crea instacia de CommentForm()

    return render(request, 'city.html', {'city':city, 'form':comment_form, 'comments': comments})

def create_new_comment(request, id): # 2. Se creo function create_new_comment()
    if request.method == 'POST':

        form = CommentForm(request.POST) #Genera instancia del modelo CommentForm y la guarda en form

        if form.is_valid():
            new_comment =  form.save(commit=False) #Guardar comentario
            new_comment.user = request.user #se obtiene usuario del request
            new_comment.city = City.objects.get(id=id) # Se obtiene la ciudad desde e modelo ciudad
            new_comment.save() #Guardar comentario en la BD
        
        return redirect('city', id=id)
    else:
        return redirect('city', id=id)



