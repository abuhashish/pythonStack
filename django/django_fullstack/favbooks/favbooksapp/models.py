from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
class UserManger(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['Username']) < 3:
            errors["name"] = "Username should be at least 3 characters"
        if len(postData['password']) < 10:
            errors["desc"] = "password should be at least 10 characters"
        return errors
class User(models.Model):
    image = models.ImageField(upload_to='images/',default='pic.png')
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger() 
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    uploaded_by = models.ForeignKey(User,related_name="books_uploaded",on_delete=CASCADE)
    users_who_like = models.ManyToManyField(User,related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
