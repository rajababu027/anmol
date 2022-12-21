from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core import serializers
from .models import employee

def employeeData(request):
    if request.method=='POST':
        name = request.POST['name']
        position = request.POST['position']
        office = request.POST['office']
        age = request.POST['age']
        date = request.POST['date']
        salary = request.POST['salary']
        employeFilterData = serializers.serialize(f"python",employee.objects.filter(name=name))
        positionData = serializers.serialize(f"python",employee.objects.filter(position=position))
        officeData = serializers.serialize(f"python",employee.objects.filter(office=office))
        # ageData = serializers.serialize(f"python",employee.objects.filter(age=age))
        # date = serializers.serialize(f"python",employee.objects.filter(date=date))
        # salaryData = serializers.serialize(f"python",employee.objects.filter(salary=salary))
        employeData = serializers.serialize("python",employee.objects.all())
        context = {
                'employeData':employeData,
                'employeFilterData':employeFilterData,
                'positionData':positionData,
                'officeData':officeData,
                # 'ageData':ageData,
                # 'date':date,
                # 'salaryData':salaryData,
            }
        return render(request,'index.html',context)
    employeData = serializers.serialize("python",employee.objects.all())
    return render(request,'index2.html',{'employeData':employeData})