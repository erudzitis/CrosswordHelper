
from django.http import JsonResponse
from django.shortcuts import render
import os
from django.template.loader import render_to_string


def main(request):
    if request.method == 'POST':
        input_word = request.POST.get('content')
        indexes = [i for i, ltr in enumerate(input_word) if not ltr == "x"]
        cString = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "\crossword_dict", str(len(input_word)) + ".txt")

        foundMatchingWords = []

        with open(cString, "r", encoding="utf8") as writer:
            all_lines = writer.readlines()
            for word in all_lines:
                if (goalWord(word, input_word, indexes)):
                    foundMatchingWords.append(word)

        html = render_to_string('main/result.html', {'foundMatchingWords': foundMatchingWords}, request=request)
        return JsonResponse({'form': html})

    return render(request, 'main/main.html')

def goalWord(word, input_word, indexes):
    totalCounted = 0
    for current_index in indexes:
        if input_word[current_index] == word[current_index]:
            totalCounted = totalCounted + 1

    if (totalCounted == len(indexes)):
        return True
    else:
        return False