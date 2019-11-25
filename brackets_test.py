from brackets import solution
#from brackets_canon import solution
# uncomment or comment to switch between solutions

def test_simple():
    assert solution("{}") == True
    assert solution("()") == True
    assert solution("[]") == True

def test_onion():
    assert solution("({[]})") == True
    assert solution("[({})]") == True
    assert solution("{[()]}") == True
    assert solution("[{[()]}]") == True
    assert solution("(([{[()]}]))") == True

def test_simple_fail():
    assert solution("}") == False
    assert solution("[") == False
    assert solution("[}") == False
    assert solution("(}") == False
    assert solution("[)") == False

def test_trailing():
    assert solution("({[]})]") == False
    assert solution("({[]})}") == False
    assert solution("{({[]})") == False
    assert solution("]({[]})") == False

def test_multi_children():
    assert solution("[{}{}]") == True
    assert solution("[{}()]") == True
    assert solution("[{}[()]{}]") == True

def test_single_level():
    assert solution("{}[]") == True
    assert solution("{}(]") == False

def test_single_level_with_children():
    assert solution("{[]}[()]") == True
    assert solution("{[]}[()]{}") == True
    assert solution("{[]}[()]{}") == True