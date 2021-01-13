from django.urls import path, include
from blog import views

urlpatterns= [
    path("", views.index, name="index"),
    # path("single/", views.single, name="single"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post"),
    path("politic/", views.politic, name="politic"),
    path("science/", views.science, name="science"),
    path("business/", views.business, name="business"),
    path("economy/", views.economy, name="economy"),
    path("art/", views.art, name="art"),
    path("csialife/", views.csialife, name="csialife"),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("allposts/", views.allposts, name="allposts"),
    path('search/', views.search, name='search'),
]