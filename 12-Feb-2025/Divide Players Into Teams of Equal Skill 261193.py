# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        # colliding 2-pointers
        left = 0
        right = len(skill) - 1
        chemistry = 0
        prod = 0
        check = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != check:
                return -1
                
            prod = (skill[left] * skill[right])
            chemistry += prod

            left += 1
            right -= 1

        return chemistry
        