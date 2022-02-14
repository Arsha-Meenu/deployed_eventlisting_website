from unicodedata import name
from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
 
app_name = 'events'
urlpatterns = [
    path('',views.Dashboard.as_view(),name = 'landing-page'),
    path("like/<int:id>", views.LikedEvent, name="like-event"),
    path("dislike/<int:id>/", views.DisLikedEvent, name="dislike-event"),
    path('register/',views.UserRegisterView.as_view(),name = 'register'),
    path('login/',views.UserLoginView.as_view(),name = 'login'),
    path('userprofile/',views.UserProfileView.as_view(),name='user-profile'),
    path('get-event-details/<int:pk>',views.EventDetailView.as_view(),name='get-event-details'),
    path('event-list',views.EventListView.as_view(),name='event-list'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('<pk>/update/',views.UserProfileUpdate.as_view(),name = 'userprofile-update'),
    path('<pk>/image-update/',views.UserProfileImageUpdate.as_view(),name = 'userimage-update'),
    path('create-checkout-session/<int:pk>/',views.CreateCheckoutSessionView.as_view(),name = "create-checkout-session"),
    path('filtering/',views.FilterSearchEvent,name = 'event-filtering'),

]

urlpatterns += staticfiles_urlpatterns()