from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    GENRE = [
        ('FPS', 'first-person shooter'),
        ('RP', 'role playing'),
        ('P', 'puzzle'),
        ('AG', 'action game')
    ]

    FSK = [
        ('0','von 0'),
        ('6','ab 6 Jahre'),
        ('12', 'ab 12 Jahre'),
        ('16', 'ab 16 Jahre'),
        ('18', 'ab 18 Jahre')
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    studio = models.CharField(max_length=50)
    release_published = models.DateTimeField()
    genre = models.CharField(max_length=3,
                            choices=GENRE,
                            )

    fsk = models.CharField(max_length=2,
                            choices=FSK,
                            )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta: 
        ordering = ['name', '-genre']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name + ' (' + self.studio + ')'

    def __repr__(self):
        return self.name + ' / ' + self.studio + ' / ' + self.genre + ' / ' + self.fsk