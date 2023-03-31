from django.urls import path, include
from . import views
# import debug_toolbar

urlpatterns = [
    # URL patterns for candidates
    path('', views.home, name='kazi'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('profile', views.profile, name='profile'),


    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('edit_candidate/', views.edit_candidate, name='edit_candidate'),
    path('register/', views.RegisterPage, name='register'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('candidates/create/', views.candidate_create, name='candidate_create'),
    path('candidates/<int:candidate_id>/update/', views.candidate_update, name='candidate_update'),
    path('candidates/<int:candidate_id>/delete/', views.candidate_delete, name='candidate_delete'),

    # URL patterns for jobs
    path('jobs/list', views.joblist_list, name='job_list'),
    path('jobs/talent/', views.talent, name='talent'),
    path('jobs/create/', views.joblist_create, name='job_create'),
    path('jobs/<int:pk>/update/', views.joblist_update, name='job_update'),
    path('jobs/<int:pk>/delete/', views.joblist_delete, name='job_delete'),
    path('jobs/category', views.category, name='category'),

    # URL patterns for companies
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('companies/create/', views.company_create, name='company_create'),
    #path('companies/<int:pk>/update/', views.company_update, name='company_update'),
    #path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),
    # path('__debug__/', include('debug_toolbar.urls')),
    
]


'''
    # URL patterns for job categories
    path('job_categories/', views.job_category_list, name='job_category_list'),
    path('job_categories/<int:pk>/', views.job_category_detail, name='job_category_detail'),
    path('job_categories/create/', views.job_category_create, name='job_category_create'),
    path('job_categories/<int:pk>/update/', views.job_category_update, name='job_category_update'),
    path('job_categories/<int:pk>/delete/', views.job_category_delete, name='job_category_delete'),
    path('', views.home, name = "test") 

'''