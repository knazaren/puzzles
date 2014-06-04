__author__ = 'knazaren'

letters = "acdegilmnoprstuw"


def hash(s):
    h = 7
    for i in range(len(s)):
        h = (h * 37 + letters.index(s[i]))
    return h


def rhash(hash_key, str_len):
    out_str = ""
    curr_hash = hash_key
    for i in range(str_len):
        curr_hash, pos = divmod(curr_hash, 37)
        out_str = letters[pos] + out_str
    return out_str


if __name__ == "__main__":
    print hash("leepadg")
    print rhash(680131659347, 7)
    print rhash(910897038977002, 9)