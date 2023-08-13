from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        service_type = request.POST['service_type']
        details = request.POST['details']
        attached_file = request.FILES['attached_file']
        resolved_date = request.POST['resolved_date']
        status = request.POST['status']

        service_request = ServiceRequest(customer_name=customer_name,service_type=service_type,details=details,attached_file=attached_file,resolved_date=resolved_date,status=status)

        service_request.save()
        
    return render(request, 'submit_request.html')

def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'track_request.html', {'service_request': service_request})

def support_dashboard(request):
    requests = ServiceRequest.objects.all()

    context = {
        'requests':requests
    }

    return render(request, 'list_request.html', context)

def dashboard(request):

    return render(request, 'index.html')