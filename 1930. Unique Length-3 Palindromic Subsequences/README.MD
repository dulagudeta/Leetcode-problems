<div align="center">
  <h1>1930. Unique Length-3 Palindromic Subsequences</h1>
  <p><strong>Difficulty:</strong> Medium</p>
</div>

<hr>

<h2>📘 Problem Summary</h2>
<p>
  You are given a string <code>s</code> consisting of lowercase English letters.
  Your task is to return the number of <strong>unique palindromic subsequences</strong>
  of length <strong>exactly 3</strong>.
</p>

<p>A length-3 palindrome must have the structure: <code>c x c</code></p>

<ul>
  <li>The first and last characters must be the same.</li>
  <li>The middle character can be anything.</li>
  <li>Even if a subsequence appears multiple times, it is counted only once.</li>
</ul>

<hr>

<h2>💡 Approach (Optimal O(n))</h2>

<h3>Key Insight</h3>
<p>
For each character from <code>'a'</code> to <code>'z'</code>:
</p>

<ol>
  <li>Find the <strong>first</strong> and <strong>last</strong> occurrence in the string.</li>
  <li>If they form a valid range (<code>first &lt; last</code>):</li>
  <ul>
    <li>Look at the substring between them.</li>
    <li>Count the <strong>unique characters</strong> inside this middle section.</li>
  </ul>
  <li>Each unique middle character forms a palindrome: <code>c x c</code></li>
</ol>

<p>Sum this count for all 26 lowercase letters.</p>

<hr>

