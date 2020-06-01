from django.shortcuts import render
from django.contrib.auth.models import Group
from dentist.settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail

# Create your views here.
def index(request):
    return render(request, 'index.html',{})
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email          
        message1 = (message_name, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        message2 = (message_name, 'we received your mail and will response shortly......', EMAIL_HOST_USER, [message_email])
        send_mass_mail((message1, message2), fail_silently=True)

        return render(request, 'contact.html', {'message_name':message_name})


    else:
        return render(request, 'contact.html',{})
def about(request):
    return render(request, 'about.html',{})
def service(request):
    return render(request, 'service.html',{})
def pricing(request):
    return render(request, 'pricing.html',{})
def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_time = request.POST['your-time']
        your_date = request.POST['your-date']
        your_message =request.POST['your-message']
        #send an email  
        appointment = "Name: " + your_name + "\n" + "Phone No. :" + your_phone + "\n" + "Email: " + your_email + "\n" + "Address: " + your_address + "\n" + "Appointment_Time: " + your_time + "\n" + "Appointment_Day: " + your_date + "\n" + "Message: " + your_message  
        message1 = (your_name, appointment, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        message2 = (your_name, 'Thank you !!! we received your mail and will response shortly......', EMAIL_HOST_USER, [your_email])
        send_mass_mail((message1, message2), fail_silently=True)

        return render(request, 'appointment.html', {
        'your_name': your_name,
        'your_phone': your_phone,
        'your_email': your_email,
        'your_address': your_address,
        'your_time': your_time,
        'your_date': your_date,
        'your_message': your_message})
    else:
        return render(request, 'index.html', {})




