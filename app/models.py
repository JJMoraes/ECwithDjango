import hashlib
from datetime import datetime

from django.contrib.auth.models import User
#from django.contrib.gis.forms import widgets
from django import template
from django.db import models

class Profile(models.Model):
    __tablename__ = 'profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    about_me = models.TextField(max_length=500, blank=True)

    def __repr__(self, *args, **kwargs):
        return '<Profile: %s>'%self.user.username


class Post(models.Model):
    __tablename__ = 'posts'
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField()
    date = models.DateTimeField(default=datetime.utcnow)    
    image = models.ImageField(upload_to='static/images')
    subtitle = models.TextField(max_length=140)
    lide = models.TextField(max_length=240)
    text = models.TextField(max_length=1800, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def insertArticles():
        user = User.objects.filter(username='jeanKlose').first()
        for x in range(20):
            post = Post(
                    title='Masculinidade Frágil - A falácia dos oprimidos opressores.%d'%x,
                    image='static/images/homem.jpg',
                    subtitle='Homem ajustando a gravata.',
                    lide = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                    Nulla arcu nunc, pharetra eget porta nec, mattis ut urna. Maecenas \
                    augue erat, iaculis vitae vestibulum eget, maximus sed dui.',
                    text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                    Nulla arcu nunc, pharetra eget porta nec, mattis ut urna. Maecenas \
                    augue erat, iaculis vitae vestibulum eget, maximus sed dui \
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                    Nulla arcu nunc, pharetra eget porta nec, mattis ut urna. \
                    Maecenas augue erat, iaculis vitae vestibulum eget, maximus sed dui.',
                    author=user
                )
            post.save()

    def __repr__(self, *args, **kwargs):
        return "<Post: %s>"%self.title