from django.shortcuts import render

# Create your views here.
def specific_folder(request):
    return render(request,'specific_folder.html')
