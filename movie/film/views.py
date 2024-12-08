from django.shortcuts import render,redirect
from film.models import Movie
from film.forms import MovieForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

#
# def home(request):
#     m = Movie.objects.all()
#     context = {'movie': m}
#     return render(request,'viewemployee.html',context)


# class based code

class HomeView(ListView):
    model=Movie
    context_object_name = "movie"
    template_name = "viewemployee.html"


    # def get_queryset(self):
    #     queryset=super().get_queryset().filter(title__startswith='T')
    #     return queryset


    # def get_context_data(self,*,object_list=None, **kwargs):
    #     context=super().get_context_data()
    #     context['name']="Arun"
    #     context['age']=24
    #     return context
            # OR
    # extra_context = {'name':'Arun','age':24}

# get_queryset()
# get_context_data()
# extra_context
#




# def addmovie(request):
#     if(request.method=="POST"):
#         t = request.POST['t']
#         d = request.POST['d']
#         l = request.POST['l']
#         y = request.POST['y']
#         i = request.FILES['i']
#
#         m=Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
#         m.save()
#         return redirect('home')
#
#     return render(request,'addmovie.html')

# def add_movie(request):
#     # if request.method=="POST":
#     #     form=MovieForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect("film:home")
#
#
#     form=MovieForm()
#     context={'form':form}
#     return render(request, 'add1.html',context)

class AddMovie(CreateView):
    model = Movie
    form_class = MovieForm
    #       OR
    # fields = ['title', 'description', 'language', 'year', 'image']
    template_name = "add1.html"
    success_url = reverse_lazy('film:home')



# def moviedetails(request,p):
#     m=Movie.objects.get(id=p)
#     context={'movie':m}
#     return render(request, 'moviedetails.html',context)


class MovieDetails(DetailView):
    model=Movie
    context_object_name = "movie"
    template_name = "moviedetails.html"






# def delete(request,p):
#     m=Movie.objects.get(id=p)
#     m.delete()
#     return redirect('home')

# def edit(request,p):
#     m=Movie.objects.get(id=p)  # read a particular record
#
#     if(request.method=="POST"):
#         m.title=request.POST['t']
#         m.description=request.POST['d']
#         m.language=request.POST['l']
#         m.year=request.POST['y']
#         if(request.FILES.get('i')==None):
#             m.save()
#         else:
#             m.image=request.FILES.get('i')
#         return redirect('home')
#
#     context = {'movie':m}
#     return render(request,'edit.html',context)

class UpdateMovie(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "edit.html"
    success_url = reverse_lazy('film:home')
#
#
class DeleteMovie(DeleteView):
    template_name = 'delete.html'
    model=Movie
    success_url = reverse_lazy('home')