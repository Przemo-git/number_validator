from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import Result

@login_required
def validate(request):
    return render(request, 'result.html')


def validate_number(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        is_valid_number = str(request.POST.get('is_valid_number'))
        name = request.POST.get('name')
        print(is_valid_number)
        print(type(is_valid_number))

        # test manual:
        # convert=int(num)
        pesel_check = list(map(int, str(is_valid_number)))
        if len(pesel_check) < 4:
            is_validate = 'pesel nieprawidłowy'
        else:
            pesel_check[3] = pesel_check[3] + 20
        print(pesel_check)
        weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        pesel_multiply = []
        if len(pesel_check) == 11:
            for index in range(len(weight)):
                pesel_multiply.append(weight[index] * pesel_check[index])
        print(pesel_multiply)
        pesel_sum = sum(pesel_multiply) % 10
        pesel_min = 10 - pesel_sum
        if pesel_min == pesel_check[-1]:
            is_validate = 'pesel prawidłowy'
        else:
            is_validate = 'pesel nieprawidłowy'


        result = is_validate

        is_valid_result = result

        Result.objects.create(is_valid_number=is_valid_number, is_valid_result=is_valid_result,
                              name=name)

        return JsonResponse({'result': is_valid_result, 'is_valid_number': is_valid_number,
                             'name': name},
                            safe=False)
