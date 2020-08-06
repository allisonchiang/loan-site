# Whenever we define or change a model, we need to tell Django to migrate those changes.
# py manage.py makemigrations
# py manage.py migrate
# py manage.py createsuperuser
# py manage.py flush
# py manage.py runserver

from django.db import models

# Create your models here.
class Address(models.Model):
    Address1 = models.CharField(max_length=60)
    Address2 = models.CharField(max_length=60, null=True)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=2)
    Zip = models.CharField(max_length=6)

    def __str__(self):
        return self.Address1

class Business(models.Model):
    Name = models.CharField(max_length=255)
    SelfReportedCashFlow = models.FloatField()
    # Address = SeparatedValuesField()
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
    TaxID = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    NAICS = models.CharField(max_length=255)
    HasBeenProfitable = models.BooleanField(max_length=255)
    HasBankruptedInLast7Years = models.BooleanField(max_length=255)
    InceptionDate = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


# class Owners(models.Model):
#     Name = models.CharField(max_length=255)
#     FirstName = models.CharField(max_length=255)
#     LastName = models.CharField(max_length=255)
#     Email = models.CharField(max_length=255)
#     HomeAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
#     DateOfBirth = models.CharField(max_length=255)
#     HomePhone = models.CharField(max_length=255)
#     SSN = models.CharField(max_length=255)
#     PercentageOfOwnership = models.FloatField(max_length=255)

#     def __str__(self):
#         return self.name


# class CFApplicationData(models.Model):
#     RequestedLoanAmount: models.CharField(max_length=255)
#     StatedCreditHistory: models.IntegerField
#     LegalEntityType: models.CharField(max_length=255)
#     FilterID: models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
