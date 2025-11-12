<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/">4. Median of Two Sorted Arrays</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return the median of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m + n))</code>.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000

<strong>Explanation:</strong> The merged array is [1,2,3] and the median is 2.
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000

<strong>Explanation:</strong> The merged array is [1,2,3,4] and the median is (2 + 3) / 2 = 2.5.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>nums1.length == m</code></li>
  <li><code>nums2.length == n</code></li>
  <li><code>0 &lt;= m &lt;= 1000</code></li>
  <li><code>0 &lt;= n &lt;= 1000</code></li>
  <li><code>1 &lt;= m + n &lt;= 2000</code></li>
  <li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>
