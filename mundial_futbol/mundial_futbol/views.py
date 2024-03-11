from core.models import Equipo, Jugador, Position, tecnico
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404


def Index(request):
    return render(request,'index.html',{
        #context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def Sing_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pasword')
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('index')
        
    return render(request, 'sing_up.html',{
        
    })

def equipos(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        flag = request.FILES['bandera']
        shield = request.FILES['escudo']
        team = Equipo(name=name, flag=flag, shield=shield)
        team.save()
        return redirect('equipos')

    equipo = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipo': equipo})

def jugadores(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        photo = request.FILES.get('photo')
        birthday = request.POST.get('birthday')
        number = request.POST.get('number')
        holder = request.POST.get('titular')
        equipo_id = request.POST.get('equipo')
        position_id = request.POST.get('position')
        jugador = Jugador(name=name, surname=surname, photo=photo, birthday=birthday, number=number, holder=holder, Equipo_id=equipo_id, Position_id=position_id)
        jugador.save()
        return redirect('jugadores')

    posicion = Position.objects.all()
    equipo = Equipo.objects.all()
    jugador = Jugador.objects.all()
    return render(request, 'jugadores.html', {'equipo': equipo , 'jugador': jugador, 'posicion':posicion})


def edit_equipos(request, id):
    equipo = Equipo.objects.get(pk= id)
    if request.method == 'POST':
        equipo.name = request.POST['name']
        flag = request.FILES.get('flag')
        shield = request.FILES.get('shield')
        
        if flag:
            equipo.flag = flag
            if shield:
                equipo.shield = shield
            return redirect('equipos')
        
        equipo.save()
        return redirect('equipos')

    return render(request, 'edit_equipos.html', {'equipo': equipo})

def delete_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipos')
    
    return render(request, 'delete_equipo.html', {'equipo': equipo})

def edit_jugador(request, id):
    jugador = Jugador.objects.get(pk=id)
    posicion = Position.objects.get(pk=id)
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        jugador.number = request.POST.get('number')
        jugador.holter = request.POST.get('titular')
        jugador.position = request.POST.get('position')
        jugador.equipos = request.POST.get('equipo')
        
        if photo:
            jugador.photo = photo
            
        jugador.save()
        return redirect('jugadores')
        
    equipo = Equipo.objects.all()
    posicion = Position.objects.all()
    return render(request, 'edit_jugador.html', {'posicion': posicion, 'equipo':equipo, 'jugador':jugador})

def delete_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    
    if request.method == 'POST':
        jugador.delete()
        return redirect('jugadores')
    
    return render(request, 'delete_jugador.html', {'jugador': jugador})

def posiciones(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        posicion = Position(name=name, description= description)
        posicion.save()
        return redirect('posiciones')
    
    posicio = Position.objects.all()
    return render(request, 'posiciones.html', {'posicionesM': posicio})

def edit_posicion(request, id):
    posicion = Position.objects.get(pk=id)
    if request.method == 'POST':
        posicion.name = request.POST.get('name')
        posicion.description = request.POST.get('description')
        posicion.save()
        return redirect('posiciones')
    
    
    return render(request, 'edit_posicion.html', {'posicion': posicion})

def delete_posicion(request, id):
    posicion = get_object_or_404(Position, id=id)
    if request.method == 'POST':
        posicion.delete()
        return redirect('posiciones')

    return render(request, 'delete_posicion.html', {'posicion': posicion})

def tecnicos(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthday = request.POST.get('birthday')
        nacionality = request.POST.get('nacionality')
        rol = request.POST.get('rol')
        tecnicos = tecnico(name= name, surname=surname, birthday= birthday, nacionality= nacionality, Rol= rol)
        tecnicos.save()
        return redirect('tecnicos')
    
    tecnicos_v = tecnico.objects.all()
    return render(request, 'tecnicos.html', {'tecnicos': tecnicos_v})

def edit_tecnico(request, id):
    tecnico_id = tecnico.objects.get(pk=id)
    if request.method == 'POST':
        tecnico_id.Rol = request.POST.get('rol')
        tecnico_id.save()
        return redirect('tecnicos')
        
    return render(request, 'edit_tecnico.html')

def delete_tecnico(request, id):
    tecnico_id = get_object_or_404(tecnico, id=id)
    if request.method == 'POST':
        tecnico_id.delete()
        return redirect('tecnicos')
    
    
    return render(request, 'delete_tecnico.html', {'tecnico': tecnico_id})