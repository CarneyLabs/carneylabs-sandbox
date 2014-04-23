from cookbook_text.forms import Recipe01Form
from cookbook_text.forms import Recipe02Form

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

    elif index == 2:
        if is_post:
            form = Recipe02Form(post_query)

            if form.is_valid():
                sequence = form.cleaned_data.get('sequence', '')
                conversion_method = form.cleaned_data.get('conversion_method', 'A')
                encoding_method = form.cleaned_data.get('encoding_method', 'I')

                # Characters to numeric codes...
                if conversion_method == 'A':
                    sequence = ' '.join([str(ord(character)) for character in sequence])
                # Numeric codes to characters...
                elif conversion_method == 'B':
                    # ASCII (ISO)...
                    if encoding_method == 'I':
                        sequence = ''.join([chr(int(character)) for character in sequence.split(' ')])
                    # Unicode...
                    elif encoding_method == 'U':
                        sequence = u''.join([unichr(int(character)) for character in sequence.split(' ')])

                return render(request, 'cookbook_text/recipe02.html', {
                    'sequence': sequence
                })

        form = Recipe02Form()

        return render(request, 'cookbook_text/recipe02.html', {
            'form': form
        })