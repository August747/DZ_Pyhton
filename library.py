number: int = 5
MSG_DEFAULT_NUMBER = 'Enter number (ex. 5.00 or 50) >>>> '


def get_ukrainian_coins(number: int, last_number=None) -> str:
    last_number = int(str(number)[-1])
    if number == 0 or number in range(5, 21) or last_number == 0:
        result = 'копійок'
    elif number == 1 or last_number == 1:
        result = 'копійка'
    elif number in [2, 3, 4] or last_number in [2, 3, 4]:
        result = 'копійки'
    else:
        result = 'копійок'

    return result


def get_ukrainian_hryvnas(number: int, last_number=None) -> str:
    last_number = int(str(number)[-1])
    if number == 0 or number in range(5, 21) or last_number == 0:
        result = 'гривень'
    elif number == 1 or last_number == 1:
        result = 'гривня'
    elif number in [2, 3, 4] or last_number in [2, 3, 4]:
        result = 'гривні'
    else:
        result = 'гривень'

    return result


def get_money(number: int, list_of_money = None ) -> str:
    number.split('.')
