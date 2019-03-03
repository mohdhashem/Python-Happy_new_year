import time
from random import randint
import os

os.system("C:\\Users\\m7ama\\source\\repos\\pyProject\\pyProject\\music.bat")

for i in range(1,45):
    print('')

s = ''

for i in range(1,1000):
    count = randint(1, 100)
    while (count > 0):
        s += ' '
        count -= 1

    if (i % 10 == 0):
        print(s + 'Happy New Year')
    elif (i % 17 == 0):
        print(s + 'Merry Christmas')
    else:
        print(s + '*')

    s = ''
    time.sleep(0.3)  # by Mohammad Hashem :D