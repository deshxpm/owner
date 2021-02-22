from django.shortcuts import render


# def home(request):
#     return render(request, 'index.html')


def integration(request):
    return render(request, 'Integration/sms_service.html')


def course(request):
	return render(request, 'course/course.html')


def instructor(request):
	return render(request, 'course/instructor.html')