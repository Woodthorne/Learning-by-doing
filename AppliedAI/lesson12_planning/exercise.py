from dataclasses import dataclass
from collections import deque

'''
    S: Start
    G: Goal
    K: Key
    D: Door
    #: Wall
    .: Vacant
'''
WORLD = [
    ["S", ".", ".", ".", "."],
    [".", "#", "#", ".", "."],
    [".", ".", "K", "#", "."],
    [".", ".", ".", ".", "D"],
    [".", ".", ".", ".", "G"]
]


@dataclass(frozen=True)
class State:
    agent_pos: tuple  # (x, y)
    has_key: bool
    door_unlocked: bool


# ACTIONS ----> Make move_down, move_left, move_right

def move_up(state:State, world):
    # Steg 1: Kolla om man kan utföra MOVE_UP
    r, c = state.agent_pos
    new_r = r - 1
    if new_r < 0:
        return None  # utanför gränsen
    if world[new_r][c] == "#":
        return None  # vägg
    if world[new_r][c] == "D" and not state.door_unlocked:
        return None  # dörren är låst

    # Steg 2: Returnera nytt tillstånd
    return State(
        agent_pos=(new_r, c),
        has_key=state.has_key,
        door_unlocked=state.door_unlocked
    )

def move_down(state:State, world):
    # Steg 1: Kolla om man kan utföra MOVE_UP
    r, c = state.agent_pos
    new_r = r + 1
    if new_r >= len(world):
        return None  # utanför gränsen
    if world[new_r][c] == "#":
        return None  # vägg
    if world[new_r][c] == "D" and not state.door_unlocked:
        return None  # dörren är låst

    # Steg 2: Returnera nytt tillstånd
    return State(
        agent_pos=(new_r, c),
        has_key=state.has_key,
        door_unlocked=state.door_unlocked
    )

def move_left(state:State, world):
    # Steg 1: Kolla om man kan utföra MOVE_UP
    r, c = state.agent_pos
    new_c = c - 1
    if new_c < 0:
        return None  # utanför gränsen
    if world[r][new_c] == "#":
        return None  # vägg
    if world[r][new_c] == "D" and not state.door_unlocked:
        return None  # dörren är låst

    # Steg 2: Returnera nytt tillstånd
    return State(
        agent_pos=(r, new_c),
        has_key=state.has_key,
        door_unlocked=state.door_unlocked
    )

def move_right(state:State, world):
    # Steg 1: Kolla om man kan utföra MOVE_UP
    r, c = state.agent_pos
    new_c = c + 1
    if new_c >= len(world[0]):
        return None  # utanför gränsen
    if world[r][new_c] == "#":
        return None  # vägg
    if world[r][new_c] == "D" and not state.door_unlocked:
        return None  # dörren är låst

    # Steg 2: Returnera nytt tillstånd
    return State(
        agent_pos=(r, new_c),
        has_key=state.has_key,
        door_unlocked=state.door_unlocked
    )


def pick_up_key(state, world):
    r, c = state.agent_pos
    if world[r][c] != "K":
        return None
    if state.has_key:
        return None

    return State(
        agent_pos=(r, c),
        has_key=True,
        door_unlocked=state.door_unlocked
    )

def unlock_door(state, world):
    r, c = state.agent_pos
    if not state.has_key:
        return None

    # Antingen kräver vi att agenten står exakt på D-rutan
    # eller i en ruta intill D. Justeras efter önskemål.
    if world[r][c] != "D":
        return None

    return State(
        agent_pos=(r, c),
        has_key=state.has_key,
        door_unlocked=True
    )

ACTIONS = {
    "MOVE_UP": move_up,
    "MOVE_DOWN": move_down,
    "MOVE_LEFT": move_left,
    "MOVE_RIGHT": move_right,
    "PICK_UP_KEY": pick_up_key,
    "UNLOCK_DOOR": unlock_door
}


def bfs_plan(start_state, world, goal_test):
    # goal_test är en funktion som kollar om ett tillstånd är målet.
    frontier = deque([(start_state, [])])  # kö av (tillstånd, plan)
    visited = set([start_state])

    while frontier:
        current_state, current_plan = frontier.popleft()

        # Kolla om vi är i mål
        if goal_test(current_state, world):
            return current_plan  # Vi har hittat en plan (sekvens av actions)

        # Annars utforska nästa möjliga tillstånd
        for action_name, action_func in ACTIONS.items():
            new_state = action_func(current_state, world)
            if new_state is not None and new_state not in visited:
                visited.add(new_state)
                new_plan = current_plan + [action_name]
                frontier.append((new_state, new_plan))

    print('Ingen plan hittad!')
    return None  # Ingen plan hittad


def is_goal(state, world):
    r, c = state.agent_pos
    return (world[r][c] == "G")


def execute_plan(state, plan, world):
    current_state = state
    for step, action_name in enumerate(plan):
        print(f"Steg {step}: {action_name} -> ", end="")
        action_func = ACTIONS[action_name]
        new_state = action_func(current_state, world)
        if new_state is None:
            print("Misslyckades att utföra!")
            return
        else:
            current_state = new_state
            print(f"{current_state}")
    print("Plan exekverad!")

if __name__ == '__main__':
    start_state = State((0,0), False, False)
    plan = bfs_plan(start_state, WORLD, is_goal)
    if plan:
        execute_plan(start_state, plan, WORLD)