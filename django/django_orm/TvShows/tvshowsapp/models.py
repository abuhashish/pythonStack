
from django.db import models
    
class ShowManger(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network  should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "description  should be at least 10 characters"
        for i in Show.objects.all():
            if i.title == postData['title']:
                errors['unqiue']="title name must be unique"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManger() 
