A: https://www.hackerrank.com/challenges/diagonal-difference/problem (VERY EASY)

B: https://www.hackerrank.com/contests/w37/challenges/dynamic-line-intersection  (FUN little hard)

C: https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard (CODE JAM Round 2  prob 1 KEVIN says easy)

D: https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/00000000000459f3 (Round 2 prob 2)

E: https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/0000000000045875 (Round 2 prob 3)

FUN PROBLEM:
There is a private array which has 2000 balls which are each colored either black or white. You’re asked to find out the majority that is if there are more white balls output an index where a white ball is present, if there are more black balls output an index where a  black ball is present. If there are an equal number of balls output 0.
Seems easy enough, now here’s the catch. You don’t have access to an array, you only have access to an ORACLE with the following description: given four unique indexes the ORACLE returns that absolute difference between the black and white balls. Using this oracle solve the problem and minimize the number of ORACLE calls used.
Heres an example  suppose the array is [W,W,B,W,B,B] then ORACLE(0,1,2,3) would be abs(1-3) = 2
