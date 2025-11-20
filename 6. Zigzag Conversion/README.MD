<h2><a href="https://leetcode.com/problems/zigzag-conversion/">6. Zigzag Conversion</a></h2> <img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" /> <hr> <p>The string <code>"PAYPALISHIRING"</code> is written in a zigzag pattern on a given number of rows like this:</p> <pre style="font-family: monospace;"> P A H N A P L S I I G Y I R </pre> <p>Then read line by line, the string becomes: <code>"PAHNAPLSIIGYIR"</code>.</p> <p>Write the code that takes a string and converts it into this zigzag form based on the number of rows:</p> <pre><code>string convert(string s, int numRows); </code></pre> <h3>Example 1:</h3> <pre> <strong>Input:</strong> s = "PAYPALISHIRING", numRows = 3 <strong>Output:</strong> "PAHNAPLSIIGYIR" </pre> <h3>Example 2:</h3> <pre> <strong>Input:</strong> s = "PAYPALISHIRING", numRows = 4 <strong>Output:</strong> "PINALSIGYAHRPI"

<strong>Explanation:</strong>
P I N
A L S I G
Y A H R
P I
</pre>

<h3>Example 3:</h3> <pre> <strong>Input:</strong> s = "A", numRows = 1 <strong>Output:</strong> "A" </pre> <h3>Constraints:</h3> <ul> <li><code>1 &lt;= s.length &lt;= 1000</code></li> <li><code>s</code> consists of English letters, <code>','</code>, and <code>'.'</code></li> <li><code>1 &lt;= numRows &lt;= 1000</code></li> </ul>