# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        length = len(people)
        left = 0
        right = length - 1
        boat = 0

        while left <= right:
            if (people[left] + people[right] ) <= limit:
                left += 1

            right -= 1
            boat += 1
        
        return boat

           
