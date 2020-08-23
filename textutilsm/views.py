# i have created this file-Mamta
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    #chech checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    Newlineremover = request.POST.get('Newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    #check which checkbox is on
    if removepunc == "on":
    #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char
                 params = {'purpose': 'Remove Punctuations', 'analyzed_text':
                     analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'Changed to Uppercase', 'analyzed_text':
                analyzed}
            djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text':
                analyzed}
        djtext = analyzed


    if(Newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed = analyzed + char
            params = {'purpose': 'Removed New Line', 'analyzed_text':
                analyzed}

    if(removepunc != "on" and fullcaps!="on" and extraspaceremover != "on"  and Newlineremover!="on" ):
        return HttpResponse("Please select the operation")

    return render(request, 'analyze.html', params)
