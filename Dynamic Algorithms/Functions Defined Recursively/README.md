# Functions Defined Recursively
## Problem:
Be a function defines this way: 

T(a,b) = 1                      -    if a=0 or b=0

T(a,b) = T(a-1,b) + T(a,b-1)    -    otherwise

with input a, b we should find a solution T(a,b)

## Requirements:
O(a*b) time and O(a*b) space.

attention: with Naive approach it will take 2^(a*b)

## Trick:
Build a Matrix with all the sub-questions so every sub-question will be solved only once.

