
import csv
from django.shortcuts import render
from django.views import View

from app01.models import Cities, Hotels
# Create your views here.
class InfosView(View):
    def get(self, request):
        cities = Cities.objects.all()

        context = {
            'cities': cities
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        cities = Cities.objects.all()

        city = request.POST.get('city')
        hotel = Hotels.objects.filter(code=city)

        return render(request, 'index.html', {'cities': cities,
                                               'hotel': hotel})

class Read_csvView(View):
    def post(self,request):
        f = request.FILES['my_file']
        type_excel = f.name.split('.')[1]
        if 'csv' == type_excel:
            name = f.name.split('.')[0]
            if name =='city':
                file_data = f.read().decode()
                for i in file_data.split('\n'):
                    if len(i) <2:
                        pass
                    else:
                        data = i.replace("'","").replace('"','').split(';')
                        print(data)
                        Cities.objects.create(code=data[0],name=data[1])
#
            if name =='hotel':
                file_data = f.read().decode()
                for i in file_data.split('\n'):
                    if len(i)<3:
                        pass
                    else:
                        data = i.replace('"','').replace("'","").split(';')
                        code_id = Cities.objects.filter(code=data[0]).first()
                        Hotels.objects.create(code=code_id,name=data[-1],hotel_code=data[1])

        return render(request,'index.html')









