from django.shortcuts import render
from .models import Company

def landing(request):
    
    return render(request, 'shatter/landing.html', {})

def company(request, company=None):
    companyObj = Company.objects.get(name=company)
    comments = companyObj.comment_set.all()
    return render(request, 
            'shatter/company.html', 
            {
                'company':companyObj,
                'comments':comments
            }) 

def survey(request):
    return render(request, 'shatter/survey.html', {})
