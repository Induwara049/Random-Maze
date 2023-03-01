import random

# Creating the Maze
print()
print("........The Maze........")
print()
length = 6
width = 6

Maze = []
for i in range(0, length):
    line = []
    for j in range(0, width):
        line.append(0)
    Maze.append(line)

startingColumn = random.randint(0, 1)
startingRow = random.randint(0, 5)

endingColumn = random.randint(4, 5)
endingRow = random.randint(0, 5)

Maze[startingRow][startingColumn] = 5
Maze[endingRow][endingColumn] = 8

count = 0
while (count < 4):
    barrierCol = random.randint(0, 5)
    barrierRow = random.randint(0, 5)
    if (barrierCol == startingColumn and barrierRow == startingRow) or (barrierCol == endingColumn and barrierRow == endingRow):
        count = count
        continue
    Maze[barrierRow][barrierCol] = 1
    count += 1

for i in Maze:
    print(i, "\n")


# Creating the Stack

def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    return stack.pop()


Stack = create_stack()

# Having a list to store path
print()
print("........DFS Search........")
print()
path = []


found = False  # checking status

# Start node
X = startingRow
Y = startingColumn
startNode = {X: Y}
currentNode = {X: Y}


path.append(startNode)  # startNode added to path

push(Stack, (startNode))

firstSearch = Maze[X][Y - 1]

secondSearch = Maze[X - 1][Y]

thirdSearch = -1
if X < 5:
    thirdSearch = Maze[X + 1][Y]

fourthSearch = -1
if Y < 5:
    fourthSearch = Maze[X][Y + 1]

fifthSearch = -1
if X < 5 and Y > 0:
    fifthSearch = Maze[X + 1][Y - 1]

sixthSearch = -1
if Y > 0 and X > 0:
    sixthSearch = Maze[X - 1][Y - 1]

seventhSearch = -1
if Y < 5 and X > 0:
    seventhSearch = Maze[X - 1][Y + 1]

eighthSearch = -1
if Y < 5 and X < 5:
    eighthSearch = Maze[X + 1][Y + 1]

a = 0
while a < 36:
    if (firstSearch == 0 or firstSearch == 8) and (Y != 0):
        if Maze[X][Y - 1] == 8:
            print('!! Path Found !! ')
            X = X
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X][Y - 1] = -1
        X = X
        Y = Y - 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X < 5:
            thirdSearch = Maze[X + 1][Y]
        if Y < 5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (secondSearch == 0 or secondSearch == 8) and (X != 0):
        if Maze[X - 1][Y] == 8:
            print('!! Path Found !! ')
            X = X - 1
            Y = Y
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X - 1][Y] = -1
        X = X - 1
        Y = Y
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y < 5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (thirdSearch == 0 or thirdSearch == 8) and (X != 5):
        if Maze[X + 1][Y] == 8:
            print('!! Path Found !! ')
            X = X + 1
            Y = Y
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X + 1][Y] = -1
        X = X + 1
        Y = Y
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y < 5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (fourthSearch == 0 or fourthSearch == 8) and (Y != 5):
        if Maze[X][Y + 1] == 8:
            print('!! Path Found !! ')
            X = X
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X][Y + 1] = -1
        X = X
        Y = Y + 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y<5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (fifthSearch == 0 or fifthSearch == 8) and (X != 5 and Y != 0):
        if Maze[X + 1][Y - 1] == 8:
            print('!! Path Found !! ')
            X = X + 1
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X + 1][Y - 1] = -1
        X = X + 1
        Y = Y - 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y<5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (sixthSearch == 0 or sixthSearch == 8) and (X != 0 and Y != 0):
        if Maze[X - 1][Y - 1] == 8:
            print('!! Path Found !! ')
            X = X - 1
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X - 1][Y - 1] = -1
        X = X - 1
        Y = Y - 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y<5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (seventhSearch == 0 or seventhSearch == 8) and (X != 0 and Y != 5):
        if Maze[X - 1][Y + 1] == 8:
            print('!! Path Found !! ')
            X = X - 1
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X - 1][Y + 1] = -1
        X = X - 1
        Y = Y + 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y<5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    elif (eighthSearch == 0 or eighthSearch == 8) and (X != 5 and Y != 5):
        if Maze[X + 1][Y + 1] == 8:
            print('!! Path Found !! ')
            X = X + 1
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            found = True
            break
        Maze[X + 1][Y + 1] = -1
        X = X + 1
        Y = Y + 1
        currentNode = {X: Y}
        push(Stack, (currentNode))
        path.append(currentNode)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X<5:
            thirdSearch = Maze[X + 1][Y]
        if Y<5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]
        a += 1

    else:
        pop(Stack)
        currentNode = {}
        for i in Stack:
            currentNode = i
        X = list(currentNode.keys())[0]
        Y = currentNode.get(X)
        firstSearch = Maze[X][Y - 1]
        secondSearch = Maze[X - 1][Y]
        if X < 5:
            thirdSearch = Maze[X + 1][Y]
        if Y < 5:
            fourthSearch = Maze[X][Y + 1]
        if X < 5 and Y > 0:
            fifthSearch = Maze[X + 1][Y - 1]
        if Y > 0 and X > 0:
            sixthSearch = Maze[X - 1][Y - 1]
        if Y < 5 and X > 0:
            seventhSearch = Maze[X - 1][Y + 1]
        if Y < 5 and X < 5:
            eighthSearch = Maze[X + 1][Y + 1]

