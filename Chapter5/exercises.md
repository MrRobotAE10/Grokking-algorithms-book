It’s important for hash functions to consistently return the same output for the same input. If they don’t, you won’t be able to find your item 
after you put it in the hash table!

Which one of these hash functions are consistent?

1. f(x) = 1

    > It's consistent

2. f(x) = rand()

    > It isn't consistent

3. f(x) = next_empty_slot()

    > It isn't consistent

4. f(x) = len(x)

    > It's consistent

Suppose you have these four hash functions that work with strings:

a. Return “1” for all input.

b. Use the length of the string as the index.

c. Use the first character of the string as the index. So, all strings starting with a are hashed together, and so on.

d. Map every letter to a prime number: a = 2, b = 3, c = 5, d = 7, e = 11, and so on. For a string, the hash function is the sum of all
the characters modulo the size of the hash. For example, if your hash size is 10, and the string is “bag”, the index is 3 + 2 + 17 %
10 = 22 % 10 = 2.

For each of these examples, which hash functions would provide a good distribution? Assume a hash table size of 10 slots.

5. A phonebook where the keys are names and values are phone numbers. The names are as follows: Esther, Ben, Bob, and Dan.

    > D

6. A mapping from battery size to power. The sizes are A, AA, AAA, and AAAA.

    > B D

7. A mapping from book titles to authors. The titles are Maus, Fun Home, and Watchmen.

    > B C D 
