from django.http import HttpResponse
from .models import Investment

def index(request):
    latest_investments_list = Investment.objects.order_by('-notification_du_marche')[:5]
    output = ', '.join([i.titreoperation for i in latest_investments_list])
    return HttpResponse(output)


def detail(request, investment_id):
    return HttpResponse("You're looking at investment %s." % investment_id)


def results(request, investment_id):
    response = "You're looking at the results of investment %s."
    return HttpResponse(response % investment_id)


def vote(request, investment_id):
    return HttpResponse("You're voting on investment %s." % investment_id)
