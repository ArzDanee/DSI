from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
User = get_user_model()
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=25, default='Blog')
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='blog_thumbnail',)
    featured = models.BooleanField()

    def __str__(self):
        return self.title