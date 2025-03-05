class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        # track = 1
        min_count = 0
        i = 0
        while i < len(answers):
            track = answers[i] + 1
            colors = answers[i]
            while i < len(answers) and track > 0 and answers[i] == colors:
                i += 1
                track -= 1
            min_count += colors + 1
        
        return min_count