from django.shortcuts import render
from django.views import View
from restapp2.serializers import CustSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
class Cust:
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
class Home(View):
    def get (self,request):
        c1=Cust("scott","mumbai",1001,100900.00)
        c2 = Cust("black", "delhi", 1002, 10087870.00)
        c3 = Cust("smith", "hyderabad", 1003, 10686800.00)
        c4 = Cust("alex", "banglore", 1004, 1006460.00)
        custs=[c1,c2,c3,c4]
        cs1=CustSerializer(custs,many=True)
        custdata=JSONRenderer().render(cs1.data)
        return HttpResponse(custdata,content_type="application/json")


