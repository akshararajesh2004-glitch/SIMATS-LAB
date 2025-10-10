
actions = [
    ("Cook", {"IngredientsReady"}, {"MealReady"}),
    ("PrepareIngredients", set(), {"IngredientsReady"}),
    ("Eat", {"MealReady"}, set())
]

def pop(plan, goals, state):
    if not goals: 
        return plan
    goal = goals.pop()
    for name, pre, eff in actions:
        if goal in eff:
            new_goals = list(pre - state)
            result = pop(plan + [name], new_goals, state.union(eff))
            if result:
                return result
    return None

initial_state = set()
goal_state = ["MealReady"]

plan = pop([], goal_state, initial_state)
print("Plan:", plan)
