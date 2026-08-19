# There are 3 rods:

# Source (A)
# Auxiliary (B)
# Destination (C)

# And N disks of different sizes.

# Initially, all disks are on the Source rod in decreasing size order (largest at bottom).

# Goal:
# Move all disks from Source → Destination.


def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case
    if n == 1:
        print(f"Move Disk 1 from {source} to {destination}")
        return

    # Move n-1 disks to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move largest disk
    print(f"Move Disk {n} from {source} to {destination}")

    # Move n-1 disks to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


tower_of_hanoi(3, 'A', 'B', 'C')

