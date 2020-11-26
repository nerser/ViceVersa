from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    num_word = user_text.strip(',!?.').split(' ')
    print(type(num_word))
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversed': reversed_text, 'number_of_words': len(num_word)})
