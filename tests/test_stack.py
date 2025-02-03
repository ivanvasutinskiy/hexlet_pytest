from hexlet_pytest.stack import stack

def test_steck1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'

def test_steck2():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)
    stack.pop()
    assert not stack