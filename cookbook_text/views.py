from cookbook_text.forms import Recipe01Form

from django.shortcuts import render

import random


def get_random_case(character):
    i = random.randint(1, 2)

    if i % 2 == 0:
        return character.upper()
    else:
        return character.lower()


def recipe(request, index):
    index = int(index)
    is_post = request.method == 'POST'
    post_query = request.POST
    get_query = request.GET

    if index == 1:
        if is_post:
            form = Recipe01Form(post_query)

            if form.is_valid():
                string = form.cleaned_data.get('string', '')
                method = form.cleaned_data.get('method', 'A')

                # List comprehension method...
                if method == 'A':
                    word = ''.join([get_random_case(character) for character in string])
                # Map built-in function method...
                elif method == 'B':
                    word = ''.join(map(get_random_case, string))

                return render(request, 'cookbook_text/recipe01.html', {
                    'word': word
                })

        form = Recipe01Form()

        return render(request, 'cookbook_text/recipe01.html', {
            'form': form
        })