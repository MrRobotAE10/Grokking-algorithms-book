Run the breadth-first search algorithm on each of these graphs to find the solution.

1. Find the length of the shortest path from start to finish.

    > The shortest path has a length of 2

2.  Find the length of the shortest path from “cab” to “bat”.

    > The shortest path has a length of 2

Here’s a small graph of my morning routine.

    wake up <- brush teeth <- eat breakfast

    wake up <- shower

It tells you that I can’t eat breakfast until I’ve brushed my teeth. So “eat breakfast” depends on “brush teeth”. On the other hand, showering doesn’t depend on brushing my teeth,
because I can shower before I brush my teeth. From this graph, you can make a list of the order in which I need to do my morning routine

3. For these three lists, mark whether each one is valid or invalid.

    A. 

       1 Wake up

       2 Shower

       3 Eat breakfast

       4 Brush Teeth

    B.

       1 Wake up

       2 Brush Teeth

       3 Eat breakfast

       4 Shower

    C.

       1 Shower

       2 Wake up

       3 Brush Teeth

       4 Eat breakfast

    > List B is valid, For list A  eat breakfast depends on brush teeth, For list C shower depends on Wake up so they are invalid

4. Here’s a larger graph. Make a valid list for this graph.

    wake up <- Exercise <- Shower <- Get Dressed
    wake up <- brush teeth <- eat breakfast
    wake up <- pack lunch

    > 1 Wake up\
      2 Pack lunch\
      3 Exercise\
      4 Shower\
      5 Brush Teeth\
      6 Get Dressed\
      7 Eat breakfast

(If task A depends on Task B, task A shows latter in the list, i.e Topological Sort)\
(Trees: Special type of graphs where no edges ever point back)

5. Which graphs are also trees?

    > Those whose bottom edges does not point back up