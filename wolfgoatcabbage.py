"""WOLFGOATCABBAGE implementation and main
Created By: Kim Eaton and Luciano Gibertoni
Date: 2/27/2022
"""

from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial=frozenset({'F','G', 'W', 'C'}), goal=frozenset({})):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)


    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list. """

        possible_actions = []
## needs when action={F,G} in initial state == {W,C}
##when action={F,C} in state={W} == {F,W,C}

        if state == {'F','G','W','C'}:
            possible_actions.append({'G', 'F'})
        elif state == {'C','W'}:
            possible_actions.append({'F'})
        elif state == {'F', 'W', 'C'}:
            possible_actions.append({'W','F'})
        elif state == {'C'}:
            possible_actions.append({'G', 'F'})
        elif state == {'W'}:
            possible_actions.append({'C', 'F'})
        elif state == {'F', 'G', 'C'}:
            possible_actions.append({'C','F'})
        elif state == {'F','W','G'}:
            possible_actions.append({'W','F'})
        elif state == {'G'}:
            possible_actions.append({'F'})
        elif state == {'F', 'G'}:
            possible_actions.append({'G', 'F'})
        elif state == {'W','C'}:
            possible_actions.append({'G', 'F'})

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        new_state = set(state)

        if action == {'G', 'F'}:
            if state == {'F', 'G'} :
                new_state.remove('F')
                new_state.remove('G')
            elif state == {'F','G','W','C'}:
                new_state.remove('F')
                new_state.remove('G')
            elif state == {'C'} or {'W'}:
                new_state.add('F')
                new_state.add('G')
        elif action == {'W','F'}:
            new_state.remove('F')
            new_state.remove('W')
        elif action == {'C','F'}:
            if state == {'W'}:
                new_state.add('F')
                new_state.add('C')
            elif state == {'F', 'G', 'C'}:
                new_state.remove('F')
                new_state.remove('C')
        elif action == {'F'}:
            new_state.add('F')


        return frozenset(new_state)

    def goal_test(self, state):
     """ Given a state, return True if state is a goal state or False, otherwise """
     return state == self.goal


if __name__ == '__main__':

    wgc = WolfGoatCabbage()
    print("initial: ")
    print(wgc.initial)
    print("goal: ")
    print(wgc.goal)
    print("goal_test: ")
    print(wgc.goal_test(frozenset({})))
    print("result: ")
    print(wgc.result(frozenset({'F', 'C', 'W', 'G'}), frozenset({'F', 'G'})))
    print("actions: ")
    print(wgc.actions(frozenset({'F', 'W', 'G', 'C'})))
    print("DFS solution:")
    print(depth_first_graph_search(wgc).solution())
    print("BFS solution:")
    print(breadth_first_graph_search(wgc).solution())
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
