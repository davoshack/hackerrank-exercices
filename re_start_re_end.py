import re
import ipdb
def re_start_end():
    S = input()
    k = input()
    ipdb.set_trace()
    m = re.search(k, S)
    pattern = re.compile(k)

    if not m: print('(-1, -1)')
    while m:
        print('({0}, {1})'.format(m.start(), m.end()-1))
        m = pattern.search(S, m.start()+1)


if __name__ == '__main__':
    re_start_end()
