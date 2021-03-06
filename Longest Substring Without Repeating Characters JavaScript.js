Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
// Solution:


    /**
     * @param {string} s
     * @return {number}
     */

    var lengthOfLongestSubstring = function(s) {
        var slen = s.length, count = 0;
        for(var i=0;i<slen;i++) {
            var flag = 0;

			for(var j=0;j<i;j++) {
				if(s[i] == s[j]){
					flag = 1;
                }
            }

            if(!flag) {
				count++;
            }
        }
        return count;
    };

    console.log(lengthOfLongestSubstring('abcabcbb')); //the answer is "abc", which the length is 3.
    console.log(lengthOfLongestSubstring('bbbbb')); // the answer is "b", with the length of 1.
    console.log(lengthOfLongestSubstring('pwwkew')); //the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

