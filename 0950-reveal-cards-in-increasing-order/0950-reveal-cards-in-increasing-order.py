class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)

        deq = deque()

        for i in range(len(deck)):
            deq.appendleft(deck[i])
            popped = deq.pop()
            deq.appendleft(popped)

        deq.append(deq.popleft())
        return list(deq)