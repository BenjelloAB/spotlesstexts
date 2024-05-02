from django.shortcuts import render
from .bib import *
from .bib_fr import *
from .bib_ar import *
from django.http import HttpResponse,JsonResponse
import pandas as pd
import io
from .bib_eng import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.

# main_page
# @login_required(login_url='login')
def mainPage(response):
    return render(response,'main3/mainpage.html',{})




# ! login stuff
def registerPage(response):
    if response.user.is_authenticated:
        return redirect('MainPage')
    else:
        form = CreateUserForm()
        if response.method == 'POST':
            form = CreateUserForm(response.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(response,'Account was created for ' + user)
                return redirect('login')
        return render(response,"main3/register.html",{'form': form})


def loginPage(response):
    if response.user.is_authenticated:
        return redirect('MainPage')
    else:
        if response.method == 'POST':
            username = response.POST.get('username')
            password = response.POST.get('password')
            user = authenticate(response, username=username, password=password)
    # ? check if the user is actually there in DB before redirecting:
            if user is not None:
                login(response, user)
                # ? so we are gonna log this specific "user"  in user object contains all infos
                return redirect('MainPage')
            else:
                messages.info(response, 'Username Or Password is incorrect')
                

        return render(response,"main3/login.html",{})


def logoutUser(response):
    logout(response)
    return redirect('MainPage')

# @login_required(login_url='login')
# def home(response):
#     return render(response,"main3/dash.html",{})


# ! login stuff


@login_required(login_url='login')
def clean_english(response):
    return render(response,'main3/EnglishClean.html',{})


#? english bib-NO AJAX
# @login_required(login_url='login')
# def english_bib(response):

#   #  time.sleep(5)

#     options_dict = {
#         'f1': remove_urlsE,
#         'f2': remove_numbersE,
#         'f3': remove_extra_whitespaceE,
#         'f4': remove_emailsE,
#         'f5': remove_special_charactersE,
#         'f6': stop_wordsE,
#         'f7': remove_non_english_wordsE
        
#     }

#     if response.method == 'POST':
#         options = response.POST.getlist('option[]')
#         txt = response.POST.get('text')
#         txtIni = txt
#         # print(response.POST)
#         # print(txt)
        
    
#         # Apply all functions except 'f7'
#         for option in options:
#             if option in options_dict and (option != 'f8' or option != 'f9' or option != 'f10'):
#                 txt = options_dict[option](txt)

#         txt = str(txt)
#         # if 'f8' in options:
#         #     txt = stem_wordsE(txt)
       
#         if 'f9' in options:
#             txt = lemmatizer_engE(txt)

#         if 'f10' in options:
#             txt = token_white_spaceE(txt)
            
    
       
#         # txt = lemmatizer_engE(txt)
#         # for option in options:
#         #     if option in options_dict:
#         #         txt = options_dict[option](txt)

#         return render(response, "main3/EnglishClean.html", {'string':txt,'textini':txtIni})
#     else:
#         pass

#     return render(response, "main3/EnglishClean.html", {'string':'','textini':''})

# ?Ajax Stuff English start
@login_required(login_url='login')
def english_bib(response):
    return render(response, "main3/EnglishClean.html", {'string':'','textini':''})

def english_bib_handle(response):

  #  time.sleep(5)

    options_dict = {
        'f1': remove_urlsE,
        'f2': remove_numbersE,
        'f3': remove_extra_whitespaceE,
        'f4': remove_emailsE,
        'f5': remove_special_charactersE,
        'f6': stop_wordsE,
        'f7': remove_non_english_wordsE
        
    }

    if response.method == 'POST':
        txt = response.POST.get('text_input')
        options = response.POST.getlist('selected_values[]')
        print(options)
        print(txt)
        txtIni = txt
        # print(response.POST)
        # print(txt)
        
    
        # Apply all functions except 'f7'
        for option in options:
            if option in options_dict and (option != 'f8' or option != 'f9' or option != 'f10'):
                txt = options_dict[option](txt)

        txt = str(txt)
        # if 'f8' in options:
        #     txt = stem_wordsE(txt)
       
        if 'f9' in options:
            txt = lemmatizer_engE(txt)

        if 'f10' in options:
            txt = token_white_spaceE(txt)
            
    
       
        # txt = lemmatizer_engE(txt)
        # for option in options:
        #     if option in options_dict:
        #         txt = options_dict[option](txt)

        print(txt)
        return JsonResponse({'string':txt})
  
    return JsonResponse({})

# ?Ajax Stuff English end

# ? darija NO AJAX
# @login_required(login_url='login')
# def clean_data(response):
#     options_dict = {
#         'f1': normalize,
#         'f2': remove_diacritics,
#         'f3': remove_urls,
#         'f4': remove_numbers,
#         'f5': remove_extra_whitespace,
#         'f6': remove_emails,
#         'f7': remove_special_characters,
#         'f8': remove_stopwords,
#         'f9': remove_non_arabic_words,
#         'f10': remove_non_arabic_symbols
        
#     }

#     if response.method == 'POST':
#         options = response.POST.getlist('option[]')
#         txt = response.POST.get('text')
#         txtIni = txt
#         print(response.POST)

#         # Apply all functions except 'f12'
#         for option in options:
#             if option in options_dict and (option != 'f12' or option != 'f11'):
#                 txt = options_dict[option](txt)

#         # Apply 'f12' function
#         if 'f12' in options:
#             txt = tokenize_ch_spec(txt)
       
#         if 'f11' in options:
#             txt = token_white_space(txt)

#         return render(response, "main3/home2.html", {'string':txt,'textini':txtIni})
#     else:
#         pass

#     return render(response, "main3/home2.html", {'string':'','textini':''})


# ?new Ajax stuff
@login_required(login_url='login')
def clean_data(response):
    return render(response, "main3/home2.html", {'string':'','textini':''})

def darija_bib_handle(response):
    options_dict = {
        'f1': normalize,
        'f2': remove_diacritics,
        'f3': remove_urls,
        'f4': remove_numbers,
        'f5': remove_extra_whitespace,
        'f6': remove_emails,
        'f7': remove_special_characters,
        'f8': remove_stopwords,
        'f9': remove_non_arabic_words,
        'f10': remove_non_arabic_symbols
        
    }

    if response.method == 'POST':
        txt = response.POST.get('text_input')
        options = response.POST.getlist('selected_values[]')
        txtIni = txt
        print(response.POST)
        print(txt)
        print(options)

        # Apply all functions except 'f12'
        for option in options:
            if option in options_dict and (option != 'f12' or option != 'f11'):
                txt = options_dict[option](txt)

        # Apply 'f12' function
        if 'f12' in options:
            txt = tokenize_ch_spec(txt)
       
        if 'f11' in options:
            txt = token_white_space(txt)

        return JsonResponse({'string':txt})
    return JsonResponse({})
    
# ?End new Ajax stuff
@login_required(login_url='login')
def clean_excel(response):
    return render(response, "main3/exceltest.html", {})

@login_required(login_url='login')
def home2(response):
    return render(response,"main3/home2.html",{})


@login_required(login_url='login')
def home3(response):
    return render(response, "main3/darija_bib_main.html", {})


@login_required(login_url='login')
def home4(response):
    return render(response,'main3/home4.html.html',{})


@login_required(login_url='login')
def french_bib_main(response):
    return render(response,'main3/french_bib_main.html',{})


@login_required(login_url='login')
def english_bib_main(response):
    return render(response,'main3/english_bib_main.html',{})


@login_required(login_url='login')
def arabic_bib_main(response):
    return render(response,'main3/arabic_bib_main.html',{})
# darija
@login_required(login_url='login')
def process_file(request):
    options_dict = {
        
        'f2': remove_diacritics,
        'f3': remove_urls,
        'f4': remove_numbers,
        'f5': remove_extra_whitespace,
        'f6': remove_emails,
        'f7': remove_special_characters,
        'f8': remove_stopwords,
        'f9': remove_non_arabic_words,
        'f10': remove_non_arabic_symbols
        
    }
       
    if request.method == 'POST' and request.FILES['myfile']:
        #! get the uploaded file
        file = request.FILES['myfile']
        options = request.POST.getlist('option[]')

        #! read the excel file into a pandas DataFrame
        df = pd.read_excel(file, header=None)

        #! apply regex expression to each row of the DataFrame
        for index, row in df.iterrows():
             for option in options:
                if option in options_dict:  
            #! modify the row using regex expression
                    df = df.applymap( options_dict[option])
       
            

        #! create a response object for the new excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="modified_file.xlsx"'

        #! write the modified DataFrame to a new excel file
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=False)

        return response

    return render(response,"main3/exceltest.html",{})

