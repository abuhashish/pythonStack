from django.db import models
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

class Message(models.Model):
    message=models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comment(models.Model):
    comment=models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)