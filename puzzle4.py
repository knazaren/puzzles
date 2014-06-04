__author__ = 'knazaren'

from array import *


def calc_volume(in_lst):
    in_array = array('i', in_lst)
    array_len = len(in_array)
    vol = 0
    if array_len < 2:
        return vol

    current_indx = in_array[0]
    in_puddle = False
    right_top = 0

    for i in range(1, array_len - 1):
        if in_array[i] <= current_indx:
            if in_puddle:
                #finish the calc
                vol += in_array[i] - current_indx
                if right_top > current_indx:
                    return vol
                return vol - (current_indx - right_top)
            else:
                #First time we start go down...
                in_puddle = 1
                right_top = current_indx
                vol = current_indx - in_array[i]

        else:
            if in_puddle:
                vol += abs(right_top - in_array[i])
                in_puddle += 1
        current_indx = in_array[i]
    return 0

if __name__ == "__main__":
    print calc_volume([2,5,1,2,3,4,7,7,6])
    print calc_volume([5,4,1])
    print calc_volume([2,5,6])
