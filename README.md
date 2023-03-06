# A* Search Algorithm Visualiser App
![Visualiser](https://github.com/Pierpaolo-C/Astar/blob/master/A_Algorithm%20Visualiser.png)
#### [Video Demo](https://youtu.be/iPy4k8W_fps)

## Description:
#### Welcome to my A* Algorithm visualiser app in Kivy!  This is the final project for [CS50x Introduction to Computer Science](https://cs50.harvard.edu/x/2023/).
#### This app allows you to visualize the pathfinding algorithm known as A* in action. Simply input the start and end nodes, add barriers, and run the A* algorithm to see the shortest path between the two nodes.
#### The interface is easy to use and intuitive, allowing you to focus on exploring the algorithm and experimenting with different scenarios. Give it a try and see for yourself!

## Features and Functionalities:
#### This A* visualizer app is built using Kivy framework which makes it stand out from other A* visualizer apps available online. The app has the following features:
#### • User-friendly interface
#### • Supports start, end, and barrier nodes
#### • Supports erasing barriers
#### • Supports resetting the grid
#### • Supports quitting the app
#### • Uses Manhattan distance as a heuristic for efficient pathfinding
#### • Can be deployed on multiple platforms

## Technologies:
#### Language: Python 3.11.1
#### Framework: kivy 2.2.0
#### In order to run the application please:
#### • clone the repository
#### • download [Python](https://www.python.org/downloads/) if not already done
#### • download [kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) framework and the required dependencies
#### • if your kivy version is different please modify the astar.kv file accordingly

## Usage:
#### Once the app is running you can start interacting with it.
#### • First click set the start node
#### • Second click set the end node
#### • Following clicks will set the barrier nodes
#### • If needed it is possible to erase a barrier node by re-clicking it
#### • To start the algorithm visualiser press -spacebar-
#### • To reset the app press -enter-
#### • To quit the app press -esc- or quit it from the window

## Files:
#### main.py:
#### This file contains the Grid method, the main class of the program. It inherits from Kivy's GridLayout class and has several properties and methods. It sets up and initialize the grid by creating and adding Node widgets to the GridLayout. There are in addition other several methods that manage the user input interactions like the clicking of the nodes and the keyboard inputs to start the algorithm and reset the grid. Moreover the draw_path method reconstruct and highlight the shortest path on the grid.

#### node.py:
#### This file contains the Node class, which represents a single node on the grid. It has attributes such as its position on the grid, and the color options which are called during the development of the algorithm in order to render a dynamic vsualisation.

#### a_star.py:
#### This file contains the A* algorithm implementation. It takes in the start and end nodes, as well as a list of barrier nodes, and returns the shortest path between the start and end nodes. The A* algorithm implemented in the app uses the Manhattan distance heuristic, also known as taxicab geometry. This heuristic calculates the distance between two points as the sum of the absolute differences of their coordinates. The Manhattan distance heuristic is particularly suitable for grid-based pathfinding problems, such as the one implemented in the app, where the movement is restricted to horizontal and vertical directions.

## Challenges Faced:
#### I faced some challenges during development. The biggest challenge was to find a way to make the app unique and stand out from other A* visualizer apps available online. I overcame this challenge by choosing Kivy framework, which not only allowed the app to be deployed on multiple platforms but also made the app visually appealing.

## Future Scope:
#### I plan to add more pathfinding algorithms to the app and also introduce more features to make it more versatile. I also plans to add more functionality to the UI, such as a slider to manage the speed of the visualisation, a menu for choosing between the algorithms and displaying the number of nodes expanded and the time taken to find the shortest path.

## Sources:
#### • [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) Wikipedia
#### • [Introduction to A*](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html) by Amit Patel
#### • [A* Pathfinding (E01: algorithm explanation)](https://www.youtube.com/watch?v=-L-WgKMFuhE&t=198s) by Sebastian Lague
#### • [A* Pathfinding Visualization Tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A&t=314s) by Tech with Tim
#### • [Pathfinding Algorithm Visualizer](https://www.youtube.com/watch?v=ZllpOjf6Glg&t=47s) by Daria Vasileva
#### • [Kivy Course - Create Python Games and Mobile Apps](https://www.youtube.com/watch?v=l8Imtec4ReQ&t=18698s) by Jonathan Roux (freeCodeCamp)

## Contact:
#### pierpaolo.capra@outlook.com
#### [GitHub repository](https://github.com/Pierpaolo-C/Astar)


### My name is Pierpaolo Capra and this was CS50!