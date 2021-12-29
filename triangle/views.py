import math

from django.shortcuts import render

from triangle.forms import Triangle


def triangle(request):
    if request.method == 'POST':
        form = Triangle(request.POST)
        if form.is_valid():
            hypo = math.sqrt(form.cleaned_data['cath1'] ** 2 + form.cleaned_data['cath2'] ** 2)
            hypo = hypo if hypo % 1 != 0 else int(hypo)
            return render(request, 'triangle.html', {'hypo': hypo})
    else:
        form = Triangle()
    return render(request, 'triangle.html', {'form': form})
