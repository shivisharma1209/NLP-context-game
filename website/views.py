from django.shortcuts import render, redirect
from django.contrib import messages
import json


def home(request):
    if request.method == 'POST':
        word = request.POST['word']
        # list = request.POST['list']
        with open('./website/result.json', 'r') as file:
            data = json.load(file)
        if word in data:
            print(data[word])
            progress_percentage = 100 - data[word] * 100 / len(data)
            return render(request, 'home.html', {'rank': data[word]+1, 'word': word, 'progress_percentage': progress_percentage})
        messages.success(request, "Word Not Valid")
    return render(request, 'home.html', {})


