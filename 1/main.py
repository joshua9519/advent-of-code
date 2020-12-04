from itertools import combinations
from math import prod

# BRUTE FORCE #

input = open('input', 'r')
Lines = input.readlines()
input.close()


class Solution:
    def __init__(self, lines=[]):
        self.input = lines

    def twoSum(self):
        print("BRUTE FORCE: PART 1")
        for l1 in self.input:
            for l2 in self.input:
                i1 = int(l1)
                i2 = int(l2)
                sum = i1 + i2
                if sum == 2020:
                    print("The 2 numbers which make 2020 are: {} and {}"
                          .format(l1.strip(), l2.strip()))
                    return i1*i2

    def threeSum(self):
        print("BRUTE FORCE: PART 2")
        for l1 in Lines:
            for l2 in Lines:
                for l3 in Lines:
                    i1 = int(l1)
                    i2 = int(l2)
                    i3 = int(l3)
                    sum = i1 + i2 + i3
                    if sum == 2020:
                        print("The 3 numbers which make 2020 are: {}, {}\
                              and {}"
                              .format(l1.strip(), l2.strip(), l3.strip()))
                        return i1*i2*i3


test = Solution(Lines)
print(test.twoSum())
print(test.threeSum())

# GOOD ANSWER #

with open('input', 'r') as f:
    entries = [int(i) for i in f.read().strip().splitlines()]


def solution(k):
    return next(prod(comb)
                for comb
                in combinations(entries, k)
                if sum(comb) == 2020)


print("GOOD ANSWER: PART 1")
print(solution(2))

print("GOOD ANSWER: PART 2")
print(solution(3))
