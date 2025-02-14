# AI Dungeon Escape

## Overview
AI Dungeon Escape is a grid-based game built using Python and Pygame. The game features an AI-controlled player that navigates through a dungeon filled with obstacles, traps, and rewards, using the A* pathfinding algorithm to reach the exit.

## Features
- **A* Pathfinding Algorithm**: Implements A* search to find the optimal path from the player's starting position to the dungeon exit.
- **Dynamic Grid Generation**: Each game generates a unique grid layout with random obstacles, traps, gold, healing spots, and speed boosts.
- **Game Elements**:
  - Obstacles (`O`): Blocks movement.
  - Traps (`T`): Reduce player health.
  - Gold (`G`): Increases player's score.
  - Healing Spots (`H`): Restores health.
  - Speed Boosts (`S`): Temporarily speeds up movement.
  - Exit (`E`): The goal of the game.
- **Visual Representation**: Uses Pygame to render the game grid and display real-time updates of the player's health and gold count.

## How It Works
1. The grid is generated with various elements randomly placed.
2. The player starts at (0,0) and follows the path found using the A* algorithm to reach the exit.
3. The player interacts with the grid elements, gaining or losing health and gold based on the encountered objects.
4. The game runs in a loop, updating movement at each step until the player either reaches the exit or runs out of health.

## Installation & Setup
1. Ensure you have Python installed (version 3.x recommended).
2. Install Pygame if you haven't already:
   ```sh
   pip install pygame
   ```
3. Run the game using:
   ```sh
   python main.py
   ```

## My Contributions
This project is a demonstration of my knowledge in AI, pathfinding algorithms, and game development using Python. I implemented the following:
- **A* Pathfinding**: Optimized the pathfinding logic to ensure efficient movement through the dungeon.
- **Game Mechanics**: Designed interactive elements such as traps, healing spots, and gold collection to add strategy.
- **Visual Representation**: Developed the rendering of the game board using Pygame.
- **Dynamic Grid System**: Created a procedural grid generator for replayability.

## Future Improvements
- **Enhanced AI Behavior**: Introduce dynamic obstacles or moving enemies.
- **User Interaction**: Allow manual player control alongside AI navigation.
- **Scoring System**: Implement a leaderboard to track best runs.
- **Save/Load Feature**: Enable saving game progress.

## License
This project is open-source and available for modification and improvement. Feel free to experiment and enhance the game!

---
Developed with passion for AI and game development.

