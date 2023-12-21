import sys


# Algorithm for solving the Tower of Hanoi
def tower_of_hanoi(n_rings, first_tower, third_tower, second_tower):
    if n_rings == 1:
        print(first_tower, ' --> ', third_tower)
        return

    tower_of_hanoi(n_rings - 1, first_tower, second_tower, third_tower)
    print(first_tower, ' --> ', third_tower)
    tower_of_hanoi(n_rings - 1, second_tower, third_tower, first_tower)


if __name__ == "__main__":
    n = 4
    # Verifying if the input is valid.
    try:
        if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
            n = int(sys.argv[1])
    except ValueError:
        print("The input isn't valid")
        print("The default value (4) will be used.")
        pass
    tower_of_hanoi(4, 'A', 'C', 'B')
