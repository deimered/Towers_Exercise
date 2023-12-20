import pygame


# Class to represent the disks.
class Hanoi_Disk:
    def __init__(self, disk_height, disk_width, disk_level, x_dist, y_dist, color, screen):
        self.__disk_height = disk_height
        self.__disk_width = disk_width
        self.__disk_level = disk_level
        self.__x_dist = x_dist
        self.__y_dist = y_dist
        self.__color = color
        self.__screen = screen
        self.__disk = pygame.Rect(self.__x_dist - self.__disk_width / 2,
                                  self.__y_dist - self.__disk_height * disk_level,
                                  self.__disk_width, self.__disk_height)

    def move(self, rod_pos, disk_level):
        self.__disk.move_ip(rod_pos - (self.__disk.x + self.__disk.width / 2),
                            self.__disk.height * self.__disk_level - self.__disk_height * disk_level)
        self.__disk_level = disk_level

    def display(self):
        pygame.draw.rect(self.__screen, self.__color, self.__disk, 0, 15, 15, 15, 15)
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__disk, 1, 15, 15, 15, 15)


# Class to represent the rods.
class Hanoi_Rod:
    def __init__(self, base_height, base_width, rod_height, rod_width, x_dist, y_dist, disks, screen):
        self.__base_height = base_height
        self.__base_width = base_width
        self.__rod_height = rod_height
        self.__rod_width = rod_width
        self.__x_dist = x_dist
        self.__y_dist = y_dist
        self.__disks = disks
        self.__screen = screen

        self.__tower_base = pygame.Rect(self.__x_dist, self.__y_dist, self.__base_width, self.__base_height)
        self.__tower_rod = pygame.Rect(self.__x_dist + self.__base_width / 2 - self.__rod_width / 2,
                                       self.__y_dist - self.__rod_height, self.__rod_width, self.__rod_height)

    def remove_disk(self):
        if len(self.__disks) > 0:
            return self.__disks.pop()

    def add_disk(self, disk):
        disk.move(self.__x_dist + self.__base_width / 2, len(self.__disks) + 1)
        self.__disks.append(disk)

    def display(self):
        pygame.draw.rect(self.__screen, (255, 255, 0), self.__tower_rod, 0, 0, 15, 15, 0)
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__tower_rod, 1, 0, 15, 15, 0)

        pygame.draw.rect(self.__screen, (255, 255, 0), self.__tower_base, 0, 15, 15, 15, 15)
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__tower_base, 1, 15, 15, 15, 15)

        for disk in self.__disks:
            disk.display()
