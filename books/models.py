from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=9)
    bio = models.TextField()
    works = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name




