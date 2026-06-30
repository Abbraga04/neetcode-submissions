class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, int> compare;

        for (int i = 0; i < s.size(); i++) {
            compare[s[i]]++;
            compare[t[i]]--;
        }

        for (auto& pair : compare) {
            if (pair.second != 0) {
                return false;
            }
        }
        return true;
    }
};
