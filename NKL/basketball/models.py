from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.

class Team(models.Model):
    name = models.CharField(_('name'), max_length= 50)
    budget = models.IntegerField(_('budget'))
    # arena = models.ManyToManyField(Arena, verbose_name= _('Arena(s)'), help_text=_('choose arenas for this team'))
    

    def __str__(self) -> str:
        return self.name

    def display_sponsors(self) -> str:
        return ', '.join(sponsor.name for sponsor in self.sponsors.all())
    display_sponsors.short_description = _('sponsor(s)')

    def display_arenas(self) -> str:
        return ', '.join(arena.name for arena in self.arenas.all())
    display_arenas.short_description = _('arena(s)')


class Sponsor(models.Model):
    name = models.CharField(_('name'), max_length= 30)
    team = models.ForeignKey(Team, verbose_name='team', on_delete=models.SET_NULL, null=True, related_name='sponsors')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('sponsor')
        verbose_name_plural = _('sponsors')


class Arena(models.Model):
    name = models.CharField(_('name'), max_length= 50)
    address = models.CharField(_('address'), max_length= 50)
    capacity = models.IntegerField(_('capacity'))
    team = models.ForeignKey(Team, verbose_name='team', on_delete=models.SET_NULL, null=True, related_name='arenas')


    def __str__(self) -> str:
        return f"{self.name} {self.address}"


class Staff(models.Model):
    name = models.CharField(_('name'), max_length = 30)
    surname = models.CharField(_('surname'), max_length= 30)
    birth_date = models.DateField(_('birth_date'))
    salary = models.IntegerField(_('salary'))
    responsibility = models.CharField(_('responsibility'), max_length= 50)
    team = models.ForeignKey(Team, verbose_name='team', on_delete=models.SET_NULL, null=True, related_name='staffs')
    photo = models.ImageField(_('photo'), upload_to='photos', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
                photo.save(self.photo.path)


class Player(models.Model):
    POSITION_CHOICES = (
        ('C', _('Center')),
        ('PF', _('Power Forward')),
        ('SF', _('Small Forward')),
        ('SG', _('Shooting Guard')),
        ('PG', _('Point Guard'))
    )
    jersey_number = models.IntegerField(_("jersey_number"))
    name = models.CharField(_('name'), max_length = 30)
    surname = models.CharField(_('surname'), max_length= 30)
    birth_date = models.DateField(_('birth_date'))
    height = models.IntegerField(_('height'))
    weight = models.IntegerField(_('weight'))
    position = models.CharField(_('position'), max_length= 2, choices=POSITION_CHOICES)
    salary = models.IntegerField(_('salary'))
    birth_country = models.CharField(_('birth_country'), max_length= 20)
    photo = models.ImageField(_('photo'), upload_to='photos', null=True, blank=True)
    team = models.ForeignKey(Team, verbose_name='team', on_delete=models.SET_NULL, null=True, blank=True, related_name='players')

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
                photo.save(self.photo.path)