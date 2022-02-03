"""
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Given a string s, find the length of the longest substring without repeating characters.

"""

class LengthOfLengestSubstring:
    def use_sliding_window(self, s):
        """
            The naive approach is very straightforward. But it is too slow. So how can we optimize it?
            In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. 
            If a substring Sij from index i to −1 is already checked to have no duplicate characters. 
            We only need to check if s[j] is already in the substring sij.
            To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2) algorithm. But we can do better.

            By using HashSet as a sliding window, checking if a character in the current can be done in O(1).
            A sliding window is an abstract concept commonly used in array/string problems. 
            A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed, right-open). 
            A sliding window is a window "slides" its two boundaries to the certain direction. 
            For example, if we slide [i,j) to the right by 11 element, then it becomes [i+1,j+1) (left-closed, right-open).
            Back to our problem. We use HashSet to store the characters in current window [i,j) (j = ij=i initially). 
            Then we slide the index jj to the right. If it is not in the HashSet, we slide jj further. 
            Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index ii.
            If we do this for all ii, we get our answer.
        """
        chars = [0]*128
        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            right +=1
        return res
    
    def sliding_window_optimization(self, s):
        n = len(s)
        ans = 0
        mp = {}
        
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans   

    def s1_test(self, s):
        max_sub = i = j = 0
        mp = {}

        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            mp[s[j]] = j + 1

            max_sub = max(max_sub, j - i + 1)
        return max_sub

l = LengthOfLengestSubstring()

tc_inputs = ["abcabcbb", "bbbbb", "pwwkew"]
for tc_input in tc_inputs:
    #print(l.use_sliding_window('abcabcbb'))
    #print(l.sliding_window_optimization(tc_inputs))
    print(tc_input, l.s1_test(tc_input))

