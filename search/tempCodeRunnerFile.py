totalCost = 0
    curPoint = position
    while foodToEat:
        heuristic_cost, food = \
            min([(util.manhattanDistance(curPoint, food), food) for food in foodToEat])
        foodToEat.remove(food)
        curPoint = food
        totalCost += heuristic_cost

    return totalCost