@login_required(login_url='login')
def english_bib_main_ex(response):
    return render(response,'main3/exceltestEng.html',{})


@login_required(login_url='login')
def arabic_bib_main_ex(response):
    return render(response,'main3/exceltestAR.html',{})

@login_required(login_url='login')
def french_bib_main_ex(response):
    return render(response,'main3/exceltestFR.html',{})


@login_required(login_url='login')
def process_file_eng(request):
    options_dict = {
        'f1': remove_urlsE,
        'f2': remove_numbersE,
        'f3': remove_extra_whitespaceE,
        'f4': remove_emailsE,
        'f5': remove_special_charactersE,
        'f6': stop_wordsE,
        'f7': remove_non_english_wordsE,
        'f9': lemmatizer_engE,
        'f10': token_white_spaceE
    }
       
    if request.method == 'POST' and request.FILES['myfile']:
        #! get the uploaded file
        file = request.FILES['myfile']
        options = request.POST.getlist('option[]')

        #! read the excel file into a pandas DataFrame
        df = pd.read_excel(file, header=None)

        #! apply regex expression to each row of the DataFrame
        for index, row in df.iterrows():
             for option in options:
                if option in options_dict:  
                   
            # #! modify the row using regex expression
                    df = df.applymap( options_dict[option])
       
            

        #! create a response object for the new excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="modified_file.xlsx"'

        #! write the modified DataFrame to a new excel file
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=False)

        return response

    return render(response,"main3/exceltestEng.html",{})


