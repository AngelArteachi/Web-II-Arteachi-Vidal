from django.db import models


class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    rfc = models.CharField(max_length=13)
    photo = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name


class user_addres(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

