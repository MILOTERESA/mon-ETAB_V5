from django.db import models

from user.models.user import CustomUserModel
from base.models.adress import AddressModel
from ..models.helpers.datemodel import DateTimeModel
from django.template.defaultfilters import slugify
import random
import string


GENDER = [
    ('F', 'WOMEN'),
    ('M', 'MEN'),
    ('O', 'OTHER'),
]

class Person(DateTimeModel):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_de_creation = models.DateField(auto_now_add=True)
    picture = models.URLField()
    telephone = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices= GENDER)
    age = models.PositiveIntegerField()  # Champ pour l'âge, uniquement des entiers positifs
    adress = models.OneToOneField(AddressModel, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    slug = models.SlugField( max_length = 100 , unique = True , blank = True ) # Champ slug unique

    class Meta :
        abstract = True

    def save ( self , * args , ** kwargs ):
        if not self.slug :
 # Génère un slug à partir du prénom et du nom
            base_slug = slugify( f"{self.first_name } - {self.last_name }" )
            slug = base_slug

 # Vérifie si le slug existe déjà dans la base de données et génère un slug unique
        while self.__class__.objects.filter(slug = slug).exists() :
 # Ajout d'un suffixe aléatoire pour assurer l'unicité
            random_suffix = '' .join(random.choices(string.ascii_lowercase + string.digits, k = 4 ))
            slug = f"{ base_slug } - { random_suffix }"

        self.slug = slug
        super (PersonModel, self ).save( * args, ** kwargs)
