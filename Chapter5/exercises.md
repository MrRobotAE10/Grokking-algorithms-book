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

