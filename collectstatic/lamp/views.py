from django.shortcuts import render


# def home(request):
#     return render(request, 'index.html')


def integration(request):
    return render(request, 'Integration/sms_service.html')
