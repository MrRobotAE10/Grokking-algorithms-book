1. Suppose you’re building an app to keep track of your finances. Every day, you write down everything you spent money on. At the end of the month, 
you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list?.

    > For a lot of inserts and a few reads, linked lists would be better.

2. Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, 
and chefs take orders off the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off 
the queue and cooks it. Would you use an array or a linked list to implement this queue?

    > There are a lot of insertions happening, and the chef takes the first order off the queue so linked lists would be better

3. Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. 
If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. 
Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list ofusernames instantly. 
Knowing this, would you implement the list as an array or a linked list?

    > Arrays provide random access while lists cant, arrays would be better (it has to be sorted for binary search to work).

4. People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? 
In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?

    > When new users are added to the array the insertions are slow and the users are inserted at the beginning or at the end of the array. In order for the binary search 
    to work the array must be reordered

5. In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. 
You have an array with 26 slots. Each slot points to a linked list. Compare this hybrid data structure to arrays and linked lists. 
Is it slower or faster than each for searching and inserting? You don’t have to give Big O run times, just whether the new data structure would be faster or slower.

    > In searching is slower than arrays because of the linked lists, in insertions is as fast as linked lists