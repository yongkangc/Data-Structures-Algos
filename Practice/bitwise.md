Bitwise Operator in python
AND : &
OR : |
XOR : ^
NOT : ~
Left Shift : <<
Right Shift : >>
NOR : ~|
NAND : ~&
XNOR : ~^


```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```
So we can XOR all bits together to find the unique number. `^=` is the XOR operator.


