<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/">2654. Minimum Number of Operations to Make All Array Elements Equal to 1</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>You are given a 0-indexed array <code>nums</code> consisting of positive integers. You can perform the following operation any number of times:</p>

<ul>
  <li>Select an index <code>i</code> such that <code>0 &lt;= i &lt; n - 1</code> and replace either <code>nums[i]</code> or <code>nums[i+1]</code> with their <code>gcd</code> value.</li>
</ul>

<p>Return the minimum number of operations to make all elements of <code>nums</code> equal to 1. If it is impossible, return <code>-1</code>.</p>

<p>The <code>gcd</code> of two integers is the greatest common divisor of the two integers.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [2,6,3,4]
<strong>Output:</strong> 4

<strong>Explanation:</strong>
We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now nums = [1,1,1,1].
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [2,10,6,14]
<strong>Output:</strong> -1

<strong>Explanation:</strong> It is impossible to make all elements equal to 1.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>2 &lt;= nums.length &lt;= 50</code></li>
  <li><code>1 &lt;= nums[i] &lt;= 10^6</code></li>
</ul>
