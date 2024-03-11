from django.db import models


class Equipo(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    flag = models.ImageField(upload_to='flags/', null=True, verbose_name='Bandera')
    shield = models.ImageField(upload_to='shields/', null=True, verbose_name='Escudo')

    def __str__(self):
        return self.name
        return self.flag
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipo"
        ordering = ['id']
        
class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=300, verbose_name="descripción")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Posición"
        verbose_name_plural = "Posiciones"
        db_table = "position"
        ordering = ['id']
    

class Jugador(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    surname = models.CharField(max_length=50, verbose_name="Apellido")
    photo = models.ImageField(upload_to='players/', null=True, verbose_name="Foto")
    birthday = models.DateField(verbose_name="Fecha de nacimiento")
    number = models.IntegerField(verbose_name="Número de camiseta")
    holder = models.BooleanField(verbose_name="Titular")
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
        return self.position
        return self.number
        return self.holder
        return self.type
    
    class Meta:
        verbose_name="Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugadores"
        ordering = ['id']

class tecnico(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    surname = models.CharField(max_length=50, verbose_name="Apellido")
    birthday = models.DateField(verbose_name="Fecha de nacimiento")
    nacionality = models.CharField(max_length=50, verbose_name="Nacionalidad")
    Rol = models.CharField(max_length=50, verbose_name="Rol")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Tecnico"
        verbose_name_plural = "Tecnicos"
        db_table = "tecnico"
        ordering = ['id']