@login_required(login_url='login')
def process_file_fr(request):
    options_dict = {
        'f1': remove_urlsF ,
        'f2': remove_numbersF,
        'f3': remove_extra_whitespaceF,
        'f4': remove_emailsF,
        'f5': remove_special_charactersF,
        'f6': remove_stop_wordsF,
        'f7': remove_non_french_words,
        'f8': lemm_wordsF,
        'f10': return_token,
        'f11': return_token_sent,
    }
       
    if request.method == 'POST' and request.FILES['myfile']:
        #! get the uploaded file
        file = request.FILES['myfile']
        options = request.POST.getlist('option[]')

        #! read the excel file into a pandas DataFrame
        df = pd.read_excel(file, header=None)

        #! apply regex expression to each row of the DataFrame
        for index, row in df.iterrows():
             for option in options:
                if option in options_dict:  
            #! modify the row using regex expression
                    df = df.applymap( options_dict[option])
       
            

        #! create a response object for the new excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="modified_file.xlsx"'

        #! write the modified DataFrame to a new excel file
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=False)

        return response

    return render(response,"main3/exceltest.html",{})


@login_required(login_url='login')
def process_file_ar(request):
    options_dict = {
        'f1': normalize,
        'f2': remove_diacritics,
        'f3': remove_urlsA ,
        'f4': remove_numbersA,
        'f5': remove_extra_whitespaceA,
        'f6': remove_emailsA,
        # 'f7': remove_non_arabic_symbolsA,
        'f7': remove_special_charactersA,
        'f8': remove_stop_wordsA, 
        'f9': remove_non_arabic_words,
        'f10': lemmaA,
        'f12': token_white_spaceA
    }
       
    if request.method == 'POST' and request.FILES['myfile']:
        #! get the uploaded file
        file = request.FILES['myfile']
        options = request.POST.getlist('option[]')

        #! read the excel file into a pandas DataFrame
        df = pd.read_excel(file, header=None)

        #! apply regex expression to each row of the DataFrame
        for index, row in df.iterrows():
             for option in options:
                if option in options_dict:  
            #! modify the row using regex expression
                    df = df.applymap( options_dict[option])
       
            

        #! create a response object for the new excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="modified_file.xlsx"'

        #! write the modified DataFrame to a new excel file
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, header=False)

        return response

    return render(response,"main3/exceltestAR.html",{})




