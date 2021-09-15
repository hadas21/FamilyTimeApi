from django.db import models
from django.contrib.auth import get_user_model
from .parent import Parent

# Create your models here.
class Family(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  members = models.ManyToManyField(
      get_user_model(),
      through=Parent,
      through_fields=('family', 'member')
  )
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The '{self.name}' family members are '{self.members}'."

  def as_dict(self):
    """Returns dictionary version of Family models"""
    return {
        'id': self.id,
        'name': self.name,
        'members': self.members
    }
