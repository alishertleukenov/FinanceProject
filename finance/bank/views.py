from django.shortcuts import render
from bank.models import Executive, FinancialOrganization
def index(request):
    context = {
        'bank': FinancialOrganization.objects.all(),
        'executive': Executive.objects.all()
    }
    return render(request, 'view.html', context)