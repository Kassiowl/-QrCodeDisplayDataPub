import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Outside dependencies
from io import BytesIO
import json

# Entities imports
from core.entities.Person import Person
from core.entities.Github import Github
from core.entities.Linkedin import Linkedin

# Repo imports
from core.Repo_impl.PersonRepo_impl import PersonInfo
from core.Repo_impl.QrCodeGenRepo_impl import QrCodeGenRepoImpl

#Use cases imports
from core.use_cases.GetPersonInfo import GetPersonInfo
from core.use_cases.GenerateQrCode import GenerateQrCodeUseCase

# Create your views here.


def person_info(request):
        #Url Get requests
    person_name = request.GET.get('name')
    person_surname = request.GET.get('surname')
    person_last_name = request.GET.get('lastname', '')
    person_age = request.GET.get('age', '')
    person_about_me = request.GET.get('aboutme', '')
    person_github_url = request.GET.get('githuburl', '')
    person_linkedin_url = request.GET.get('linkedinurl', '')

    print("person linkedin url___")
    print(person_linkedin_url)
    context = {'name': person_name, 'surname': person_surname, 'lastname': person_last_name, 'age': person_age, 'about_me': person_about_me, 'github': person_github_url, 'linkedin':person_linkedin_url}

    return render(request, 'index.html', context)


def index(request):


    #Url Get requests
    person_name = request.GET.get('name')
    person_surname = request.GET.get('surname')
    person_last_name = request.GET.get('lastname', '')
    person_age = request.GET.get('age', '')
    person_about_me = request.GET.get('aboutme', '')
    person_github_user = request.GET.get('githubuser', '')
    person_github_contribuitions = request.GET.get('githubcontribuitions', '')
    person_linkedin_user = request.GET.get('linkedinuser', '')


    person_github = Github(f'https://github.com/{person_github_user}', person_github_user, int(person_github_contribuitions))

    person_linkedin = Linkedin(f'https://www.linkedin.com/in/{person_linkedin_user}', person_linkedin_user)

    person = Person(person_name, person_surname, person_last_name, person_about_me, person_age,
                        person_github, person_linkedin 
                    )
    
    person_info_repo = PersonInfo(person)

    person_info_use_case = GetPersonInfo(person_info_repo)
    person_result = person_info_use_case.run()
    print(type(person_result))

    print("person result___")
    print(person_result)

    URL = f'http://127.0.0.1:7000/api/personDisplayData?name={person_result["Name"]}&surname={person_result["Surname"]}&lastname={person_result["lastname"]}&age={person_result["age"]}&aboutme={person_result["about_me"]}&githuburl={person_result["github_url"]}&linkedinurl={person_result["linkedin_url"]}/'
    print(URL)
    qrcode_person = QrCodeGenRepoImpl(URL)

    qrcode_use_case = GenerateQrCodeUseCase(qrcode_person)

    qrcode_img = qrcode_use_case.run()
    
    img_bytes = BytesIO()
    qrcode_img.save(img_bytes)
    img_bytes.seek(0)
    

    # return image as API response
    response = HttpResponse(img_bytes, content_type='image/png')
    return response
