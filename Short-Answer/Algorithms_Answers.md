#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Loop continues until a is brought up to a constant value set by n^3. Each loop adds n\*2 to a, so really it's going to loop n times. That is just O(n).

b) There are two nested loops based on n. The outer loop is O(n). The inner loop doubles the index value each time for O(log n), together they'd add up to an O(n log n) situation.

c) Recursion doesn't add that much overhead. This recursive function isn't doing anything fancy except calling itself. That's once again a linear function, or O(n).

## Exercise II

This is a binary search, which is O(log n) because it halves the values each time.

We should start dropping eggs from half way up the building, floor n//2. Depending on the result of the egg drop. We should move either half way up (not broken) or half way back down (broken) the building and drop a second egg and so on until the correct floor is located.
