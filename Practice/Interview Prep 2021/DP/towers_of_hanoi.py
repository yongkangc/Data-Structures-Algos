
# The is to move the n-1 disks from source to auxilary rod
# and then move the nth disk from source to destination rod
# then move the


# Time complexity:
#  O(2^n) because in the recursion  T(n)=2T(n−1)+1


# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
n = 5
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
