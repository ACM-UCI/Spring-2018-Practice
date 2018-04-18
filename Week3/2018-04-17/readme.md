Dynamic Programming

EASY DP

PROBLEM 1  
https://www.hackerrank.com/challenges/prime-xor/problem

PROBLEM 2  
https://www.hackerrank.com/challenges/mr-k-marsh/problem

PROBLEM 3  (THIS COMES IN EVERY PROGRAMMING COMPETITION, WE WILL DO MORE OF THESE ONES LATER)  
https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem



ACTUALLY EASY DP

PROBLEM 1  
https://www.hackerrank.com/challenges/coin-change/problem

PROBLEM 2  
https://www.hackerrank.com/challenges/equal/problem Beware, the problem statement is currently wrong.  It should say {1,2,5}, not {1,3,5}.

PROBLEM 3  
https://www.hackerrank.com/challenges/sherlock-and-cost/problem


GOOGLE INTERVIEW DP  
You are given a plane on which certain rectangles are placed. How do you choose a point that is equally chosen from the rectangles in the plane. (Remember some points will have overlap)


---

## Solutions:

### Equal:

At first, it seems like it's not a DP problem.  Play around with the problem and simulate small examples in your head a bit, and you might notice that each operation is equivalent to subtracting x from the chosen index.  That is, adding 5 to everyone else but Bob is equivalent to subtracting 5 from Bob.  You'll also notice that you *have* to get every person to have the same amount of chocolate as the person with the smallest.  So, you have to repeatedly select any person who is not the smallest until they match up with the smallest.  There's no other way to decrease the gap between a person and the smallest.

So, this operation is kind of atomic, in that each person's decreasingment does not interact with another's.  So we simply need to find out how many operations it takes to turn a person X into the minimum (when we model the operation as subtracting chocolates).  How many operations does it take to turn 13 into 2?  We need to subtract 11 chocolates to get from 13 to 2.  What's the shortest amount of operations to subtract 11 chocolates?  This is where the DP comes in.

We use standard DP coinchange/mcnugget numbers calculation to find the minimum amount of operations to subtract any amount from 0 to 1000.

Then, we simply add up all the numbers of operations needed for every person to get to the minimum.

However, you may notice a severe edgecase, or maybe you don't and you submit it but find out that several testcases don't pass.  
Sometimes, performing an operation on THE MINIMUM will be beneficial.

For example, if the amounts of chocolate are 1 5 5 5 5: to get each 5 to be 1 would require us to reduce each person's chocolates by 4.  The fastest way to do that is 2 operations each.  However, if we decrease the 1 by 1 chocolate, we get 0 5 5 5 5, and now each 5 only needs 1 operation (a 5) to be settled.  

This may seem like it throws a wrench in the whole thing.  When I realized this, I was afraid that the whole approach was wrong.  However, we can notice that this is only an issue if INCREASING the gap between some person x and the minimum will REDUCE the number of operations needed to get from x to the minimum. This can really only happen when the gap increases by 1 or 2.  (Observation of the DP table leads to this hypothesis.)  For example of an increase of 1, it takes 3 operations to make 7, but only 2 to make 8.  An increase of 2: it takes 4 operations to make 13, but only 3 to make 15.  But none exist with increases of 3 or more.  

So, we would only ever want to increase the min by 1 or 2.  But how do we know when we should?  Well, since there are only 3 options (increase min by 0, 1, or 2), we don't need to predict whether we need to do one or the other.  We can just try all 3 options, and choose the lowest answer from those.  (See line 18 in the code.)  Honestly, I never convinced myself that this is all we need to do.  There are a few more potential edge-cases that I haven't convinced myself are not actually edge cases, like what if we need to operate on 2 people who are both minimums?  Like 1 1 5 5 5 5 5.  In fact, as I write this, I'm pretty sure that is actually an edge case, but the test cases didn't cover it, so my program passed anyways.

-Kevin Wang

