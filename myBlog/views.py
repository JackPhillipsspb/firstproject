from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, zForm
from .forms import PostForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import send_mail


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'myBlog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'myBlog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myBlog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myBlog/post_edit.html', {'form': form})

@csrf_protect
def subscribe_post(request):
	pass

@csrf_protect
def create_post(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        response_data = {}
        a = zForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        a.save()
        response_data['form_ok'] = 1
        response_data['result'] = "Сообщение отправлено!"
        
        send_mail(subject, " %s %s" % (message, email), 'robot@foodandfilm.info', ['admin@icont-trade.com'], fail_silently=False)
        
           	
        
        #response_data.update(csrf(request))
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn`t happening"}),
            content_type="application/json"
        )