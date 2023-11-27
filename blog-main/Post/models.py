from django.db import models
from Profiles.models import Profile
# Create your models here.
from django.db.models import Count
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-id')

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    img = models.ImageField(upload_to = "post/", blank =True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Model manager
    objects=models.Manager()
    posts = CustomManager()

    def __str__(self):
        return self.title[:10]

    def get_num_of_likes(self):
        likes =  self.likes.aggregate(Count('user'))
        return likes['user__count']
    #     return self.likes.count()
    
    def get_my_likes(self):
        return self.likes.all().values()
    

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)    

    # def __str__(self):
    #     return f"{self.user}-{self.post}-{self.body[:5]}"
    
    

class Like(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='my_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.user}-{self.post}"