# ontime!
## What is it?
Let's keep it simple: ontime is an activity sorting algorithm that allows for the automatic sorting of input tasks based on three factors:

* Priority of the task
* Duration of the task
* Available times

If the activity with the topmost priority cannot fit in a certain timeslot, it will be moved into another timeslot (if any) in which it can fit. Essentially it is an iterative sorting process where the priority order determines which tasks are allocated first and then allocates them based on the continuous available timeslots. If the task cannot be fit into any of the slots it will be dismissed.

## Why and how to use ontime!
ontime is easy to use and works purely based on user inputs. If you wish to use this program there is no need for inputting anything in the code or modifying any line. You just need to run the code and the algorithm will do everything for you (given of course that you have input everything correctly). There is some degree of error handling, however like all things in life ontime! is not perfect, and is prone to having some errors based on the user inputs

To use ontime, the user will first need to define (in separate input boxes, which will appear one at a time) their fixed task name, start hour, and end hour. After adding how many fixed tasks the user wants, they will need to press enter on a blank text box to advance to creating the "dynamic" tasks, or the tasks to be sorted. In order, and separate input dialogs, the user will have to define the description/name of the task to be sorted, the duration (in complete hours) of the task, and the priority. Here are some things to take into consideration:

* The priority follows no scale, the lower the number the higher the priority. The only requirement for the priority value is that the number is required to be non-negative.
* This program only works with intervals of full hours. This means the only supported intervals of time are from XX:00 to YY:00. There is no option to create intervals from XX:30 to YY:45 and so on.

## Where should I start if I want to contribute to ontime!
Great question! ontime is far from a perfect program, so if you wish to work and help make ontime a better program you could start by working on any of the following aspects of the code:

* Conflicting priorities
* More precise timeslots
* Multi-day scheduling
* More friendly UX
* Code optimisation

These are just some suggestions to work on, you may find any other problematic or unrefined element within the algorithm and its processes that is not listed above.

Happy coding!

ontime team
