from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, choices=[
        ('Leadership', 'Leadership'),
        ('Strategy', 'Strategy'),
        ('Technology', 'Technology'),
    ])
    community = models.CharField(max_length=255, choices=[
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Technology', 'Technology'),
    ])
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
