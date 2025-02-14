import pygame
import heapq
import random


GRID_SIZE = 20
CELL_SIZE = 40
WINDOW_SIZE = GRID_SIZE * CELL_SIZE


pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI Dungeon Escape")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Colors for different elements
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Heuristic function for A* algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm for pathfinding
def a_star_search(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < GRID_SIZE and 0 <= next_cell[1] < GRID_SIZE:
                if grid[next_cell[1]][next_cell[0]] != "O":
                    new_cost = cost_so_far[current] + 1
                    if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                        cost_so_far[next_cell] = new_cost
                        priority = new_cost + heuristic(goal, next_cell)
                        heapq.heappush(open_list, (priority, next_cell))
                        came_from[next_cell] = current
    return []  # Return empty path if no path found

# Reconstructs the path
def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []  # No path found
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Generates the game grid
def generate_grid():
    grid = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for _ in range(GRID_SIZE * 3):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "O"
    for _ in range(GRID_SIZE):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "T"
    for _ in range(GRID_SIZE):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "G"
    for _ in range(GRID_SIZE // 2):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "H"
    for _ in range(GRID_SIZE // 2):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = "S"
    grid[GRID_SIZE - 1][GRID_SIZE - 1] = "E"
    return grid, (0, 0)

# Draws the grid
def draw_grid(grid, player):
    screen.fill(WHITE)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == "O":
                pygame.draw.rect(screen, BLACK, rect)
            elif grid[y][x] == "T":
                pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3)
            elif grid[y][x] == "G":
                pygame.draw.circle(screen, GOLD, rect.center, CELL_SIZE // 3)
            elif grid[y][x] == "H":
                pygame.draw.circle(screen, GREEN, rect.center, CELL_SIZE // 3)
            elif grid[y][x] == "S":
                pygame.draw.circle(screen, CYAN, rect.center, CELL_SIZE // 3)
            elif grid[y][x] == "E":
                pygame.draw.rect(screen, PURPLE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
    pygame.draw.rect(screen, BLUE, pygame.Rect(player[0] * CELL_SIZE, player[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw UI elements
def draw_ui(player_hp, player_gold):
    hp_text = font.render(f"HP: {player_hp}", True, BLACK)
    gold_text = font.render(f"Gold: {player_gold}", True, BLACK)
    screen.blit(hp_text, (10, 10))
    screen.blit(gold_text, (10, 40))

# Main function
def main():
    grid, player = generate_grid()
    player_hp = 100
    player_gold = 0
    exit_pos = (GRID_SIZE - 1, GRID_SIZE - 1)
    
    path = a_star_search(grid, player, exit_pos)
    if not path:
        print("No path found! Game over.")
        return

    running = True
    step = 0
    while running:
        clock.tick(7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        if step < len(path):
            player = path[step]
            x, y = player
            if grid[y][x] == "T":
                player_hp -= 15
            elif grid[y][x] == "G":
                player_gold += 10
            elif grid[y][x] == "H":
                player_hp += 10
            elif grid[y][x] == "S":
                clock.tick(14)
            grid[y][x] = " "
            step += 1

        draw_grid(grid, player)
        draw_ui(player_hp, player_gold)
        pygame.display.flip()

        if player_hp <= 0 or player == exit_pos:
            running = False
    
    pygame.quit()

main()
