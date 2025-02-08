# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(list)
        ans = []
        for domain in cpdomains:
            new_list = domain.split()
            visit, full_domain = int(new_list[0]), new_list[1] 
            # add to hash
            count[full_domain].append(visit)

            word = full_domain
            for i in range(len(word)):
                if word[i] == ".":
                    subdomain = word[i+1: ]
                    count[subdomain].append(visit)
            
        for key, val in count.items():
                total_visit = sum(val)
                new_cpdomain = f"{total_visit} {key}"
                ans.append(new_cpdomain)
            
        return ans
       