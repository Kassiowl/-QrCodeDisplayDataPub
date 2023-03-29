# Introduction
<p>I'm doing this application in clean architecture, since the application is small and i don't have a more 
clear context of the business rules, i decided to split as i would imagine this cenario </p>

## Clean Architecture overview image
![Clean Architecture ](CleanArchitecture.jpg)


## This project Architecture
![Project Architecture](architecture.png)


## Tecnology Stack
* Django 
* React

## Repo - Repositories 

  > Interfaces Definitions
  * QrCodeGen
      * gen()
      * gen_url()

## Repo_impl - Repositories implementation
  > Concrete classes
  * QrCodeGen
      * gen()
      * get_url()  

## Entities
    linkedin
    github
    Person
    * Has a linkedin
    * Has a github


## Use Cases
    *   GenerateQrCode
    *   RedirectQrCode
    *   GetPersonInfo

# Django Api
## Request example:
## QR CODE
> /api/?name=john&surname=william&lastname=Oliver&age=21&aboutme=loremipsum&githubuser=john&githubcontribuitions=300&linkedinuser=oliverwilliam

## PERSON INFO
> api/personDisplayData?name=john&surname=william&lastname=Oliver&age=21&aboutme=loremipsum&githuburl=https://github.com/john&linkedinurl=https://www.linkedin.com/in/oliverwilliam