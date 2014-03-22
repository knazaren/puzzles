__author__ = 'knazaren'
from puzzle_lib import *

if __name__ == "__main__":
    d = build_dict(poem)
    while True:
        try:
            num_letters = int(raw_input("How long would you like riddle to be (not more than 10 please) ?: "))
            if num_letters <= 10:
                print gen_riddle(d, num_letters)
            else:
                print "Are you kidding me?"
            break
        except:
            print "Wrong input"
