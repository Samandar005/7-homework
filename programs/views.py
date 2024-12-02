from django.shortcuts import render, redirect
from .models import Program


def language_list(request):
    languages = Program.objects.all()
    ctx = {'languages': languages}
    return render(request, 'programs/program-list.html', ctx)

def language_create(request):
    language_name = request.POST.get('language_name')
    description = request.POST.get('description')
    if language_name and description:
        Program.objects.create(
            language_name = language_name,
            description = description
        )
        return redirect('programs:language_list')
    return render(request, 'programs/program-form.html')
