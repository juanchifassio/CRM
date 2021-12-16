from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.utils.translation import ugettext_lazy as _
from PIL import Image


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def save(self,**kwargs):                    
        super().save()

        img= Image.open(self.image.path)

        if img.height>500 or img.width>500:
            output_size=(500,500)
            img.thumbnail(output_size)
            img.save(self.image.path) 


class Agent(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=50, null=True, blank=True)
    phone=models.CharField(max_length=12)
    email=models.EmailField()

    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def save(self,**kwargs):                    
        super().save()

        img= Image.open(self.image.path)

        if img.height>500 or img.width>500:
            output_size=(500,500)
            img.thumbnail(output_size)
            img.save(self.image.path) 

    def __str__(self):
        return f'{self.email}'




class Lead(models.Model):

    CHOICES=[('Open','Open'),
            ('Working','Working'),
            ('Customer','Customer'),
            ('Nurture','Nurture'),
            ('Inactive','Inactive'),
    ]

    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    birthday=models.DateTimeField(help_text="YYYY-MM-DD")
    address=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    description= models.CharField(max_length=500, null=True, blank=True)
    agent=models.ForeignKey(Agent, on_delete=SET_NULL, null= True, blank=True)
    status=models.CharField(choices=CHOICES, max_length=50, null=True, blank=True, default='Open')

    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
