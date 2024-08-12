from django.db import models # type: ignore

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
# Example for Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
