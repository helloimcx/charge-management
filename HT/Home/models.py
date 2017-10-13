from django.db import models
from uuid import uuid1


# Create your models here.
class Suggestions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    phone = models.CharField(max_length=254)
    title = models.TextField(max_length=254)
    content = models.TextField()
    record_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
