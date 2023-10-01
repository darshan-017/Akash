from django.shortcuts import render
from .models import ContactInfo, Photo
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    photo = Photo.objects.filter(name="home").first()
    context = {
        'photo': photo
    }
    return render(request, 'basic_web/home.html', context)


def about(request):
    return render(request, 'basic_web/about.html', {'title': 'About'})

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        address = request.POST['address']
        #sent = send_mail(name, message, 'journeysbyakash003@gmail.com', ['journeysbyakash003@gmail.com'])
        contact_info = ContactInfo( name = name,
                                    phone = phone,
                                    email = email,
                                    address = address,
                                    discuss_about = message)
        contact_info.save()
    return render(request, 'basic_web/contact.html', context={'title':'Contact'})

def portfolio(request):
    photos = Photo.objects.all()
    context = {
        'title':'Portfolio', 
        'photos':photos,
        'big_photo': Photo.objects.last()}
    return render(request, 'basic_web/portfolio.html', context=context)