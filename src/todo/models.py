from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name