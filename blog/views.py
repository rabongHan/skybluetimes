from django.shortcuts import render, get_object_or_404, redirect, reverse
from blog.models import Category, Post
import random
from django.views import generic
from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings
from marketing.forms import EmailSignupForm
from marketing.models import Signup, Comment
from django.http import HttpResponseRedirect
from django.db.models import Q

form = EmailSignupForm()

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:4]
    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)
    post_main = Post.objects.filter(main3=True)
    post_editorpick = Post.objects.filter(editorpick=True)
    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    form = EmailSignupForm()
    context = {
        "post_latest": post_latest,
        "post_random": post_random,
        "post_main": post_main,
        "post_editorpick": post_editorpick,
        "form": form,
        
    }
    return render(req, "index.html", context=context)

# def single(req):
#     context = {

#     }
#     return render(req, "single.html", context=context)

class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    
    def post(self, request, pk):
        post = self.get_object()
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        comment = request.POST.get('comment', False)
        new_comment = Comment()
        new_comment.name = name
        new_comment.email = email
        new_comment.comment = comment
        new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_latest'] = Post.objects.order_by("-createDate")[:4]
        context['post_random'] = random.sample(list(Post.objects.all()), 4)
        
        return context
    
def politic(req):
    post_politics = Post.objects.filter(category=2)
    post_politics_latest = post_politics.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_politics_latest": post_politics_latest,
        "post_random": post_random,
        "form": form
    }
    return render(req, "politic.html", context=context)

def science(req):
    post_science = Post.objects.filter(category=1)
    post_science_latest = post_science.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_science_latest": post_science_latest,
        "post_random": post_random,
        "form": form
    }
    return render(req, "science.html", context=context)

def business(req):
    post_business = Post.objects.filter(category=4)
    post_business_latest = post_business.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_business_latest": post_business_latest,
        "post_random": post_random,
        "form": form
    }
    return render(req, "business.html", context=context)

def economy(req):
    post_economy = Post.objects.filter(category=3)
    post_economy_latest = post_economy.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)
    
    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_economy_latest": post_economy_latest,
        "post_random": post_random,
        "form": form,
        
    }
    return render(req, "economy.html", context=context)

def art(req):
    post_art = Post.objects.filter(category=5)
    post_art_latest = post_art.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_art_latest": post_art_latest,
        "post_random": post_random,
        "form": form
    }
    return render(req, "art.html", context=context)

def csialife(req):
    post_csialife = Post.objects.filter(category=6)
    post_csialife_latest = post_csialife.order_by("-createDate")

    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_csialife_latest": post_csialife_latest,
        "post_random": post_random,
        "form": form
    }
    return render(req, "csialife.html", context=context)

def aboutus(req):
    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_random": post_random,
        "form": form
    }
    return render(req, "aboutus.html", context=context)

def allposts(req):
    post_editorpick = Post.objects.filter(editorpick=True)
    post_latest = Post.objects.order_by("-createDate")

    if req.method == "POST":
        email = req.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_latest": post_latest,
        "post_editorpick": post_editorpick,
        "form": form

    }
    return render(req, "allposts.html", context=context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    posts = list(Post.objects.all())
    post_random = random.sample(posts, 4)
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(textcontent__icontains=query) |
            Q(author__icontains=query)
        ).distinct()

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    form = EmailSignupForm()
    context = {
        "post_random": post_random,
        'queryset': queryset,
        'form':form,
        'query': query
    }
    return render(request, 'search_results.html', context=context)
