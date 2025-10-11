from django.shortcuts import render

def grades_list(request):
    return render(request, 'diary/grades_list.html')
