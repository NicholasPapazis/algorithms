# [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)

## Problem Description

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

## Approach

- \*\*create pointers to word1 and word2
- \*\*create array to store output
- \*\*loop while inbounds for both word1 and word2, and append alternating characters to array
- \*\*append remaining remaining characters from both strings
- \*\*join and return output array

## Time complexity

- \*\*O(n+m)

## Additional Notes

- \*\*use array while building output, as it is less costly than constantly modifying a string.
