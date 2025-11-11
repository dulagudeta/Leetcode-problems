<h2><a href="https://leetcode.com/problems/ones-and-zeroes/">474. Ones and Zeroes</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>You are given an array of binary strings <code>strs</code> and two integers <code>m</code> and <code>n</code>.</p>

<p>Return the size of the largest subset of <code>strs</code> such that there are at most <code>m</code> 0's and <code>n</code> 1's in the subset.</p>

<p>A set <code>x</code> is a subset of a set <code>y</code> if all elements of <code>x</code> are also elements of <code>y</code>.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> strs = ["10","0001","111001","1","0"], m = 5, n = 3
<strong>Output:</strong> 4

<strong>Explanation:</strong> The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> strs = ["10","0","1"], m = 1, n = 1
<strong>Output:</strong> 2

<strong>Explanation:</strong> The largest subset is {"0", "1"}, so the answer is 2.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= strs.length &lt;= 600</code></li>
  <li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
  <li><code>strs[i]</code> consists only of digits '0' and '1'.</li>
  <li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>
