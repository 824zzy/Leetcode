""" https://leetcode.com/problems/design-a-food-rating-system/
complex but not hard to implement.
"""
from header import *


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2c = {f: c for f, c in zip(foods, cuisines)}
        self.f2r = {f: r for f, r in zip(foods, ratings)}
        self.mp = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            self.mp[c].add([-r, f])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        oldRating = self.f2r[food]
        self.mp[cuisine].remove([-oldRating, food])
        self.mp[cuisine].add([-newRating, food])
        self.f2r[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.mp[cuisine][0][1]
