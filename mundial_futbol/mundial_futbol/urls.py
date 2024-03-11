from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('login/', views.login_view, name='login'),
    path('sing_up.html', views.Sing_up, name='sing_up'),
    path('equipos/', views.equipos, name='equipos'),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('edit_equipos/<int:id>/', views.edit_equipos, name='edit_equipos'),
    path('delete_equipo/<int:id>/', views.delete_equipo, name='delete_equipo'),
    path('edit_jugador/<int:id>/', views.edit_jugador, name='edit_jugador'),
    path('delete_jugador/<int:id>/', views.delete_jugador, name='delete_jugador'),
    path('posiciones/', views.posiciones, name='posiciones'),
    path('edit_position/<int:id>/', views.edit_posicion, name='edit_posicion'),
    path('delete_posicion/<int:id>/', views.delete_posicion, name='delete_posicion'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('edit_tecnico/<int:id>/', views.edit_tecnico, name='edit_tecnico'),
    path('delete_tecnico/<int:id>/', views.delete_tecnico, name='delete_tecnico'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)