print("Path : ", path)
print()
print("Stack : ", Stack)

if found == True:
    time = len(path)
    print()
    print('Time to reach the goal node : ' + str(time) + ' minutes')


def resetMaze():
    for x in range(0, 6):
        for y in range(0, 6):
            if (Maze[x][y] == -1):
                Maze[x][y] = 0


resetMaze()


def heuristicCostCal():
    count_y = 0
    goal_Y = endingRow
    goal_X = endingColumn
    global heuristic_value
    heuristic_value = {}
    while count_y < 6:
        count_x = 0
        while count_x < 6:
            heuristic_cost = max(abs(count_x - goal_X), abs(count_y - goal_Y))
            heuristic_value[count_y,count_x] = heuristic_cost
            # print('heusristic cost for ' + str(count_y) + ',' + str(count_x) + ' are ' + str(heuristic_cost))
            count_x += 1
        count_y += 1
    print()
    print("Heuristic costs : ", heuristic_value)


heuristicCostCal()

print()
print()
def Astar():
    print('........A* Search........')
    print()
    X = startingRow
    Y = startingColumn

    currentNode = {X: Y}
    path = []
    path.append(currentNode)
    gN = 1

    n = 1
    while(n < 36):

        minimum = {}  # having a dictionary to store costs

        # calculating f cost
        if (Y != 0) and (Maze[X][Y - 1] == 0 or Maze[X][Y - 1] == 8):
            left_h_cost = heuristic_value.get((X, Y - 1))
            left_actual_cost = gN + left_h_cost
            minimum["Left"] = left_actual_cost
        if (X != 0) and (Maze[X - 1][Y] == 0 or Maze[X - 1][Y] == 8):
            top_h_cost = heuristic_value.get((X - 1, Y))
            top_actual_cost = gN + top_h_cost
            minimum["Top"] = top_actual_cost
        if (X != 5) and (Maze[X + 1][Y] == 0 or Maze[X + 1][Y] == 8):
            bottom_h_cost = heuristic_value.get((X + 1, Y))
            bottom_actual_cost = gN + bottom_h_cost
            minimum["Bottom"] = bottom_actual_cost
        if (Y != 5) and (Maze[X][Y + 1] == 0 or Maze[X][Y + 1] == 8):
            right_h_cost = heuristic_value.get((X, Y + 1))
            right_actual_cost = gN + right_h_cost
            minimum["Right"] = right_actual_cost
        if (X != 5 and Y != 0) and (Maze[X + 1][Y - 1] == 0 or Maze[X + 1][Y - 1] == 8):
            bottomLeft_h_cost = heuristic_value.get((X + 1, Y - 1))
            bottomLeft_actual_cost = gN + bottomLeft_h_cost
            minimum["BottomLeft"] = bottomLeft_actual_cost
        if (X != 0 and Y != 0) and (Maze[X - 1][Y - 1] == 0 or Maze[X - 1][Y - 1] == 8):
            topLeft_h_cost = heuristic_value.get((X - 1, Y - 1))
            topLeft_actual_cost = gN + topLeft_h_cost
            minimum["TopLeft"] = topLeft_actual_cost
        if (X != 0 and Y != 5) and (Maze[X - 1][Y + 1] == 0 or Maze[X - 1][Y + 1] == 8):
            topRight_h_cost = heuristic_value.get((X - 1, Y + 1))
            topRight_actual_cost = gN + topRight_h_cost
            minimum["TopRight"] = topRight_actual_cost
        if (X != 5 and Y != 5) and (Maze[X + 1][Y + 1] == 0 or Maze[X + 1][Y + 1] == 8):
            bottomRight_h_cost = heuristic_value.get((X + 1, Y + 1))
            bottomRight_actual_cost = gN + bottomRight_h_cost
            minimum["BottomRight"] = bottomRight_actual_cost

        minimum_actual_cost = min(minimum, key=minimum.get)

        if (minimum_actual_cost == "Left"):
            Maze[X][Y] = -1
            X = X
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if(Maze[X][Y]==8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "Top"):
            Maze[X][Y] = -1
            X = X - 1
            Y = Y
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "Bottom"):
            Maze[X][Y] = -1
            X = X + 1
            Y = Y
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "Right"):
            Maze[X][Y] = -1
            X = X
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "BottomLeft"):
            Maze[X][Y] = -1
            X = X + 1
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "TopLeft"):
            Maze[X][Y] = -1
            X = X - 1
            Y = Y - 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "TopRight"):
            Maze[X][Y] = -1
            X = X - 1
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

        elif (minimum_actual_cost == "BottomRight"):
            Maze[X][Y] = -1
            X = X + 1
            Y = Y + 1
            currentNode = {X: Y}
            path.append(currentNode)
            n += 1
            if (Maze[X][Y] == 8):
                print('!! Path Found !! ')
                print('Path : ', path)
                break

    print()
    time = len(path)
    print('Time to reach the goal node : ' + str(time) + ' minutes')
print()
Astar()
