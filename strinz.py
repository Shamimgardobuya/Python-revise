 python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a='Moscow'
>>> b='Mule'
>>> print(f'{a} {b}')
Moscow Mule
>>> r='florida dolphins'
>>> r.capitalize()
'Florida dolphins'
>>> greeting='Hello World'

SyntaxError: invalid syntax
>>> 
>>> you=greeting[::-1]
>>> print(you)
dlroW olleH
>>> sentence='The cat in the hat'
>>> sentence.upper()
'THE CAT IN THE HAT'
>>> sentence.lower()
'the cat in the hat'
>>> animal='fish'
>>> print(animal.lower([0] [3])
... 
... 
KeyboardInterrupt
>>> animal='fish'
>>> print(animal.lower([0] [3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(animal.lower([0][3]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print(animal.upper(animal[0] animal[3])
  File "<stdin>", line 1
    print(animal.upper(animal[0] animal[3])
                                 ^
SyntaxError: invalid syntax
>>> print(animal.upper(animal[0]+ animal[3])
... 
... 
[2]+  Stopped                 python3
student@student-ThinkPad-X250:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> animal='fish'
>>> print(animal[0,3].upper())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
>>> animal[0,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
>>> print(animal[0].upper())
F
>>> print(animal[0][3].upper())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> print(animal)
fish
>>> print(animal[0]).upper()+ [3:])
  File "<stdin>", line 1
    print(animal[0]).upper()+ [3:])
                                ^
SyntaxError: invalid syntax
>>> print(animal[0]).upper()+ animal[3:].upper())
  File "<stdin>", line 1
    print(animal[0]).upper()+ animal[3:].upper())
                                                ^
SyntaxError: unmatched ')'
>>> print('animal[0]).upper()+ animal[3:].upper()')
animal[0]).upper()+ animal[3:].upper()
>>> animal[0]).upper()+ animal[3:].upper()
  File "<stdin>", line 1
    animal[0]).upper()+ animal[3:].upper()
             ^
SyntaxError: unmatched ')'
>>> city= 'New York'
>>> city.startswith('N')
True
>>> city.endswith('k')
True
>>> animal='fish'
>>> print(f'{animal[0].upper()},{animal[-1].upper()}')
F,H
>>> print(f'{animal[0].upper()}"i s "{animal[-1].upper()}')
F"i s "H
>>> print(f'{animal[0].upper()}is{animal[-1].upper()}')
FisH
>>> print(f'{animal[0].upper()}{animal[1:-1]}{animal[-1].upper()}')
FisH
>>> animal='leopard'
>>> print(f'{animal[0].upper()}{animal[1:-1]}{animal[-1].upper()}')
LeoparD
>>> print(f'{animal[0:0].upper()}{animal[-1].upper()}')
D
>>> print(f'{animal[0:].upper()}{animal[-1].upper()}')
LEOPARDD
>>> animal='leopard'
>>> print(f'{animal[0].upper()}{}{animal[-1].upper()}')
[3]+  Stopped                 python3
student@student-ThinkPad-X250:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 


