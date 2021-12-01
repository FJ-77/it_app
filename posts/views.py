from django.shortcuts import render
from .models import Post
from .models import Advertisement

def index(request):
	return render(request, 'posts/index.html')

def friends(request):
	return render(request, 'posts/friends.html')

def login(request):
	return render(request, 'posts/login.html')	

def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'posts/post_list.html', context)		

def advertisement_table(request):
	adverts = Advertisement.objects.all()
	context = {
		'adverts': adverts
	}	
	return render(request, 'posts/advertisement_table.html', context)