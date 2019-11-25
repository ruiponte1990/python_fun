import sys

class Bracket_Tree:
    def __init__(self, List):
        self.root = root_node(List)
    def isValid(self):
        return self.root.isValid()


class root_node:
    def __init__(self, List, children=None):
        self.children = [] if not children else children
        self.add(List)

    def add(self, List):
        new_node = Bracket_Node(List, self)
        self.children.append(new_node)

    def isValid(self):
        for n in self.children:
            if not n.isValid():
                return False
        return True

class Bracket_Node:
    def __init__(self, List, parent=None, open_="", close_="", children=None):
        self.open = open_
        self.close = close_
        self.children = [] if not children else children
        self.parent = parent
        self.add(List)

    def add(self, List):
        if len(List) > 0:
            one = List.pop(0)
            if one == "(":
                if not self.open: 
                    self.open = one
                    if (len(List) > 0):
                        two = List.pop(0)
                        if two == ")":
                            self.close = two
                            if self.parent and (len(List) > 0):
                                self.parent.add(List)
                        else:
                            new_node = Bracket_Node([two] + List, self)
                            self.children.append(new_node)
                else:
                    new_node = Bracket_Node([one] + List, self)
                    self.children.append(new_node)
            elif one == "{": 
                if not self.open: 
                    self.open = one
                    if (len(List) > 0):
                        two = List.pop(0)
                        if two == "}":
                            self.close = two
                            if self.parent and (len(List) > 0):
                                self.parent.add(List) 
                        else:
                            new_node = Bracket_Node([two] + List, self)
                            self.children.append(new_node)
                else:
                    new_node = Bracket_Node([one] + List, self)
                    self.children.append(new_node)
            elif one == "[":
                if not self.open: 
                    self.open = one
                    if (len(List) > 0):
                        two = List.pop(0)
                        if two == "]":
                            self.close = two
                            if self.parent and (len(List) > 0):
                                self.parent.add(List)
                        else:
                            new_node = Bracket_Node([two] + List, self)
                            self.children.append(new_node)
                else:
                    new_node = Bracket_Node([one] + List, self)
                    self.children.append(new_node)
            else:
                self.close = one
                if self.parent and (len(List) > 0):
                        self.parent.add(List)

    def isValid(self):
        if self.open and self.close:
            if self.open == "(" and self.close == ")": 
                for child in self.children:
                    if not child.isValid():
                        return False
                return True
            elif self.open == "[" and self.close == "]": 
                for child in self.children:
                    if not child.isValid():
                        return False
                return True
            elif self.open == "{" and self.close == "}":
                for child in self.children:
                        if not child.isValid():
                            return False
                return True
            else:
                return False
        else:
            return False
        
                             
                                         
def solution(brackets):
    bracket_list = [char for char in brackets]
    tree = Bracket_Tree(bracket_list)
    return tree.isValid()

print(solution("[{}{}]"))
print(solution("[{}()]"))
print(solution("[{}[()]{}]"))
print(solution("[{}[()]{}{}[]()]"))