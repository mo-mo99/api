from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.user_name


class Subject(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True, blank=True)
    text = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField()