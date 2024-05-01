from tkinter import N
import numpy as np


def min_time(cpus, n):
    timetable = np.zeros(len(cpus), dtype='int')
    task_count = np.zeros(len(cpus), dtype='int')
    while n > 0:
        temp = timetable
        for i in range(len(temp)):
            temp[i] = cpus[i] * pow((task_count[i] + 1), 2)
        min_idx = np.argmin(temp)
        timetable[min_idx] = temp[i]
        task_count[min_idx] += 1
        n -= 1
    for i in range(len(timetable)):
        timetable[i] = cpus[i] * pow((task_count[i]), 2)
    return np.max(timetable)


cpus = [
    [4, 2, 3, 1],
    [5, 1, 8],
    [1, 2, 2, 1, 2, 3, 2, 2, 2],
    [1, 2, 2, 1, 2, 3, 2, 2, 2]
]
n = [10, 6, 4, 15]
for c, n in zip(cpus, n):
    print(min_time(c, n))
