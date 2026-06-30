class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        vector<int> compare(26, 0);

        for (int i = 0; i < s.size(); i++) {
            compare[s[i] - 'a']++;
            compare[t[i] - 'a']--;
        }

        for (int val : compare) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};
