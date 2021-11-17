from django.shortcuts import render

def index(request):
	return render(request, 'posts/index.html')

def friends(request):
	return render(request, 'posts/friends.html')

def messedge(request):
	return render(request, 'posts/messedge.html')		