class NumbersError(Exception):
    pass


class CyrillicError(NumbersError):
    pass


class CapitalError(NumbersError):
    pass


class TypeError(NumbersError):
    pass


def cyr(name):
    for letter in name:
        if letter not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            raise CyrillicError('Вызвано исключение CyrillicError')
        return True
    

def cap(name):
    for letter in name[1:]:
        if letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            raise CapitalError('Вызвано исключение CapitalError')
    if name[0] not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
        raise CapitalError('Вызвано исключение CapitalError')
    return True


def typ(name):
    if isinstance(name, str):
        return True
    raise TypeError('Вызвано исключение TypeError')


def name_validation(name):
    try:
        if typ(name) and cyr(name) and cap(name):
            return name
    except NumbersError as e:
        return e