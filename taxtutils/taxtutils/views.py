# I have created this file
from django.http import HttpResponse
from django.shortcuts import  render


def index(request):
    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext= request.POST.get('text', 'default')
    #check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspceremover = request.POST.get('extraspceremover', 'off')
    charcount = request.POST.get('charcount', 'off')



    #--------if removepunc is ON---------------------------
    if removepunc == "on":
        punctuations ='''!@#$%^&*()-_{}[];:/><.,*/`~`'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'Removed punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    #---------if Fullcaps is ON-----------------------------
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        print(djtext)

    #---------if newlineremover is On------------------------
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        print(djtext)
        # Analyze the text
        #return render(request, 'analyze.html', params)

    #---------if Extraspaces remover is ON-----------------
    if(extraspceremover =="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):

                analyzed = analyzed + char
        params = {'purpose': 'Spaces Remove', 'analyzed_text': analyzed}
        print(djtext)
        # Analyze the text
        #return render(request, 'analyze.html', params)

    #-------------if Char count is ON---------------------------
    if(charcount == "on"):
        count = 0
        for char in djtext:
            if char.isalpha():
                count = count + 1
        params = {'purpose': 'Spaces Remove', 'analyzed_text': count}

        return render(request, 'analyze.html', params)

    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and extraspceremover!="on" and charcount!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)


