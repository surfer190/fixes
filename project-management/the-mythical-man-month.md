# Notes from the mythical man month

> I believe that large programming projects suffer management problems different in kind from small ones, due to division of labor. I believe the critical need to be the preservation of the conceptual integrity of the product itself.

## The Tar Pit

### The Joys of the Craft

* Making Things
* Pleasure of making things useful to other people
* Fascination of bringing things together
* The joy of always learning - from the non-repeating nature of the task
* It is a tractable medium - controllable and flexible
* Gratifies creative longings built deep inside us

### The Woes of the Craft

> Human beings are not accustomed to being perfect, and few areas of human activity demand it. Adjusting to the requirement for perfection is, I think, the most difficult part of learning to program.

> Next, other people set one's objectives, provide one's resources, and furnish one's information. One rarely controls the circumstances of his work, or even its goal.

> The dependence upon others has a particular case that is espe- cially painful for the system programmer. He depends upon other people's programs. These are often maldesigned, poorly implemented, incompletely delivered (no source code or test cases), and poorly documented. So he must spend hours studying and fixing things that in an ideal world would be complete, available, and usable.

## The Mythical Man-Month

1. Our techniques of estimating are poorly developed. More seriously, they reflect an unvoiced assumption which is quite untrue, i.e., that all will go well.
2. Our estimating techniques fallaciously confuse effort with progress, hiding the assumption that men and months are interchangeable.
3. because we are uncertain of our estimates, software managers often lack the courteous stubbornness of Antoine's chef.
4. Schedule progress is poorly monitored
5. When schedule slippage is recognized, the natural (and traditional) response is to add manpower. Like dousing a fire with gasoline, this makes matters worse, much worse.

### Optimism

Software development seems to attract these idiot __optimists__ that think everything will go well. Some go so far as to demonise me, a realist, a person focusing on the outcome and a person willing to say no.

> For the human makers of things, the incompletenesses and inconsistencies of our ideas become clear only during implementation.

Because the medium is tractable, we expect few difficulties in implementation; hence our pervasive optimism

Because our ideas are faulty, we have bugs; hence our optimism is unjustified.

### The man month

> Cost does indeed vary as the product of the number of men and the number of months. Progress does not.

> Men and months are interchangeable commodities only when a task can be partitioned among many workers with no communication among them

Ie. when things need to be done in sequence (not in parrallel) the application of more effort has no effect on the schedule. Debugging is an example of a sequential task.

> The bearing of a child takes nine months, no matter how many women are assigned.

If there is communication between sub tasks, the effort of communication must be added to the amount of work that needs to be done.

Communication is made up of training (of goals, technology and overall strategy) and intercommunication, which is very costly as pairwise communication increases exponentially.

> Since software construction is inherently a systems effort — an exercise in complex interrelationships — communication effort is great, and it quickly dominates the decrease in individual task time brought about by partitioning. Adding more men then lengthens, not shortens, the schedule.

Failing to give enough time to testing (at the end, we aren't talking the superior test driven development), is peculiarly disastrous. Since the delay comes at the end of the schedule, no one is aware of schedule trouble until almost the delivery date. Bad news, late and without warning, is unsettling to customers and to managers. Furthermore, delay at this point has unusually severe finan- cial, as well as psychological, repercussions.

### Gutless Estimating

> Observe that for the programmer, as for the chef, the urgency of the patron may govern the scheduled completion of the task, but it cannot govern the actual completion

An omelette, promised in two minutes, may appear to be progressing nicely. But when it has not set in two minutes, the customer has two choices — wait or eat it raw. Software customers have had the same choices.
The cook has another choice; he can turn up the heat. The result is often an omelette nothing can save—burned in one part, raw in another.

> Brooke's law: Adding manpower to a late software project makes it later.

> More software projects have gone awry for lack of calendar time than for all other causes combined.

### The Surgical Team

The data showed no correlation whatsoever between experience and performance.

### Mill's Proposal a.k.a the Mob Proposal

Each segment of a large job be tackled by a team. But instead of each member cutting away at the problem, one does teh cutting the rest provide the support to enhance his effectiveness and productivity.

> Absolutely vital to Mills's concept is the transformation of programming "from private art to public practice" by making all the computer runs visible to all team members and identifying all programs and data as team property, not private property.

### Aristocracy, Democracy and System Design