#? arabic bib no AJAX
# @login_required(login_url='login')
# def arabic_bib(response):

#   #  time.sleep(5)

#     options_dict = {
#         'f1': normalize,
#         'f2': remove_diacritics,
#         'f3': remove_urlsA ,
#         'f4': remove_numbersA,
#         'f5': remove_extra_whitespaceA,
#         'f6': remove_emailsA,
#         # 'f7': remove_non_arabic_symbolsA,
#         'f7': remove_special_charactersA,
#         'f8': remove_stop_wordsA, 
#         'f9': remove_non_arabic_words 
#     }

#     if response.method == 'POST':
#         options = response.POST.getlist('option[]')
#         txt = response.POST.get('text')
#         txtIni = txt
#         # print(response.POST)
#         # print(txt)
        
    
#         # Apply all functions except 'f7'
#         for option in options:
#             if option in options_dict and (option != 'f10' or option != 'f11' or option != 'f12'):
#                 txt = options_dict[option](txt)

#         # txt = str(txt)
#         if 'f12' in options:
#             txt = token_white_spaceA(txt)    
#         # if 'f11' in options:
#         #     txt = stem_arabic_text(txt)

#         if 'f10' in options:
#             txt = lemmaA(txt)
#         # txt = lemmatizer_engE(txt)
#         # for option in options:
#         #     if option in options_dict:
#         #         txt = options_dict[option](txt)

#         return render(response, "main3/arabic_bib.html", {'string':txt,'textini':txtIni})
#     else:
#         pass

#     return render(response, "main3/arabic_bib.html", {'string':'','textini':''})
# ? Ajax Stuff Arabic
@login_required(login_url='login')
def arabic_bib(response):
    return render(response, "main3/arabic_bib.html", {'string':'','textini':''})

@login_required(login_url='login')
def arabic_bib_handle(response):

  #  time.sleep(5)

    options_dict = {
        'f1': normalize,
        'f2': remove_diacritics,
        'f3': remove_urlsA ,
        'f4': remove_numbersA,
        'f5': remove_extra_whitespaceA,
        'f6': remove_emailsA,
        # 'f7': remove_non_arabic_symbolsA,
        'f7': remove_special_charactersA,
        'f8': remove_stop_wordsA, 
        'f9': remove_non_arabic_words 
    }

    if response.method == 'POST':
        txt = response.POST.get('text_input')
        options = response.POST.getlist('selected_values[]')
        print(options)
        print(txt)
        txtIni = txt
        # print(response.POST)
        # print(txt)
        
    
        # Apply all functions except 'f7'
        for option in options:
            if option in options_dict and (option != 'f10' or option != 'f11' or option != 'f12'):
                txt = options_dict[option](txt)

        # txt = str(txt)
        if 'f12' in options:
            txt = token_white_spaceA(txt)    
        # if 'f11' in options:
        #     txt = stem_arabic_text(txt)

        if 'f10' in options:
            txt = lemmaA(txt)
        # txt = lemmatizer_engE(txt)
        # for option in options:
        #     if option in options_dict:
        #         txt = options_dict[option](txt)

        return JsonResponse({'string':txt})
    return JsonResponse({})

