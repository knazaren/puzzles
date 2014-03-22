__author__ = 'knazaren'
import re
import urllib2
import random

poem = '''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''

sowpod_dict_path = "http://www.freescrabbledictionary.com/sowpods.txt"

def build_dict(in_str):
    """
    Build a dictionary with (key, value) = (letter, number this letter appearing in the in_str)
    """
    my_dict = {}
    for c in in_str:
        if c.isalpha():
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
    return my_dict


def say_something(sym_dict, num_arr):
    """
    Spits the decoding of the riddle
    """
    the_word = "".join([sym_dict[x] for x in num_arr])
    print "I'm saying: %s" % the_word


def print_mapping(rdict):
    """
    Dump the dictionary to std.out
    """
    var = ["%s:%s" % (k, v) for k, v in rdict.items()]
    print var


def read_sowpod(path2sowpod, word_len):
    """
    read a scrabble dictionary and select a list of words of the specified length (word_len)
    if word_len is 0 or negative integer the words will not be filtered by word length
    """
    try:
        f = urllib2.urlopen(path2sowpod)
    except ValueError:
        try:
            f = open(path2sowpod)
        except:
            return []
    lines = [w for w in f.read().splitlines()[2:] if word_len <= 0 or len(w) == word_len]
    return lines


def gen_riddle(rdict, word_len=5):
    """
    This function generated the riddle of the specified length
    """
    # We need to match the fords, which only consist of letters from the original poem (keys from rdict)
    pattern_int_str = "".join(["%s" % k for k in rdict.keys()])
    pattern_str = "^[" + pattern_int_str.lower() + "]*$"
    pattern = re.compile(pattern_str)
    # Read the scrabble dictionary
    word_list = read_sowpod(sowpod_dict_path, word_len)
    word_list_to_choose_riddle_from = []
    for word in word_list:
        if pattern.match(word):
            word_list_to_choose_riddle_from.append(word)
    if len(word_list_to_choose_riddle_from) > 0:
        #randomly select a riddle
        riddle2be = random.choice(word_list_to_choose_riddle_from)
        riddle_str = "say(["
        riddle_str += ",".join(["%s" % rdict[c] for c in riddle2be.lower()])
        riddle_str += "])"
        return riddle_str
    return None