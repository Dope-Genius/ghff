from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from .models import Contact
# from django.views.generic import ListView, DetailView


def index(request):
  queryset = Post.objects.filter(featured=True)[0:3]
  # queryset = Post.objects.order_by('-timestamp')[0:3]
  context = {
    'object_list': queryset
  }
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')


def blog(request):
  post_list = Post.objects.all() 
  paginator = Paginator(post_list, 2)
  page_request_var = 'page'
  page = request.GET.get(page_request_var)

  try:
    paginated_queryset = paginator.page(page)
  except PageNotAnInteger:
    paginated_queryset = paginator.page(1)
  except EmptyPage:
    paginated_queryset = paginator.page(paginator.num_pages)

  context = {
    'queryset': paginated_queryset,
    'page_request_var': page_request_var
  }
  return render(request, 'blog.html', context)


def post_details(request, id):
  return render(request, 'post_detail.html', {
    'post': get_object_or_404(Post, pk=id)
  })

def challenge(request):
  return render(request, 'challenge.html' )

def contact(request):
  if request.method == 'POST':
    fullname = request.POST['fullname']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    date = request.POST['date']

    contact = Contact(fullname=fullname, email=email, subject=subject, message=message, date=date,)

    contact.save()

  return render(request, 'contact.html')

def donate(request):
  return render(request, 'donate.html')

def ourwork(request):
  post_list = Post.objects.filter(work=True) 
  paginator = Paginator(post_list, 2)
  page_request_var = 'page'
  page = request.GET.get(page_request_var)

  try:
    paginated_queryset = paginator.page(page)
  except PageNotAnInteger:
    paginated_queryset = paginator.page(1)
  except EmptyPage:
    paginated_queryset = paginator.page(paginator.num_pages)

  context = {
    'queryset': paginated_queryset,
    'page_request_var': page_request_var
  }
  return render(request, 'ourwork.html', context)
  # return render(request, 'ourwork.html')

def getinvolved(request):
  return render(request, 'getinvolved.html')

def teams(request):
  return render(request, 'teams.html')

