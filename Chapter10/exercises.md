1. In the Netflix example, you calculated the distance between two different users using the distance formula. But not all users rate
movies the same way. Suppose you have two users, Yogi and Pinky, who have the same taste in movies. But Yogi rates any movie he likes as a 5, 
whereas Pinky is choosier and reserves the 5s for only the best. They’re well matched, but according to the distance
algorithm, they aren’t neighbors. How would you take their different rating strategies into account?

    > Normalize Pinky's and Yogi's ratings by their mean, and adjust it until both have the same mean and then compare.

2. Suppose Netflix nominates a group of “influencers.” For example, Quentin Tarantino and Wes Anderson are influencers on Netflix, 
so their ratings count for more than a normal user’s. How would you change the recommendations system so it’s biased toward the
ratings of influencers?

    > Make the influencers have weight to their rating so they count more 