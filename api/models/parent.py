from django.db import models
from django.contrib.auth import get_user_model



class Parent(models.Model):

    member = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)
    family = models.ForeignKey('Family', on_delete=models.CASCADE)

    def __str__(self):
        return self.due_date
