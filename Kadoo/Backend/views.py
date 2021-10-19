from django.shortcuts import render

# Create your views here.
def mainPage(request):
    return render(request, 'main.html')

def plantPage(request):
    return render(request, 'Backend/plantsTable.html')

def toolPage(request):
    return render(request, 'Backend/toolsTable.html')

def tagPage(request):
    return render(request, 'Backend/tagsTable.html')