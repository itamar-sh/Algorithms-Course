## Assignment Of Tasks
This is the **second** problem we come to solve in the Greedy Algorithm Section.

### The Problem
We have n tasks, each task represent as segment in $\mathbb{R}$.

We can denote each segment with $s_i$ and $f_i$ for start an end of segment.

We want to return subgroup of the [n] such that each task is strangers to each other
and the time of the subgroup is the biggest.

### Input
List of n int's represent time of start of each task.

List of n int's represent time of finish of each task.

### Output
List of k int's represent the tasks we chose. 

### Example 1
we want to consider the folowwing tasks:
[0,2],[1,3],[2,4]
So the first list, start time:
[0,1,2]
And The second list. finish time:
[2,3,4]
The optimal result are this tasks:
[0,2],[2,4]
So The output should be:
[0,2]
Because we chose the 0 task and the 2 task.

## Algorithm For Solution
Each iteration we take the task that will finish first.