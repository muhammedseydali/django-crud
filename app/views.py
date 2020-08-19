from django.shortcuts import render,redirect
from app.models import table
from app.forms import tableform
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# Create your views here.
def insertion(request):
	if request.method == "POST":
		form=tableform(request.POST,request.FILES)
		if form.is_valid():
			print('valid success')
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			department=form.cleaned_data['department']
			address=form.cleaned_data['address']
			contact_number=form.cleaned_data['contact_number']
			email=form.cleaned_data['email']
			profile_picture=form.cleaned_data['profile_picture']
			print('cleaned')
			form=table(first_name=first_name,last_name=last_name,department=department,address=address,contact_number=contact_number,email
				=email,profile_picture=profile_picture)
			print('done')
			form.save()
			print('saved')
			return redirect('/app/show/')  
		else:
			return HttpResponse('not success')	
	else:
			form = tableform()
			return render(request,'index.html',{'add':form})	
def show(request):  
    form = table.objects.all()  
    return render(request,'show.html',{'add1':form})
def edit(request,id):  
    form = table.objects.get(id=id)  
    return render(request,'edit.html', {'editkey':form})  
def update(request,id):
	print('11111')  
	form = table.objects.get(id=id)
	form = tableform(request.POST)
	print('4444')    
	if form.is_valid():
		form.save()    
	return render(request, 'edit.html', {'editkey': form})  
def delete(request,id):  
	form = table.objects.get(first_name=first_name)  
	form.delete()  
	return redirect('/app/show/')       

