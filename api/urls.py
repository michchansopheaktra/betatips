from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('add-category/', views.category_add, name='category_add'),
    path('category/edit/<slug:slug>/', views.category_edit, name='category_edit'),
    path('category/delete/<slug:slug>/', views.category_delete, name='category_delete'),

    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add-post/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('tag/<slug:tag_slug>/', views.tagged_posts, name='tagged_posts'),

    path('search/', views.post_search, name='post_search'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
    path('contact/', views.contact_page, name='contact'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('about/', views.about_page, name='about'),
   
]
