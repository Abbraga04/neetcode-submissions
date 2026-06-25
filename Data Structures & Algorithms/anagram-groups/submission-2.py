class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            signature = tuple(counts)

            buckets.setdefault(signature, []).append(word)

        return list(buckets.values())