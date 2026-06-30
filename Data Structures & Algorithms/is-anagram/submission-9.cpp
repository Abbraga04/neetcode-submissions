class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, int> compare;

        for (char c1 : s) {
            compare[c1]++;
        }
        for (char c2 : t) {
            compare[c2]--;
        }

        for (auto& pair : compare) {
            if (pair.second != 0) {
                return false;
            }
        }
        return true;
    }
};
