from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from .views import ChangePasswordView



urlpatterns=[
    # ?handles for ajax
    path("french_bib_handle/",views.french_bib_handle,name="french_bib_handle"),
    path("darija_bib_handle/", views.darija_bib_handle, name="darija_bib_handle"),
    path("arabic_bib_handle/",views.arabic_bib_handle,name="arabic_bib_handle"),
    path("english_bib_handle/",views.english_bib_handle,name="english_bib_handle"),
   
#    ?404 page
    # path("p404/",views.error_404,name="p404"),
    path("register/",views.registerPage,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("darija_bib_main/",views.home3,name="home3"),
    path("english_bib_main/",views.english_bib_main,name="english_bib_main"),
    path("arabic_bib_main/",views.arabic_bib_main,name="arabic_bib_main"),
    path("french_bib_main/",views.french_bib_main,name="french_bib_main"),
    path("english_bib_main_excel/",views.english_bib_main_ex,name="english_bib_main_excel"),
    path("arabic_bib_main_excel/",views.arabic_bib_main_ex,name="arabic_bib_main_excel"),
    path("french_bib_main_excel/",views.french_bib_main_ex,name="french_bib_main_excel"),
    path("",views.mainPage,name="MainPage"),
    path("lang_choice/",views.home4,name="home4"),
    # path("clean_english/",views.clean_english,name="EnglishClean"),
    path("english_bib/",views.english_bib,name="english_bib"),
    path("arabic_bib/",views.arabic_bib,name="arabic_bib"),
    path("french_bib/",views.french_bib,name="french_bib"),
    
    # path("excelTest/",views.home,name="home"),
    path("excelTest/",views.process_file,name="home"),
    path("excelTest_FR/",views.process_file_fr,name="home"),
    path("excelTest_ENG/",views.process_file_eng,name="home"),
    path("excelTest_AR/",views.process_file_ar,name="home"),
    path("clean_darija/", views.clean_data, name="home2"),
    path("clean_excel/",views.clean_excel, name="cleanExecl"), #cleanExcel will be used in href
    #!Reset password
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="main3/password_reset.html") , 
         name ="reset_password"),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="main3/password_reset_done.html"), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="main3/password_reset_confirm.html") , 
         name="password_reset_confirm"),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="main3/password_reset_complete.html") , 
         name = "password_reset_complete"),

     path('change_password/', ChangePasswordView.as_view(template_name='main3/password_reset_confirm.html'), name='change_password'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler404 ='main3.views.error_404'

# ? ---Tanjawi---
# urlpatterns=[
#     path("",views.home3,name="home3"),
#     path("english_bib/",views.english_bib,name="english_bib"),
#     path("arabic_bib/",views.arabic_bib,name="arabic_bib"),
#     path("french_bib/",views.french_bib,name="french_bib"),
#     path("excelTest/",views.process_file,name="home"),
#     path("clean_darija/", views.clean_data, name="home2"),
#     path("clean_excel/",views.clean_excel, name="cleanExecl") #cleanExcel will be used in href
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()




# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns=[
#     path("",views.home2,name="home2"),
#     path("",views.remove_extra_chars,name="remove_extra_chars"),
#     path("excelTest/",views.process_file,name="home"),
#     path("clean_darija/", views.clean_data, name="clean_data"),
#     path("clean_excel/",views.clean_excel, name="cleanExecl") #cleanExcel will be used in href
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)