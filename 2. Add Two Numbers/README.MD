<h2><a href="https://leetcode.com/problems/add-two-numbers/">2. Add Two Numbers</a></h2> <img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" /> <hr> <p>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each node contains a single digit.</p> <p>Add the two numbers and return the sum as a linked list.</p> <p>You may assume the two numbers do not contain any leading zero, except the number <code>0</code> itself.</p> <h3>Example 1:</h3> <pre> <strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4] <strong>Output:</strong> [7,0,8]

<strong>Explanation:</strong>
342 + 465 = 807.
</pre>

<h3>Example 2:</h3> <pre> <strong>Input:</strong> l1 = [0], l2 = [0] <strong>Output:</strong> [0] </pre> <h3>Example 3:</h3> <pre> <strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] <strong>Output:</strong> [8,9,9,9,0,0,0,1] </pre> <h3>Constraints:</h3> <ul> <li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li> <li><code>0 &lt;= Node.val &lt;= 9</code></li> <li>The input lists do not contain leading zeros.</li> </ul>