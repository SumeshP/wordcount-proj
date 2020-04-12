from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return HttpResponse('Hello')

def homepage(request):
    return render(request, 'home.html', {'Creator':'Sumesh', 'Date':'06-Dec-2019'})

def about(request):
    return render(request, 'about.html')

def homepages(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext) #prints in terminal
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    #return render(request, 'count.html')
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords })