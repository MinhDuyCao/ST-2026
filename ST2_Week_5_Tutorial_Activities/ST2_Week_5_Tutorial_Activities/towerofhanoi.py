# TowerOfHanoi_CountMoves.py

count = 0  # Global counter

def main():
    global count
    n = eval(input("Enter number of disks: "))
    count = 0  # Reset counter
    moveDisks(n, 'A', 'B', 'C')
    print("Total number of moves:", count)

def moveDisks(n, fromTower, toTower, auxTower):
    global count
    if n == 1:
        print("Move disk 1 from", fromTower, "to", toTower)
        count += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        count += 1
        moveDisks(n - 1, auxTower, toTower, fromTower)

main()