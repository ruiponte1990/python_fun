import sys


class Bracket_Tree:
    def __init__(self, List):
        self.root = Bracket_Node(List)
    def isValid(self):
        return self.root.isValid()

class Bracket_Node:
    def __init__(self, List, parent=None, open_="", close_="", children=None):
        self.open = open_
        self.close = close_
        self.children = [] if not children else children
        self.parent = parent
        self.add(List)

    def print_node(self):
        print("open: {0} close: {1}".format(self.open,self.close))
        print("Number of children: {0}".format(len(self.children)))

    def add(self, List):
        if len(List) > 0:
            one = List.pop(0)
            if one == "(": 
                self.open = one
                two = List.pop(0)
                if two == ")":
                    self.close = two
                    if self.parent:
                        self.parent.add(List)
                else:
                    new_node = Bracket_Node([two] + List, self)
                    self.children.append(new_node)
            elif one == "{": 
                self.open = one
                two = List.pop(0)
                if two == "}":
                    self.close = two
                    if self.parent:
                        self.parent.add(List) 
                else:
                    print("creating new node")
                    new_node = Bracket_Node([two] + List, self)
                    self.children.append(new_node)
                    print(self.children)
            elif one == "[": 
                self.open = one
                two = List.pop(0)
                if two == "]":
                    self.close = two
                    if self.parent:
                        self.parent.add(List)
                else:
                    print("creating new node")
                    new_node = Bracket_Node([two] + List, self)
                    self.children.append(new_node)
                    print(self.children)
            else:
                self.close = one
                if self.parent:
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
