import numpy as np

# ---input row number---
rowInput = 0
while True:
    rowInput = input("Input how many rows the dirt map has: ")
    try:
        rowInput = int(rowInput)
        if rowInput <= 0:
            print("Sorry, row number should be a positive integer. Try again.")
            continue
        break
    except ValueError:
        print("Please input an int:")
        continue
print("The dirt_map has " + str(rowInput) + " rows.\n")
# ---input row number end---


# ---input column number---
columnInput = 0
while True:
    columnInput = input("Input how many columns the dirt map has: ")
    try:
        columnInput = int(columnInput)
        if columnInput <= 0:
            print("Sorry, row number should be a positive integer. Try again.")
            continue
        break
    except ValueError:
        print("Please input an int:")
        continue
print("The dirt map has " + str(columnInput) + " columns.\n")
# ---input column number end---


# =====================Environment Simulator Begin=====================
# ---generate a random dirt map and agent starting position given the row and column numbers---

x = rowInput
y = columnInput
dirt_map = np.empty((x, y), dtype=int)
stPosX = 0
stPosY = 0
dirtCounter = 0

if (x > 0) and (y > 0):
    # dirt_map = np.empty((x,y), dtype = bool)
    stPosX = np.random.randint(0, x)
    stPosY = np.random.randint(0, y)
    strPos = dirt_map[stPosX][stPosY]
    for i in range(0, x):
        for j in range(0, y):
            dirt_map[i][j] = bool(np.random.choice([0, 1]))
            if dirt_map[i][j] == 1:
                dirtCounter += 1
elif (x > 0) and (y == 0):
    dirt_map = np.zeros((x, 1), dtype=int)
    stPosX = np.random.randint(0, x)
    # stPosY = 0
    strPos = dirt_map[stPosX][0]
    for i in range(0, x):
        dirt_map[i][0] = bool(np.random.choice([0, 1]))
        if dirt_map[i][0] == 1:
            dirtCounter += 1
elif (x == 0) and (y > 0):
    dirt_map = np.zeros((1, y), dtype=int)
    # stPosX = 0
    stPosY = np.random.randint(0, y)
    strPos = dirt_map[0][stPosY]
    for j in range(x, y):
        dirt_map[0][j] = bool(np.random.choice([0, 1]))
        if dirt_map[0][j] == 1:
            dirtCounter += 1
# ---generate a random dirt map and agent starting position given the row and column numbers ends---
# =====================Environment Simulator End=====================

print("The randomized environment looks like:\n")
print(dirt_map)
print("\nThe starting position is: dirt_map[" + str(stPosX) + "][" + str(stPosY) + "].")
print("\nThere is/are " + str(dirtCounter) + " dirty square(s) in the dirt_map.")

cPosX = stPosX
cPosY = stPosY

print("\nAgent is now at dirt_map[" + str(cPosX) + "][" + str(cPosY) + "].")

# =====================Agent Begin=====================
def agent(cPosX, cPosY, dirt_map):
    # ---------------------sensor begin---------------------
    pos = 0

    def sensor(cPosX, cPosY, dirt_map):
        global pos
        if cPosX == 0 and cPosY == 0:
            pos = 0
        elif cPosX == 0 and 0 < cPosY < y - 1:
            pos = 1
        elif cPosX == 0 and cPosY == y - 1:
            pos = 2
        elif 0 < cPosX < x - 1 and cPosY == 0:
            pos = 3
        elif 0 < cPosX < x - 1 and 0 < cPosY < y - 1:
            pos = 4
        elif 0 < cPosX < x - 1 and cPosY == y - 1:
            pos = 5
        elif cPosX == x - 1 and cPosY == 0:
            pos = 6
        elif cPosX == x - 1 and 0 < cPosY < y - 1:
            pos = 7
        elif cPosX == x - 1 and cPosY == y - 1:
            pos = 8
        return pos

    # ---------------------sensor end---------------------

    # ---------------------actuator begin---------------------
    dirt = dirt_map[cPosX][cPosY]

    def actuator(pos, dirt):
        def clean():
            global dirt_map
            global cPosX
            global cPosY
            if dirt == 1:
                dirt_map[cPosX][cPosY] = 0
                print("\nThe dirt in dirt_map[" + str(cPosX) + "][" + str(cPosY) + "] is cleaned!")
                print("\nNow the environment looks like: \n")
                print(dirt_map)
            else:
                print("\nThere's no dirt in dirt_map[" + str(cPosX) + "][" + str(cPosY) + "]!")

        actList = [0]

        def chooseMov(pos):
            global actList
            if pos == 0:
                actList = [1, 3]
            elif pos == 1:
                actList = [0, 1, 3]
            elif pos == 2:
                actList = [0, 3]
            elif pos == 3:
                actList = [1, 2, 3]
            elif pos == 4:
                actList = [0, 1, 2, 3]
            elif pos == 5:
                actList = [0, 2, 3]
            elif pos == 6:
                actList = [1, 2]
            elif pos == 7:
                actList = [0, 1, 2]
            elif pos == 8:
                actList = [0, 2]
            return actList

        def movAct(actList):
            move = ""
            mov_num = np.random.choice(actList)
            global cPosX
            global cPosY
            if mov_num == 0:
                move = "MOVE LEFT"
                cPosY -= 1
            elif mov_num == 1:
                move = "MOVE RIGHT"
                cPosY += 1
            elif mov_num == 2:
                move = "MOVE UP"
                cPosX -= 1
            elif mov_num == 3:
                move = "MOVE DOWN"
                cPosX += 1
            print("\nTake action: '" + move + "'")
            print("\nNow agent is at point: dirt_map[" + str(cPosX) + "][" + str(cPosY) + "]")
            return cPosX, cPosY, mov_num

        clean()
        movAct(chooseMov(sensor(cPosX, cPosY, dirt_map)))
        # return

    # ---------------------actuator end---------------------

    sensor(cPosX, cPosY, dirt_map)
    actuator(pos, dirt)


# =====================Agent Ends=====================

# ---------------------performance grader begin---------------------

def grader(dirtCounter):
    i = 0
    j = 0
    dirtRam = 0
    for i in range(rowInput):
        for j in range(columnInput):
            if dirt_map[i][j] == 1:
                dirtRam += 1
    # print("\nThere are " + str(dirtCounter - dirtRam) + "dirty square(s) cleaned.")
    # print("\n" + str(dirtRam) + " dirty square(s) left.")
    return dirtRam


# ---------------------performance grader end---------------------

steps = int(input("\nInput how many steps you wanna run with this agent: "))
n = 0
while n < steps:
    agent(cPosX, cPosY, dirt_map)
    n += 1

print("\nAfter " + str(steps) + " moves, there are " + str(dirtCounter - grader(dirtCounter)) +
      " dirty square(s) cleaned, "
      + str(grader(dirtCounter)) + " dirty square(s) left.")

input("\n\nThat's CS534 1st Assignment. Press any key to continue...")
