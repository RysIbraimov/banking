from django.db import models
import datetime
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20, default='Кыргызстан')
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.IntegerField(unique=True)
    accaunt_type = models.PositiveIntegerField(default=1)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)



class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateField(datetime.date.today())
    account = models.ForeignKey(Account, on_delete=models.CASCADE)





