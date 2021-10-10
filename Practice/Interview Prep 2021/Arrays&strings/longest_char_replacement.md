## sliding window technique

1. the idea for sliding window technique is to have 2 pointers, start and end
1. to achieve the target, you move the end until it cannot be moved
1. once the end cannot be moved, you move the start

   - Since we are only interested in the longest valid substring, our sliding windows need not shrink, even if a window may cover an invalid substring. We either grow the window
   - by appending one char on the right, or shift the whole window to the right by one. And we only grow the window when the count of the new char exceeds the historical max
   - count (from a previous window that covers a valid substring).
   - That is, we do not need the accurate max count of the current window; we only care if the max count exceeds the historical max count; and that can only happen because of the new char.

1. in this question, the condition that the acannot be moved is when k is exceeded.
1. you would store a variable max_count which calculates the longest chain.
1. the current end is standing key "letter" for the longest chain
1. you would take the longest length and minus the chain to see if it exceeds k

## Non Optimized sol:

finding the max from dict.values() at each iteration

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s : return 0
        if k >= len(s) : return k

        char_count = collections.defaultdict(int)
        left = 0
        char_count[s[left]] += 1

        res = 0

        # keep moving to the right

        for right in range(1,len(s)):
            char_count[s[right]] += 1
            curr_count = max(char_count.values())

            if right - left + 1 - curr_count > k: #left left
                char_count[s[left]] -= 1
                left +=1


            res = max(right - left + 1,res)



        return res

# min window
# keep moving right until you cannot move right, move left
```

## Optimized solution:

Time : O(N)

Store only the max count instead of finding the max count at each index

````python
def characterReplacement(self, s, k):
        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result
        ```
````

```golang
func characterReplacement(s string, k int) int {

    // make a map which stores the string
    charMap := make(map[rune]int)
    start,maxCounter,result := 0,0,0

    // loop through the len of the string with the end as the main shifter and start as pivot
    for endIndex,endValue :=range s{

        // check if endChar in dict
        if _,ok := charMap[endValue];ok{
            charMap[endValue] +=1
        } else{
            charMap[endValue] = 1
        }


        // max counter finds the longest streak so far
        maxCounter = max(maxCounter,charMap[endValue])
        // check if the replacement exceeds k.
        if endIndex - start + 1  - maxCounter > k {
            // if it exceeds, you dont move end, and you move start instead
            // if  replacement is less than k, you continue moving end
            startChar := rune(s[start])
            charMap[startChar] --
            start ++
        }
        result = max(endIndex - start + 1,result)

    }
    return result

}

func max(a,b int) int {
    if a>b{
        return a
    }
    return b
}
```
