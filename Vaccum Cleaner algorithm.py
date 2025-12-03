# Vacuum Cleaner Agent (Simple Reflex Agent)

environment = {
    "A": "Dirty",
    "B": "Dirty"
}

agent_position = "A"

def print_env(env):
    for room in env:
        print(room, ":", env[room])

print("Before cleaning:")
print_env(environment)

def vacuum_cleaner(env, pos):
    if env[pos] == "Dirty":
        env[pos] = "Clean"

    if pos == "A":
        return "B"
    else:
        return "A"

# Agent cleans A
agent_position = vacuum_cleaner(environment, agent_position)

# Agent cleans B
agent_position = vacuum_cleaner(environment, agent_position)

print("\nAfter cleaning:")
print_env(environment)
