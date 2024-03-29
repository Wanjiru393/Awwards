from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name='Index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.sign_out, name='logout'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('new/project',views.new_project, name='new-project'),
    path('directory/',views.directory, name='directory'),
    path('profile/',views.profile, name='profile'),
    path('site/<site_id>',views.site,name='site'),
    path('search/',views.search_results, name='search_results'),
    # path('user/',views.user_profile,name='user-profile'),

    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)