# serializers.py
from rest_framework import serializers

from .models import Business, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('Address1', 'Address2', 'City', 'State',
                    'Zip',)

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    Address = AddressSerializer()
    class Meta:
        depth = 1 # for nested Address
        model = Business
        fields = ('Name', 'SelfReportedCashFlow', 'Address', 'TaxID',
                    'Phone', 'NAICS', 'HasBeenProfitable', 'HasBankruptedInLast7Years', 'InceptionDate',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['Address'] = AddressSerializer(
            Address.objects.get(pk=data['Address1'])).data
        return data
