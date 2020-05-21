# Snake Game

Built using Python and the `turle` library. Simple implementation of the `turtle` library to show kids I was tutoring that the library was more than just about drawing lines.

## `snake.py`

Playable snake game where Up, Left, Down, Right keys control the Snake. Includes session-based scoring system, auto-reset of game upon collision with side walls or with itself.


## `snake_spath.py`

Automated snake solver using spath (optimal path through grid) where user is still able to control the snake with  Up, Left, Down, Right keys. Snake automatically changes path to optimal path in order to avoid colliding with side walls and itself even with user-controlled changes, maximising score. Delay between frames is set to `0.01` in order to highlight the optimal path that the snake is traversing. Increase the delay between frames to make it more playable.


## `snake_BFS.py`

Snake solver using Best First Search heuristic by calculating the manhattann distance between the food and all possible paths of the snake head to find the optimal path to the food form any given location.
