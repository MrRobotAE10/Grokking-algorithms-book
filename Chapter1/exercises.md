1. Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

    > The maximun number of steps it would take in a sorted list of 128 names would be: log_2 (128) = 7 steps (rounded)

2. Suppose you double the size of the list. What’s the maximum number of steps now?

    > Size of the list now = 256\
    > The maximun number of steps it would take in a sorted list of 256 names would be: log_2 (256) = 8 steps (rounded)

Give the run time for each of these scenarios in terms of Big O.

3. You have a name, and you want to find the person’s phone number in the phone book.

    > Using binary search in a sorted phone book, the run time would be O(log n)

4. You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

    > Using linear search in the phone book, the run time would be O(n)

5. You want to read the numbers of every person in the phone book.

    > It requires linear search so the run time would also be O(n)

6. You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)

    > It also requires linear search so the run time would be O(n)

