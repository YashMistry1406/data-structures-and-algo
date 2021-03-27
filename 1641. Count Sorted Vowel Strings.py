#Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
#
#A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
#
#
#https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC%2B%2BPython-DP-O(1)-Time-and-Space


class Solution:
   def countVowelStrings(self, n):
       return int((n + 1) * (n + 2) * (n + 3) * (n + 4) / 24)
