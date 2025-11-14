<h2><a href="https://leetcode.com/problems/increment-submatrices-by-one/">2536. Increment Submatrices by One</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

<p>You are given a positive integer <code>n</code>, indicating that we initially have an <code>n x n</code> zero-indexed integer matrix <code>mat</code> filled with zeroes.</p>

<p>You are also given a 2D integer array <code>queries</code>. For each <code>queries[i] = [row1, col1, row2, col2]</code>, you should perform the following operation:</p>

<p>Add <code>1</code> to every element in the submatrix with top-left corner <code>(row1, col1)</code> and bottom-right corner <code>(row2, col2)</code>.  
That is, add <code>1</code> to <code>mat[x][y]</code> for all <code>row1 ≤ x ≤ row2</code> and <code>col1 ≤ y ≤ col2</code>.</p>

<p>Return the matrix <code>mat</code> after performing every query.</p>

<h3>Example 1:</h3>
<pre>
<strong>Input:</strong> n = 3, queries = [[1,1,2,2],[0,0,1,1]]

<strong>Output:</strong> [[1,1,0],
          [1,2,1],
          [0,1,1]]

<strong>Explanation:</strong>
After the first query, we increment the submatrix (1,1) to (2,2).
After the second query, we increment the submatrix (0,0) to (1,1).
</pre>

<h3>Example 2:</h3>
<pre>
<strong>Input:</strong> n = 2, queries = [[0,0,1,1]]
<strong>Output:</strong> [[1,1],
          [1,1]]

<strong>Explanation:</strong>
Every element is incremented once.
</pre>

<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= n &lt;= 500</code></li>
  <li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
  <li><code>0 &lt;= row1 &lt;= row2 &lt; n</code></li>
  <li><code>0 &lt;= col1 &lt;= col2 &lt; n</code></li>
</ul>
