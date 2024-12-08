"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from film import views

from django.conf.urls.static import static
from django.conf import settings

app_name='film'
urlpatterns = [
    path('admin/', admin.site.urls),
     # path('',views.home,name="home"),
     # path('addmovie',views.addmovie,name="addmovie"),
     # path('moviedetails/<int:p>',views.moviedetails,name="moviedetails"),
     # path('delete/<int:p>',views.delete,name="delete"),
     # path('edit/<int:p>',views.edit,name="edit"),


    path('',views.HomeView.as_view(),name="home"),
    path('add',views.AddMovie.as_view(),name="addmovie"),

    path('details/<int:pk>', views.MovieDetails.as_view(), name="moviedetails"),

    path('delete/<int:pk>',views.DeleteMovie.as_view(),name="delete"),
    path('edit/<int:pk>',views.UpdateMovie.as_view(),name="edit"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)