class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for s in strs:
            grouped_anagrams["".join(sorted(s))].append(s)
        return list(grouped_anagrams.values())