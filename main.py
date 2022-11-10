from typing import List, Callable

import second
from teste_pacote import ola_pacote

class Hint():
    pass

def main():
    print('main...')
    second.ola()
    

def hint(text: str) -> str:
    print(text)
    return f'[{text}]'


def logger_builder(prefix: str) -> Callable[[str], str]:
    func: Callable[[str], str] = lambda txt: f'{prefix} : {txt}'

    return func


if __name__ == '__main__':
    main()
    text = 'text'
    print(type(text))
    text = 190
    print(type(text))
    ola_pacote()

    array1 = list()
    array2 = []
    dict1 = dict()
    dict2 = {}

    print(hint('99'))

    array1 = list(range(10))
    print(array1)
    for i in array1:
        array2.append(i ** 2)
    
    print(array2)

    print([n ** 2 for n in range(10)])
    print(list(map(lambda n: n**2, range(10))))

    print([n ** 2 for n in range(10) if (n % 2) == 0])
    print(list(filter(lambda el: (el % 2) == 0, list(map(lambda n: n**2, range(10))))))

    if Hint():
        print(True)
    else:
        print(False)

    logger_f = logger_builder('prefixo=>')
    print(logger_f('ola builder'))
    print(logger_f('bye builder'))

class Logger(object):
    def __init__(self, prefix: str):
        self.prefix = prefix

    def log(self, txt: str) -> str:
        return f'{self.prefix} : {txt}'

logger_obj = Logger('prefixo=>')
print(logger_obj.log('ola log object'))
print(logger_obj.log('bye log object'))

class Gambiarra(object):
    def __init__(self):
        self.prefix = 'gabiarra funciona...'    

print(Logger.log(Gambiarra(), 'ola gambiarra'))
