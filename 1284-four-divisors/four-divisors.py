class Solution:
    def __init__(self):
        self.is_prime = [True for _ in range(10**5+1)]
        self.is_prime[0] = self.is_prime[1] = False
        i = 2
        while i * i <= 10**5:
            if self.is_prime[i]:
                j = 2
                while i * j <= 10**5:
                    self.is_prime[i*j] = False
                    j += 1
            i += 1
        self.primes = []
        for i in range(10**5+1):
            if self.is_prime[i] == True:
                self.primes.append(i)
        self.is_prime[1] = True
        
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        dp = {}
        # print(self.primes)
        for num in nums:
            if num in dp:
                ans += dp[num]
                continue
            if self.is_prime[num]:
                dp[num] = 0
                continue
            for prime in self.primes:
                if num % prime == 0:
                    if num//prime == prime:
                        dp[num] = 0
                    elif self.is_prime[num//prime] or prime ** 2 == num//prime:
                        dp[num] = 1 + num + num//prime + prime
                    else:
                        dp[num] = 0
                    break
            ans += dp[num]
        return ans
