# Towers of Hanoi

Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).

You have the following constraints:

(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk. Write a program to move the disks from the first tower to the
last using Stacks.

My inituition:
Let number of disk be n.
if n is odd, we move the first disk to the right most rod.
if n is even, we move the first disk to the middle rod.

base case : n = 1 or n = 2

move the layers all the way to the right rod. move the new layer to the middle rod.
form the layer on the middle rod.

first get the bottom layer to the right rod.

okay i cannot get it by pure intuition

Notes:

n = 2

```
Move disk 1 from A (source) to C (auxiliary)
Move disk 2 from A (source) to B (destination)
Move disk 1 from C (auxiliary) to B (destination)
```

n = 3 :

```
Step 1

Move disk 1 from A (source) to B (destination)
Move disk 2 from A (source) to C (auxiliary)
Move disk 1 from B (destination) to C (auxiliary)
Now we have the first two disks at C (auxiliary). The next step is to move disk 3 from A (source) to B (destination). This consists of only one step.

Step 2

Move disk 3 from A (source) to B (destination)
The last step is to move the two disks from C (auxiliary) to the destination tower B. This again involves a similar three steps with differences in the source and destination towers. The steps to move the two disks to the final destination tower is as follows.

Step 3

Move disk 1 from C (auxiliary) to A (source)
Move disk 2 from C (auxiliary) to B (destination)
Move disk 1 from A (source) to B (destination)
```

Looks like step 1 and step 3 is the same as n = 2.
We first move the top disks to the auxiliary tower, then the bottom disk to the destination tower, and lastly the top disks to the destination tower.

# Recursive case : if we know how to move the top n-1 disks, how can we move n disks.

where we divide the disks into two parts:

the first $n-1$ top disks
the last disk $n$

### Time complexity: O(2^n) because in the recursion T(n)=2T(n−1)+1

### References

https://lei-d.gitbook.io/leetcode/recursion/tower-of-hanoi
https://github.com/Data-Driven-World/d2w_notes/blob/master/Divide_Conquer.ipynb
Simulation game : https://www.mathsisfun.com/games/towerofhanoi.html
