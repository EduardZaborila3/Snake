# Minimalist Snake Game

A minimalist implementation of the classic Snake game developed in Python using the Pygame library. This project features toroidal map mechanics (screen wrapping) and an instant restart system, focusing on clean code and simple gameplay loop.

## Features

* **Classic Mechanics:** Traditional snake movement and growth mechanics upon consuming food.
* **Screen Wrapping:** The game map is continuous. Exiting the screen boundaries transports the snake to the opposite side (e.g., exiting left reappears on the right).
* **Collision Detection:** The game ends only when the snake collides with its own body.
* **Score Display:** The final score is displayed on the Game Over screen.
* **Instant Restart:** Players can immediately reset the game state by pressing the 'R' key after losing.

## Prerequisites

Ensure the following are installed on your system:

* Python 3.x
* Pygame library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
   ```
2. Install the required dependencies:
   ```bash
   pip install pygame
   ```
   
## Usage
* **To start the game, run the main script from the terminal:**
  ```bash
  python app.py
  ```

## Controls
* **Direction Keys:** W(Up), S(Down), A(Left), D(Right)
* **Other Keys:** R (Restart the game)

## Future improvements
* **This project is currently in its initial version. Planned features include:**
  * Implementation of a high-score system with local storage.
  * Progressive difficulty (speed increase).
  * Start menu interface.
