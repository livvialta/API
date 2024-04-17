from django.db import models

class ToDo(models.Model):
    Title = models.CharField(max_length = 100, blank = False)
    Description = models.TextField(blank = True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    Completed = models.BooleanField(default = False)

    def __str__(self):
        return self.Title
