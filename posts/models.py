from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=225)
    content=models.TextField()
    author=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='thumbnails',default='default.png')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Post {self.title}>"