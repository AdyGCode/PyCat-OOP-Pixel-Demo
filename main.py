import time
from random import random

from cat import Cat

if __name__ == '__main__':
    c = Cat()
    c.show()
    while True:
        time.sleep(random()*5)
        c.blink(duration=random()+0.1)
