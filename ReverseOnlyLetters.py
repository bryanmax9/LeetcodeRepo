"""
917. Reverse Only Letters
Solved
Easy
Topics
Companies
Hint

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.


"""


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        lista = list(s)
        l = 0

        r = len(s) - 1

        while l < r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                lista[l], lista[r] = lista[r], lista[l]
                l += 1
                r -= 1

        return "".join(lista)
