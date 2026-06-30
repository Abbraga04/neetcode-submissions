class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> checker;
        for (int i = 0; i < nums.size(); i++) {
            if (checker.contains(nums[i])) {
                return true;
            }
            checker.insert(nums[i]);
        }
        return false;
    }
};