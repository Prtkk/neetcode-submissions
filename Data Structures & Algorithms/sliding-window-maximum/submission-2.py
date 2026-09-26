class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        i = 0
        for j in range(len(nums)):
            # Smaller elements behind a bigger one are useless (they can never become the max later)
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            # element at the front falls out of the window
            if i>q[0]:
                q.popleft()
        
            if j+1 >= k:
                res.append(nums[q[0]])
                i +=1
            
            j += 1

        return res
