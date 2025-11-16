<h2><a href="https://leetcode.com/problems/number-of-substrings-with-only-1s/">1513. Number of Substrings With Only 1s</a></h2> <img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" /> <hr> <p>You are given a binary string <code>s</code>.</p> <p>Return the number of substrings that consist of <strong>only the character '1'</strong>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p> <h3>Example 1:</h3> <pre> <strong>Input:</strong> s = "0110111" <strong>Output:</strong> 9

<strong>Explanation:</strong>
Substrings consisting only of '1':
"1" → 5 times
"11" → 3 times
"111" → 1 time
Total = 9
</pre>

<h3>Example 2:</h3> <pre> <strong>Input:</strong> s = "101" <strong>Output:</strong> 2

<strong>Explanation:</strong>
Only the substring "1" appears twice.
</pre>

<h3>Example 3:</h3> <pre> <strong>Input:</strong> s = "111111" <strong>Output:</strong> 21

<strong>Explanation:</strong>
Every substring consists only of '1'.
</pre>

<h3>Constraints:</h3> <ul> <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li> <li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li> </ul>