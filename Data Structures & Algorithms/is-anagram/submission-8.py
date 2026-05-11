class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1, dict2 = {}, {}
        for char1, char2 in zip(s, t):
            dict1[char1] = dict1.get(char1, 0) + 1
            dict2[char2] = dict2.get(char2, 0) + 1

        if dict1 == dict2:
            return True
        return False