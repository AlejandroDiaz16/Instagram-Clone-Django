from django.urls import path

from platzigram import views

urlpatterns = [
    path('hola', views.holaa),
    path('', views.hello),
    path('sorted/', views.sorted),
    path('hi/<str:name>/<int:age>', views.say_hi)
]
