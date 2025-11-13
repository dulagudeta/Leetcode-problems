<h2><a href="https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/">2966. Divide Array Into Arrays With Max Difference</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>You are given an integer array <code>nums</code> of size <code>n</code> where <code>n</code> is a multiple of 3, and a positive integer <code>k</code>.</p>

<p>Divide the array <code>nums</code> into <code>n / 3</code> arrays of size 3 satisfying the following condition:</p>
<ul>
  <li>The difference between any two elements in one array is less than or equal to <code>k</code>.</li>
</ul>

<p>Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array.  
If there are multiple answers, return any of them.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums = [1,3,4,8,7,9,3,5,1], k = 2
<strong>Output:</strong> [[1,1,3],[3,4,5],[7,8,9]]

<strong>Explanation:</strong>
The difference between any two elements in each array is less than or equal to 2.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums = [2,4,2,2,5,2], k = 2
<strong>Output:</strong> []

<strong>Explanation:</strong>
Different ways to divide nums into 2 arrays of size 3 are:
[[2,2,2],[2,4,5]] (and its permutations)
[[2,2,4],[2,2,5]] (and its permutations)
Because there are four 2s, there will be an array with the elements 2 and 5 no matter how we divide it.
Since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
<strong>Output:</strong> [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]

<strong>Explanation:</strong>
The difference between any two elements in each array is less than or equal to 14.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>n == nums.length</code></li>
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
  <li><code>n</code> is a multiple of 3.</li>
  <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
