""" https://foobar.withgoogle.com/escape_nebula
This is a great problem to learn the basic of cellular automata.
First of all, we need to simplify the 2D problem into 1D cellular automata.
To do that, we can separately compute all the valid previous states column by column and save them into a hash table.

Secondly, go over every current state's column from left to right to compute the sum of all the legit previous states.

Reference:
1. [Wikipedia](https://en.wikipedia.org/wiki/Cellular_automaton)
2. [Natural of Code](https://natureofcode.com/book/chapter-7-cellular-automata/)
3. [Idea from this blog](https://michael.kim/blog/cellular-automaton)
"""
from collections import defaultdict
# use previous state mapping to easily build columns of bits
PREVMAPPING = {
    '1': {
        ('1', '0'): [('0', '0')],
        ('0', '1'): [('0', '0')],
        ('0', '0'): [('1', '0'), ('0', '1')],
    },
    '0': {
        ('0', '1'): [('0', '1'), ('1', '1'), ('1', '0')],
        ('1', '0'): [('1', '1'), ('1', '0'), ('0', '1')],
        ('1', '1'): [('0', '0'), ('1', '0'), ('0', '1'), ('1', '1')],
        ('0', '0'): [('0', '0'), ('1', '1')]
    }
}


def solution(A):
    A = [tuple(x) for x in A]
    A = list(zip(*A))

    # build a hash table to save every valid columns to integer
    columns2num = {}
    for i, col in enumerate(A):
        if col in columns2num:
            continue
        column2bits = []
        for c in col:
            c = '1' if c else '0'
            # mapping the top cell in the column to bits
            if not column2bits:
                prev_state = []
                for k, v in PREVMAPPING[c].items():
                    for vv in v:
                        prev_state.append([k, vv])
                column2bits = prev_state
            # mapping the remained cells in the column to bits
            else:
                prev_state = []
                for i in range(len(column2bits)):
                    for k, v in PREVMAPPING[c].items():
                        if k == column2bits[i][-1]:
                            for vv in v:
                                prev_state.append(column2bits[i] + [vv])
                column2bits = prev_state

        # convert column in bits to column in integers
        bit_column = defaultdict(list)
        for state in column2bits:
            l, r = [int(''.join(x), 2) for x in zip(*state)]
            bit_column[r].append(l)
        columns2num[col] = bit_column
    print(columns2num)
    for k, v in columns2num.items():
        print(k)
        print(v)

    # use right column of previous state as k and number of valid left column
    # states and value
    nxt_col = {}
    for col in list(A):
        cur_col = columns2num[col]
        if not nxt_col:
            nxt_col = {k: len(v) for k, v in cur_col.items()}
        else:
            tmp = {}
            for k, v in cur_col.items():
                cnt = 0
                for vv in v:
                    if vv in nxt_col:
                        cnt += nxt_col[vv]
                tmp[k] = cnt
            nxt_col = tmp
    return sum(nxt_col.values())


ans = solution(
    [[True, False, True], [False, True, False], [True, False, True]])
print(ans)

# ans = solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
# print(ans)
