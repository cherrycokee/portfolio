from django.shortcuts import render
from .models import Post
from django.shortcuts import render
# Create your views here.
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def index(request):
    post = Post.objects.all()
    context = {
        'post' : post,
    }
    return render(request, 'final/final.html', context)
