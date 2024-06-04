# enumerate() is build in function that allows to iterate over a sequence while keeping track of the index of each item
states = ['virginia', 'new jersey', 'north carolina', 'california']

for index, state in enumerate(states,start=101):
    print(f"State {index}: {state}")