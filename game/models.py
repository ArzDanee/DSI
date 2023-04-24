from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=25, default='Game')
    updated = models.DateField(auto_now_add=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    game_mechanism = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    steam_link = models.URLField()
    featured = models.BooleanField(default=False)
    thumbnail = models.FileField(upload_to='game_thumbnail')

    def __str__(self):
        return self.title
    

    @property
    def images(self):
        return Media.objects.filter(file_type=Media.IMAGE)

    @property
    def videos(self):
        return Media.objects.filter(file_type=Media.VIDEO)

class Media(models.Model):
    VIDEO = 'video'
    IMAGE = 'image'
    FILE_TYPE_CHOICES = (
        (VIDEO, 'Video'),
        (IMAGE, 'Image')
    )
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='media_gallery')
    file = models.FileField(upload_to='game_gallery')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default=IMAGE)
    
    def __str__(self):
        return self.file.name
    

    
    
