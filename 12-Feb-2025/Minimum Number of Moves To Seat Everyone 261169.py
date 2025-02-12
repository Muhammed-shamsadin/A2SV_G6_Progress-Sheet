# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        left, right = 0, 0
        count = 0

        while left < len(seats) and right < len(students):
            count += abs(seats[left] - students[right])

            left += 1
            right += 1
        
        return count