from django.db import models

# aadmin:admin123@


class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

