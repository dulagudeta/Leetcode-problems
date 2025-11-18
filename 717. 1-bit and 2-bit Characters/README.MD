<h2><a href="https://leetcode.com/problems/1-bit-and-2-bit-characters/">717. 1-bit and 2-bit Characters</a></h2> <img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" /> <hr> <p>We have two special characters:</p> <ul> <li>The first character can be represented by one bit: <code>0</code>.</li> <li>The second character can be represented by two bits: <code>10</code> or <code>11</code>.</li> </ul> <p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p> <h3>Example 1:</h3> <pre> <strong>Input:</strong> bits = [1,0,0] <strong>Output:</strong> true

<strong>Explanation:</strong>
The only way to decode it is a two-bit character followed by a one-bit character.
So the last character is a one-bit character.
</pre>

<h3>Example 2:</h3> <pre> <strong>Input:</strong> bits = [1,1,1,0] <strong>Output:</strong> false

<strong>Explanation:</strong>
The only way to decode it is two two-bit characters.
So the last character is not a one-bit character.
</pre>

<h3>Constraints:</h3> <ul> <li><code>1 &lt;= bits.length &lt;= 1000</code></li> <li><code>bits[i]</code> is either <code>0</code> or <code>1</li> </ul>