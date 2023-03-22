import sys

input = open("./input.txt").readline

n = int(input())

direction = [
  [0, 1],
  [-1, 0],
  [-1, 0],
  [1, 0]
]

def dragonCurve(y, x, d, n, curve):
  curve[y][x] = 1
  