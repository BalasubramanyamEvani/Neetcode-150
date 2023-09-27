class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for cpdomain in cpdomains:
            val, domain = cpdomain.split()
            domain_parts = domain.split(".")
            for i in range(len(domain_parts)):
                domain_part = ".".join(domain_parts[i:])
                if domain_part in res:
                    res[domain_part] += int(val) 
                else:
                    res[domain_part] = int(val)
        print(res)
        ret = []
        for k, v in res.items():
            ret.append(str(v) + " " + k)
        return ret
