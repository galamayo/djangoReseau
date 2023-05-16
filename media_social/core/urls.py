from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('like-post', views.like_post, name='like-post'),
    path('upload', views.upload, name='upload'),
     path('follow', views.follow, name='follow'),
      path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('setting', views.setting, name='setting'),
    path('creationCompte', views.creationCompte, name='creationCompte'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('accueil', views.accueil, name='accueil'),
   
]
