from django.shortcuts import render
from django.http import HttpResponse
from .models import SingerModel

def singerView(request):
    singer = SingerModel.objects.all()
    return render(request, "singer/singer.html", {'singer': singer})








    #  try:
    #     p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404("Poll does not exist")
    # return render(request, "polls/detail.html", {"poll": p})