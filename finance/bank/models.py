from django.db import models

class FinancialOrganization(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Executive(models.Model):
    fio = models.CharField(max_length=128)
    iin = models.BigIntegerField()
    position = models.CharField(max_length=128)
    contact = models.TextField()
    image = models.ImageField(upload_to='images')
    bank = models.ForeignKey(to=FinancialOrganization, on_delete=models.CASCADE)

    def __str__(self):
        return f'Direktor {self.bank.name} | {self.fio} '
