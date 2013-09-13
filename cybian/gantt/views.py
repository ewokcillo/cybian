from django.shortcuts import render

def gantt(request):
    params = {}
    return render(request, 'gantt/gantt.html', params)
