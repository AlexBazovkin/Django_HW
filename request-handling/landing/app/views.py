from collections import Counter
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing

    result = request.GET.get('from-landing')
    counter_click.update([result])

    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # return render(request, 'landing.html')

    result = request.GET.get('ab-test-arg')
    counter_show.update([result])

    if result == 'test':
        return render(request, 'landing_alternate.html')

    if result == 'original':
        return render(request, 'landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    if counter_show['test'] != 0:
        count_test = round(counter_click['test'] / counter_show['test'], 1)
    else:
        count_test = 'Не было показов'

    if counter_show['original'] != 0:
        count_original = round(counter_click['original'] / counter_show['original'], 1)
    else:
        count_original = 'Не было показов'

    return render(request, 'stats.html', context={
        'test_conversion': count_test,
        'original_conversion': count_original,
    })
