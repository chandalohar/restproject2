from rest_framework import serializers
class CustSerializer(serializers.Serializer):
    cname = serializers.CharField(max_length=20)
    cadd = serializers.CharField(max_length=100)
    cacno = serializers.IntegerField()
    cbal = serializers.DecimalField(max_digits=10, decimal_places=2)