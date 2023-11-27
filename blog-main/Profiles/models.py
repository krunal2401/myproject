from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    avatar = models.ImageField(default = "avatar.jpg", upload_to='avatars/')
    COUNTRY = (
        ('India','India'),
        ('USA','USA'),
        ('UK','UK'),
        )
    country= models.CharField(max_length=5,choices=COUNTRY, default='India')
    LANG = (
        ('English(US)','English(US)'),
        ('English(UK)','English(UK)'),
        )
    language = models.CharField(max_length=11,choices=LANG, default='English(US)')

    def __str__(self):
        return str(self.user)

    def all_author_posts_num(self):
        return self.post.all().count()
    
    def get_all_author_posts(self):
        return self.post.all()
    
    def get_my_likes(self):
        return self.my_likes.all()

    def natural_key(self):
        return (self.firstname, self.lastname, self.email,str(self.user), str(self.avatar))
    