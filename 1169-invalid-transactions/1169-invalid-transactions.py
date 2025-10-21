class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        '''
          handle for the case when,
           - transaction occurs in 2 cities, by same name, in under <= 60
           - transaction has in same city, same name, in under <= 60 but amount >1000
           - 
        '''
        
        # name, time, amount, city
        # hashmap = defaultdict(int)
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, t))
        
        result = []
        n = len(parsed)
        
        for i in range(n):
            name1, time1, amount1, city1, raw1 = parsed[i]
            is_invalid = False
            
            # Rule 1: amount > 1000
            if amount1 > 1000:
                is_invalid = True
            
            # Rule 2: within 60 min, same name, different city
            for j in range(n):
                if i == j:
                    continue
                name2, time2, amount2, city2, raw2 = parsed[j]
                if name1 == name2 and abs(time1 - time2) <= 60 and city1 != city2:
                    is_invalid = True
                    break  # one match is enough
            
            if is_invalid:
                result.append(raw1)
        
        return result

            
            # add it on a hashmap if it is not already there.
            # if already in hashmap with same name try to check the cities, if different citites check the time
        # return list(invalid)