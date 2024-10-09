from django.shortcuts import render, redirect
from django.contrib import messages
import json
import math

LEN_DATA = 51000

def home(request):
    if request.method == 'POST':
        word = request.POST['word']
        with open('./website/result.json', 'r') as file:
            data = json.load(file)
        if word in data:
            previous_guesses = request.session.get('previous_guesses', [])
            if any(guess['word'] == word for guess in previous_guesses):
                messages.success(request, "Word already guessed")
            else:
                rank = data[word] + 1
                if rank == 1:
                    progress_percentage = 100
                else:
                    progress_percentage = (math.log(LEN_DATA / data[word])) / math.log(LEN_DATA) * 100
                previous_guesses.append({
                    'word': word,
                    'rank': rank,
                    'progress_percentage': progress_percentage
                })
                previous_guesses = sorted(previous_guesses, key=lambda x: x['rank'])
                request.session['previous_guesses'] = previous_guesses
                return render(request, 'home.html', {
                    'rank': rank,
                    'word': word,
                    'progress_percentage': progress_percentage,
                    'previous_guesses': previous_guesses
                })
        else:
            messages.success(request, "Word Not Valid")
    else:
        # Clear the session data on GET request
        request.session['previous_guesses'] = []
    return render(request, 'home.html', {
        'previous_guesses': request.session.get('previous_guesses', [])
    })