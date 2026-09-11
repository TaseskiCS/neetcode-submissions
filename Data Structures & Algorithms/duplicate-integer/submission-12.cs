public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> set = new HashSet<int>();
        foreach(int num in nums) {
            if (set.TryGetValue(num, out var val)) {
                return true;
            }
            set.Add(num);
        }
        return false;
    }
}