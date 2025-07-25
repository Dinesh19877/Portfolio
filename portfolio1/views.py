from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project
# Create your views here.
def homePage(request):
    projects = Project.objects.all()  # Get all projects from the database
    return render(request, 'index.html', {'projects': projects})





@csrf_exempt
def contact_form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Form Submission from {name}"
        body = f"""
        You have received a new message from your portfolio contact form.

        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject,
            body,
            'dineshsharama7799@gmail.com',          # sender
            ['dineshsharama7799@gmail.com'],        # recipient
            fail_silently=False,
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
