from django.db import models

# Create your models here.
class LibraryModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    publication = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    