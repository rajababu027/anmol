from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core import serializers
from .models import employee

def employeeData(request):
    if request.method=='POST':
        TextData = request.POST['name']
        print(TextData)
        employeFilterData = serializers.serialize(f"python",employee.objects.filter(name=TextData))
        # TextStore(TextData=TextData).save()
        # results = TextStore.objects.filter(topic__startswith=f"{TextData}")
        print("-----------------")
        print(employeFilterData)
        print("-----------------")
    employeData = serializers.serialize("python",employee.objects.all())
    print("-----------------")
    print(employeData)
    print("-----------------")
    # context = {
    #     'employeData':employeData,
    #         # 'employeFilterData':employeFilterData,
    # }
    return render(request,'index.html',{'employeData':employeData,'employeFilterData':employeFilterData,})
    # return render(request,'index.html',{'employeData':employeData,})