# ?Ajax Stuff arabic End

#? FRENCH bib NO AJAX
# @login_required(login_url='login')
# def french_bib(response):

    

#   #  time.sleep(5)

#     options_dict = {
#         'f1': remove_urlsF ,
#         'f2': remove_numbersF,
#         'f3': remove_extra_whitespaceF,
#         'f4': remove_emailsF,
#         'f5': remove_special_charactersF,
#         'f6': remove_stop_wordsF
#         # 'f7': remove_non_french_words
#     }

#     if response.method == 'POST':
#         options = response.POST.getlist('option')
#         txt = response.POST.get('text')
#         txtIni = txt
#         # print(response.POST)
#         # print(txt)
        
    
#         # Apply all functions except 'f7'
#         for option in options:
#             if option in options_dict and (option != 'f8' or option != 'f9' or option != 'f10' or option != 'f11'):
#                 txt = options_dict[option](txt)
#         txt = str(txt)
#         if 'f8'  in options:
#             txt = lemm_wordsF(txt)

#         # if 'f9' in options:
#         #     txt = return_stem(txt)

#         if 'f10' in options:
#             txt = return_token(txt)  

#         if 'f11' in options:
#             txt = return_token_sent(txt)    
      
#         # txt = lemmatizer_engE(txt)
#         # for option in options:
#         #     if option in options_dict:
#         #         txt = options_dict[option](txt)

#         # return render(response, "main3/french_bib.html", {'string':txt,'textini':txtIni})
#         return HttpResponse({'string':txt})
#     else:
#         pass

#     return render(response, "main3/french_bib.html", {'string':'','textini':''})


# ?Ajax Stuff French 
@login_required(login_url='login')
def french_bib(response):
    return render(response, "main3/french_bib.html", {'string':'','textini':''})



import urllib.parse
import json
def french_bib_handle(response):
    options_dict = {
        'f1': remove_urlsF ,
        'f2': remove_numbersF,
        'f3': remove_extra_whitespaceF,
        'f4': remove_emailsF,
        'f5': remove_special_charactersF,
        'f6': remove_stop_wordsF,
        'f7': remove_non_french_words
    }

    if response.method == 'POST':
        # options = response.POST.getlist('options')
        # txt = response.POST.get('text')
        # print(options)
        # print(txt)
        txt = response.POST.get('text_input')
        options = response.POST.getlist('selected_values[]')
        print(options)
        print(txt)

        # json_data = json.loads(response.POST.get('json_data'))
        # print(json_data)
        # options = json_data['values']
        # txt = response.POST.get('text')
        # txt = urllib.parse.unquote(txt1)
        txtIni = txt
        # print(response.POST)
        # print(txt)
        
    
        # Apply all functions except 'f7'
        for option in options:
            if option in options_dict and (option != 'f8' or option != 'f9' or option != 'f10' or option != 'f11'):
                txt = options_dict[option](txt)
        txt = str(txt)
        if 'f8'  in options:
            txt = lemm_wordsF(txt)

        # if 'f9' in options:
        #     txt = return_stem(txt)

        if 'f10' in options:
            txt = return_token(txt)  

        if 'f11' in options:
            txt = return_token_sent(txt)    
      
        # txt = lemmatizer_engE(txt)
        # for option in options:
        #     if option in options_dict:
        #         txt = options_dict[option](txt)

        # return render(response, "main3/french_bib.html", {'string':txt,'textini':txtIni})
        print('3333333333333333333')
        print(txt)
        return JsonResponse({'string':txt})
  
    return JsonResponse({})


from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('MainPage')



# ?Ajax Stuff french end








def error_404(response, exception):
    return render(response,'main3/404page.html',{})