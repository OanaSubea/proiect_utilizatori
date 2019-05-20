from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_login = models.IntegerField()

    class Meta:
        ordering = ('number_of_login',)
        index_together = (('number_of_login'),)
        db_table = 'Users'

    def __str__(self):
        return self.first_name