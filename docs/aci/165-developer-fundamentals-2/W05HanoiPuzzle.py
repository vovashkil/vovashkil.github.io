def tower_of_hanoi(number_of_disks, source, destination, helper):
    moves = 1
    if number_of_disks == 1:
        # Base case: when there is only one disk left to move
        print(f"Move disk {number_of_disks} from rod {source} to rod {destination}")
    else:
        # Recursive case: when there are more disks to move than 1
        # move all but last disk from source to helper rod
        # destination thus becomes the new helper rod
        moves += tower_of_hanoi(number_of_disks - 1, source, helper, destination)
        # move the largest disk from the source to the target
        print(f"Move disk {number_of_disks} from rod {source} to rod {destination}")
        # move tower reduced by one from helper rod to the target
        moves += tower_of_hanoi(number_of_disks - 1, helper, destination, source)

    return moves


# Driver code
n = 5
result = tower_of_hanoi(n, 'A', 'C', 'B')  # A, C, B are the names of rods

# Print the total number of moves
print(f"Total moves: {result}")