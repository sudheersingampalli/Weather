from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from . forms import Cities_form
from . models import Cities
import requests

# Create your views here.

def home(request):
	if request.method == 'POST':
		temp_details = Cities_form(request.POST)
		if temp_details.is_valid():
			url = 'http://api.openweathermap.org/data/2.5/weather?appid=194f84243cbe067b08c91b419facc1d6&units=metric&q='
			com_url = url+request.POST.get('City_name','')
			print 'com_url is ..', com_url
			raw_data = requests.get(com_url).json()
			print 'raw_data ', raw_data
			print 'description ', raw_data['weather'][0]['description']
			msg=''
			if 'message' in raw_data.keys(): 
				msg = 'City not found'
				flag = 0
				cities = Cities.objects.all()
				context = {'msg':msg,'cities':cities,'Cities_form':Cities_form,'flag':flag}
				return render(request,'weatherapp/home.html',context)
			else:
				flag = 1
				item = temp_details.save(commit = False)
				input_name = request.POST.get('City_name',' ')
				
				try:
					city = Cities.objects.get(City_name=input_name)
				except ObjectDoesNotExist:
					city= None

				if city is None:
					item.save()
				cities = Cities.objects.all()
				context = {'flag':flag,'cities':cities,'raw_data':raw_data,'msg':msg}
				return render(request,'weatherapp/home.html',context)
		else:
			print 'form is not valid'
			msg = 'Input a City name'
			cities = Cities.objects.all()
			print 'cities..',cities
			context = {'flag':0,'Cities_form':Cities_form,'cities':cities,'msg':msg}
			return render(request,'weatherapp/home.html',context)
			
	if request.method == 'GET':
		print 'inside get'
		cities = Cities.objects.all()
		print 'cities..',cities
		context = {'flag':0,'Cities_form':Cities_form,'cities':cities}
		return render(request,'weatherapp/home.html',context)
	
