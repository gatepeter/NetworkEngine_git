from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'cisco'

urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('logout/', views.LogoutClass.as_view(), name='logout'),
    path('control/', views.ControlSite.as_view(), name='control'),
    path('home/', views.HomeClass.as_view(), name='home'),
    path('addevice/', views.AddeviceClass.as_view(), name='addevice'),
    path('aboutme/', views.AboutClass.as_view(), name='aboutme'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('search/', views.SearchResultsView.as_view(), name='Search_results'),
    path('monitor/', views.Monitor.as_view(), name='monitor'),
    #TODO: export file excel ...
    path('export/', views.CSVPageView.as_view(), name='export_excel'),
    path('export/excel', views.export_users_xls, name='export_excel'),
    path('import/', views.simple_upload, name='import_excel'),
    ######################################
    path('settings/', views.simple_upload, name='settings'),
    # path('settings/', views.settings.as_view(), name='settings'),
]
