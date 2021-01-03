from calculator.assets.modules.calculator import Actions, List_actions

actions = Actions()
list_actions = List_actions()

assert actions.add(1, 2) == 3
assert actions.multiply(2, 3) == 6

assert list_actions.add([1, 2, 3]) == 6
assert list_actions.multiply([1, 2, 3, 4]) == 24
