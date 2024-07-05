""" https://foobar.withgoogle.com/Bring_a_Gun_to_a_Trainer_Fight
1. use bfs to find all the reflected points of myself and bunny trainers
2. remove invalid angles that will shoot me first by "banned" dictionary
3. go through reflected trainer points to find valid angles
"""
from __future__ import division
from math import sqrt, atan2
from collections import defaultdict

DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def solution(DIM, S, T, lim):
    def find_candidates(sx, sy, tx, ty, mode):
        Q = [(sx, sy, 0, 0)]
        seen = set()
        while Q:
            x, y, cntx, cnty = Q.pop()
            seen.add((x, y))
            for dx, dy in DIR:
                # reflect odd/even times
                cntxx, cntyy = cntx, cnty
                xx, yy = x, y
                if dx > 0:
                    if not cntxx & 1:
                        xx = x + 2 * (M - sx)
                    else:
                        xx = x + 2 * sx
                    cntxx += 1
                elif dx < 0:
                    if not cntxx & 1:
                        xx = x - 2 * sx
                    else:
                        xx = x - 2 * (M - sx)
                    cntxx -= 1
                if dy > 0:
                    if not cntyy & 1:
                        yy = y + 2 * (N - sy)
                    else:
                        yy = y + 2 * sy
                    cntyy += 1
                elif dy < 0:
                    if not cntyy & 1:
                        yy = y - 2 * sy
                    else:
                        yy = y - 2 * (N - sy)
                    cntyy -= 1
                if (xx, yy) not in seen:
                    if mode == "m":
                        dist = sqrt((xx - sx) ** 2 + (yy - sy) ** 2)
                    elif mode == "t":
                        dist = sqrt((xx - tx) ** 2 + (yy - ty) ** 2)
                    if dist < lim:
                        seen.add((xx, yy))
                        Q.append((xx, yy, cntxx, cntyy))
        return seen

    M, N = DIM
    sx, sy = S
    tx, ty = T

    # use bfs compute all valid reflected points of me and trainer
    refected_me = find_candidates(sx, sy, tx, ty, "m")
    refected_trainer = find_candidates(tx, ty, sx, sy, "t")
    # find invalid points that shot myself
    dx, dy = sx - tx, sy - ty
    init_angle = atan2(dy, dx)

    banned = defaultdict(lambda: (float("inf"), float("inf")))
    for x, y in refected_me:
        dx, dy = sx - x, sy - y
        angle = atan2(dy, dx)
        # find angles that has minimum length
        banned[angle] = min(
            [banned[angle], (dx, dy)], key=lambda x: abs(x[0]) + abs(x[1])
        )

    ans = set([init_angle])
    for x, y in refected_trainer:
        dx, dy = sx - x, sy - y
        angle = atan2(dy, dx)
        if angle not in banned or (
            abs(dx) < abs(banned[angle][0]) and abs(dy) < abs(banned[angle][1])
        ):
            ans.add(angle)

    # corner case
    if sqrt((sx - tx) ** 2 + (sy - ty) ** 2) > lim:
        return len(ans) - 1
    else:
        return len(ans)


ans = solution([10, 10], [3, 3], [3, 5], 1)  # 0
print(ans)

ans = solution([10, 10], [4, 4], [3, 3], 5000)  # 739323
print(ans)
ans = solution([2, 5], [1, 2], [1, 4], 11)  # 27
print(ans)

ans = solution([3, 2], [1, 1], [2, 1], 4)  # 7
print(ans)
ans = solution([23, 10], [6, 4], [3, 2], 23)  # 8
print(ans)
ans = solution([300, 275], [150, 150], [185, 100], 500)  # 9
print(ans)
ans = solution([1250, 1250], [1000, 1000], [500, 400], 10000)  # 196
print(ans)
ans = solution([42, 59], [34, 34], [6, 34], 5000)  # 29279
print(ans)
