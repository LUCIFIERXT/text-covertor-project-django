# I HAVE CREATED THIS FILE - JASIR
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   params = {'name':'JASIR JABBAR', 'place':'PAKISTAN', 'variable':'X,Y,Z'}
   return render(request, 'index.html', params)

    # return HttpResponse('''
    #       HELLO FROM <b>JASIR JABBAR!<b> <br>
    #      <b>THIS IS JASIR'S FIRST DJANGO PROJECT HERE ARE SOME OF THE PAGE WHCIH YOU CAN TRY OR VIST :<b><br>
    #                     <a href="http://127.0.0.1:8000/about"><h1>ABOUT THIS DJANGO WEBPAGE</h1></a>
    #                     <br>
    #                     <a href="http://127.0.0.1:8000/navigator"><h1>SOCIAL LINKS NAVIGATOR</h1></a>''')


def about(request):

   params = {'name': 'JASIR JABBAR', 'place': 'PAKISTAN', 'variable': 'X,Y,Z'}

   return render(request, 'about.html', params)
    # return HttpResponse('''ABOUT MR. JASIR JABBAR<br><a href="http://127.0.0.1:8000"><h1>BACK HOME</h1></a>''')



def navigator(request):
   return render(request, 'navigator.html')
    # return HttpResponse('''<h1>YOUTUBE :</h1><a href="https://www.youtube.com/">CLICK ME FOR YOUTUBE !</a><hr>
    #                     <h1>WHATSAPP :</h1><a href="https://www.web.whatsapp.com/">CLICK ME FOR WHATSAPP !</a><hr>
    #                     <br><a href="http://127.0.0.1:8000"><h1>BACK HOME</h1></a>''')


def analyze(request):
#getting text from textarea
   djtext = request.POST.get('text', 'default')
   removepunc = request.POST.get('removepunc', 'off')
   fullcap = request.POST.get('fullcap', 'off')
   newlineremover = request.POST.get('newlineremover', 'off')
   extraspaceremover = request.POST.get('extraspaceremover', 'off')
   charcounter = request.POST.get('charcounter', 'off')

#Some Extra!
   # print("Removing Punctuation Is Checked", removepunc)
   # print(djtext)

#CHECKING WHICH OPTION IS TURNED ON!
   if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed=""

#FUNCTION
      for char in djtext:
         if char not in punctuations:
            analyzed = analyzed + char

      params = {'purpose':'Removed Puncuations', 'Analyzed_Text': analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)

   if(fullcap== "on"):
      analyzed = ""
      for char in djtext:
         analyzed = analyzed + char.upper()
      params = {'purpose': 'Changed To UPPER CASE', 'Analyzed_Text': analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)

   if(newlineremover== "on"):
      analyzed = ""
      for char in djtext:
            if char !="\n" and char!="\r":
                  analyzed= analyzed + char
      params = {'purpose':'REMOVED NEW LINES', 'Analyzed_Text':analyzed}
      djtext = analyzed
     # return render(request, 'analyze.html', params)

   if(extraspaceremover == "on"):
      analyzed = ""
      for index, char in enumerate(djtext):
          if not(djtext[index] == " " and djtext[index+1]== " "):
               analyzed = analyzed + char
      params = {'purpose': 'REMOVED NEW LINES', 'Analyzed_Text': analyzed}
      djtext = analyzed
      #return render(request, 'analyze.html', params)

   if charcounter == 'on':

      analyzed = ""
      count = 0
      for i in (djtext):
         count += 1

      params = {
         'purpose': 'Number of Characters',
         'Analyzed_Text': count 
      }
      djtext = analyzed
      # return render(request, 'analyze.html', params)


   if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcounter != "on"):
     return HttpResponse("please select any operation and try again")

   return render(request, 'analyze.html', params)


# def removepuncuations(request):
#    djtext = request.POST.get('text', 'default')
#    print(djtext)
#    return render(request, 'removepuncuations.html')
#
# def capatilizefirst(request):
#    return render(request, 'capatilizefirst.html')
#
# def newlineremove(request):
#    return render(request, 'newlineremove.html')
#
#
# def spaceremove(request):
#    return render(request, 'spaceremove.html')
