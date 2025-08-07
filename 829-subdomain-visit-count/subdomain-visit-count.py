from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapping = {}

        for combo in cpdomains:
            count_str, full_domain = combo.split(' ')
            visit = int(count_str)
            domain_parts = full_domain.split('.')

            # Generate all subdomains from full_domain
            for i in range(len(domain_parts)):
                subdomain = '.'.join(domain_parts[i:])
                mapping[subdomain] = mapping.get(subdomain, 0) + visit

        # Build result list
        res = []
        for domain, count in mapping.items():
            res.append(f"{count} {domain}")

        return res
