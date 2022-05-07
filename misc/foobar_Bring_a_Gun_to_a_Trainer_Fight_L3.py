""" https://foobar.withgoogle.com/Bring_a_Gun_to_a_Trainer_Fight
"""
from __future__  import division
from math import sqrt, atan2
from collections import defaultdict
DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def solution(DIM, S, T, lim):
    def find_candidates(sx, sy, tx, ty):
        Q = [(sx, sy, 0, 0)]
        seen = set()
        while Q:
            x, y, cntx, cnty = Q.pop()
            seen.add((x, y))
            for dx, dy in DIR:
                # reflect odd/even times
                cntxx, cntyy = cntx, cnty
                xx, yy = x, y
                if dx>0:
                    if not cntxx&1: xx = x+2*(M-sx)
                    else: xx = x+2*sx
                    cntxx += 1
                elif dx<0:
                    if not cntxx&1: xx = x-2*sx                    
                    else: xx = x-2*(M-sx)
                    cntxx -= 1
                if dy>0:
                    if not cntyy&1: yy = y+2*(N-sy)
                    else:  yy = y+2*sy
                    cntyy += 1
                elif dy<0:
                    if not cntyy&1: yy = y-2*sy
                    else: yy = y-2*(N-sy)
                    cntyy -= 1
                if (xx, yy) not in seen and sqrt((xx-tx)**2+(yy-ty)**2)<lim:
                    seen.add((xx, yy))
                    Q.append((xx, yy, cntxx, cntyy))
        return seen
            
    M, N = DIM
    sx, sy = S
    tx, ty = T

    # use bfs compute all valid reflected points of me and trainer
    refected_me = find_candidates(sx, sy, tx, ty)
    refected_trainer = find_candidates(tx, ty, sx, sy)
    # find invalid points that shot myself
    dx, dy = sx-tx, sy-ty
    init_angle = atan2(dy, dx)
    # print("init_angle:", init_angle)

    # banned = {init_angle: (dx, dy)}
    banned = defaultdict(lambda: (float('inf'), float('inf')))
    for x, y in refected_me:
        dx, dy = sx-x, sy-y
        angle = atan2(dy, dx)

        banned[angle] = min(banned[angle], (dx, dy))
    #     print(x, y, dx, dy, angle)
    # print("banned: ", banned)
    
    ans = set([init_angle])
    # ans = set()
    for x, y in refected_trainer:
        dx, dy = sx-x, sy-y
        angle = atan2(dy, dx)
        if angle not in banned or (abs(dx)<=abs(banned[angle][0]) and abs(dy)<=abs(banned[angle][1])):
            ans.add(angle)
            # print(x, y, dx, dy, '|', angle)
        # else: print(x, y, dx, dy, angle)
        # ans.add(angle)
        
    # print(ans)
    # print(len(ans|banned))
    return len(ans)


    # banned = set()
    # for x, y in refected_trainer:
    #     if x==sx and y==sy: continue
    #     dx, dy = tx-x, ty-y
    #     angle = atan2(dy, dx)
    #     banned.add(angle)
    #     print(x, y, dx, dy, angle)
    # print("banned: ", banned)

    # for x, y in refected_me:
    #     if x==sx and y==sy: continue
    #     dx, dy = tx-x, ty-y
    #     angle = atan2(dy, dx)
    #     if angle not in banned:
    #         ans.add(angle)
    #     else: print(x, y, dx, dy, angle)
    #     # ans.add(angle)
    #     # print(x, y, dx, dy, '|', angle)
    # print(ans)
    # print(len(ans|banned))
    # return len(ans)
    

ans = solution([10,10], [4,4], [3,3], 5000) # 739323
print(ans)
ans = solution([2,5], [1,2], [1,4], 11) # 27
print(ans)

ans = solution([3,2], [1,1], [2,1], 4) # 7
print(ans)
ans = solution([23,10], [6,4], [3,2], 23) # 8
print(ans)
ans = solution([300,275], [150,150], [185,100], 500) # 9
print(ans)
ans = solution([1250,1250], [1000,1000], [500,400], 10000) # 196
print(ans)
ans = solution([42,59], [34,34], [6,34], 5000) # not 31694
print(ans)
"""
int[] dimensions = new int[] {42, 59};
int[] captain_position = new int [] {34, 44};
int[] badguy_position = new int[] {6, 34};
int distance = 5000;
//Desired Output: ??? (Unknown)
//Actual Output: 31694 (Incorrect)

"""
