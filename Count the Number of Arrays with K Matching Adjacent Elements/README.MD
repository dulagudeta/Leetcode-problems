<h2><a href="https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/">3405. Count the Number of Arrays with K Matching Adjacent Elements</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>You are given three integers <code>n</code>, <code>m</code>, and <code>k</code>.</p>

<p>A good array <code>arr</code> of size <code>n</code> is defined as follows:</p>
<ul>
  <li>Each element in <code>arr</code> is in the inclusive range <code>[1, m]</code>.</li>
  <li>Exactly <code>k</code> indices <code>i</code> (where <code>1 &lt;= i &lt; n</code>) satisfy the condition <code>arr[i - 1] == arr[i]</code>.</li>
</ul>

<p>Return the number of good arrays that can be formed.</p>

<p>Since the answer may be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> n = 3, m = 2, k = 1
<strong>Output:</strong> 4

<strong>Explanation:</strong>
There are 4 good arrays:
[1, 1, 2], [1, 2, 2], [2, 1, 1], and [2, 2, 1].
Hence, the answer is 4.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> n = 4, m = 2, k = 2
<strong>Output:</strong> 6

<strong>Explanation:</strong>
The good arrays are:
[1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1], and [2, 2, 2, 1].
Hence, the answer is 6.
</pre>

<h3>Example 3:</h3>
<pre>
<strong>Input:</strong> n = 5, m = 2, k = 0
<strong>Output:</strong> 2

<strong>Explanation:</strong>
The good arrays are:
[1, 2, 1, 2, 1] and [2, 1, 2, 1, 2].
Hence, the answer is 2.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= m &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= k &lt;= n - 1</code></li>
</ul>
