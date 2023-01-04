from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse
# Create your views here.


def form_view(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data()
            uc = UserComments(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                comment=cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })

    return render(request, 'blog.html', {'form': form})


def ratings(request):
    greeting = "Welcome to the Django example page, ... ratings"
    print("Rating test!")
    return HttpResponse(request, greeting)
