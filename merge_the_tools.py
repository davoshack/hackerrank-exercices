import ipdb

def merge_the_tools(S, k):
    for part in zip(*[iter(S)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))




if __name__ == '__main__':
    print('Enter the string:')
    S = input()
    print('Enter k')
    k = input()
    merge_the_tools(S, k)
