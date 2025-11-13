<h2><a href="https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/">2294. Partition Array Such That Maximum Difference Is K</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. You may partition <code>nums</code> into one or more subsequences such that each element in <code>nums</code> appears in exactly one of the subsequences.</p>

<p>Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most <code>k</code>.</p>

<p>A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [3,6,1,2,5], k = 2
<strong>Output:</strong> 2

<strong>Explanation:</strong>
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2.
It can be shown that 2 is the minimum number of subsequences needed.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [1,2,3], k = 1
<strong>Output:</strong> 2

<strong>Explanation:</strong>
We can partition nums into the two subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2.
Another optimal solution is to partition nums into [1] and [2,3].
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [2,2,4,5], k = 0
<strong>Output:</strong> 3

<strong>Explanation:</strong>
We can partition nums into the three subsequences [2,2], [4], and [5].
The difference between the maximum and minimum value in each subsequence is 0.
Since three subsequences were created, we return 3.
It can be shown that 3 is the minimum number of subsequences needed.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
