import pygame
import time
import sys
from random import randint
from classes import Hanoi_Disk
from classes import Hanoi_Rod

# Number of disks.
n = 4

# Initiating pygame
pygame.init()

# Width of the screen.
screen_width = 800
# Height of the screen.
screen_height = 600

# Screen that's going to be displayed.
screen = pygame.display.set_mode((screen_width, screen_height))

# Width distance between towers.
towers_dist = screen_width / 16
# Height distance of the towers
towers_height = screen_height * 0.9

# Height of the tower's base.
towers_base_height = screen_height / 16
# Width of the tower's base
towers_base_width = (screen_width - 4 * towers_dist) / 3

# Height of the tower's rod.
towers_rod_height = screen_height * 0.7
# Width of the tower's rod.
towers_rod_width = screen_width / 16

# Height of the disk.
disk_height = screen_height * 0.05
# Base width of a disk.
disk_width = screen_width * 0.1


# Function to handle pygame events.
def pygame_events_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Function to introduce delay between movements.
def delay(seconds):
    start_t = time.time()
    while True:
        pygame_events_handler()
        if time.time() - start_t > seconds:
            break


# Function for updating the towers state
def update_towers(first_tower, second_tower, third_tower):
    screen.fill((58, 200, 207))
    first_tower.display()
    second_tower.display()
    third_tower.display()
    pygame.display.flip()


# Algorithm for solving the Tower of Hanoi
def tower_of_hanoi(n_rings, first_tower, third_tower, second_tower):
    if n_rings == 1:
        # Creating delay
        delay(1)
        # Moving a disk
        third_tower.add_disk(first_tower.remove_disk())
        # Updating the screen
        update_towers(first_tower, second_tower, third_tower)
        return

    tower_of_hanoi(n_rings - 1, first_tower, second_tower, third_tower)
    # Creating delay
    delay(1)
    # Moving a disk
    third_tower.add_disk(first_tower.remove_disk())
    # Updating the screen
    update_towers(first_tower, second_tower, third_tower)
    tower_of_hanoi(n_rings - 1, second_tower, third_tower, first_tower)


if __name__ == "__main__":
    # Verifying if the input is valid.
    try:
        if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
            n = int(sys.argv[1])
    except ValueError:
        print("The input isn't valid")
        print("The default value (4) will be used.")
        pass

    # List of the disks.
    disks = []

    # Constructing the disks and the towers.
    for i in range(n):
        disks.append(Hanoi_Disk(disk_height, disk_width + 10 * (n - i), i + 1, towers_dist + towers_base_width / 2,
                                towers_height, (randint(0, 255), randint(0, 255), randint(0, 255)), screen))

    first_rod = Hanoi_Rod(towers_base_height, towers_base_width, towers_rod_height, towers_rod_width,
                          towers_dist, towers_height, disks, screen)

    second_rod = Hanoi_Rod(towers_base_height, towers_base_width, towers_rod_height, towers_rod_width,
                           2 * towers_dist + towers_base_width, towers_height, [], screen)

    third_rod = Hanoi_Rod(towers_base_height, towers_base_width, towers_rod_height, towers_rod_width,
                          3 * towers_dist + 2 * towers_base_width, towers_height, [], screen)

    # Showing the initial state
    update_towers(first_rod, second_rod, third_rod)

    # Calling the algorithm
    tower_of_hanoi(n, first_rod, third_rod, second_rod)

    while True:
        pygame_events_handler()
