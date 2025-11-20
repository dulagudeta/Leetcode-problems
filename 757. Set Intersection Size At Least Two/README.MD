<h2><a href="https://leetcode.com/problems/set-intersection-size-at-least-two/">757. Set Intersection Size At Least Two</a></h2> <img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" /> <hr> <p>You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code> represents all integers from <code>start_i</code> to <code>end_i</code> inclusive.</p> <p>A <strong>containing set</strong> is an array <code>nums</code> such that every interval in <code>intervals</code> includes at least <strong>two integers</strong> from <code>nums</code>.</p> <p>Return the <strong>minimum possible size</strong> of such a containing set.</p> <h3>Example 1:</h3> <pre> <strong>Input:</strong> intervals = [[1,3],[3,7],[8,9]] <strong>Output:</strong> 5

<strong>Explanation:</strong>
One optimal containing set is nums = [2, 3, 4, 8, 9].
Each interval contains at least two numbers from nums.
It can be shown that no containing set of size 4 exists.
</pre>

<h3>Example 2:</h3> <pre> <strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]] <strong>Output:</strong> 3

<strong>Explanation:</strong>
One optimal containing set is nums = [2, 3, 4].
It can be shown that no containing set of size 2 satisfies the condition.
</pre>

<h3>Example 3:</h3> <pre> <strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]] <strong>Output:</strong> 5

<strong>Explanation:</strong>
An optimal containing set is nums = [1, 2, 3, 4, 5].
No containing set of size 4 can satisfy all intervals.
</pre>

<h3>Constraints:</h3> <ul> <li><code>1 &lt;= intervals.length &lt;= 3000</code></li> <li><code>intervals[i].length == 2</code></li> <li><code>0 &lt;= start_i &lt; end_i &lt;= 10<sup>8</sup></code></li> </ul>