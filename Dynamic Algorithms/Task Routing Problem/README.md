# Task Routing Problem
## Problem:
In a factory there is 2 identical production lines with 'n' stages each.
For moving between each stage you need to pay. 
We want to pay the minimal price possible.

## The Input:
Graph: G = (V,E)
Costs: x_1,..,x_n,a_2,..,a_n-1,y_1,..,y_n,b_2,..,b_n-1
Two Nodes: s, t

## Output
Minimal Path from s to t.

## Requirements:
O(n) time and O(n) space.

Note: Dijkstra solution will solve it with O(n*log(n)) time.
But we have another assumptions on the problem, so we can do better.

## Trick:
Build 2 arrays with all the sub-questions so every sub-question will be solved only once.

We split the problem to min distance for n-1 nodes for the upside and n-1 for the downside.
So:
p_u[k] = x_n           if k = n-1
p_d[k] = min(x_k+1 + p_u[k+1], a_k+1 + p_d[k+1])   else
