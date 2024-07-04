
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.sum = 0
        self.status = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            if self.status == 0 and value < self.root.data:
                self.status = 1
            elif self.status == 1 and value > self.root.data:
                self.status = 0
            
            current = self.root
            prev = None
            while current is not None and current.data < value:
                prev = current
                current = current.next
            
            if prev is None:
                new_node.next = self.root
                self.root = new_node
            else:
                new_node.next = current
                prev.next = new_node
                
        self.sum += value

    def remove(self, value):
        if self.root is None:
            return

        current = self.root
        prev = None

        while current is not None and current.data != value:
            prev = current
            current = current.next

        if current is None:
            return

        if prev is None:
            self.root = self.root.next
        else:
            prev.next = current.next

        self.sum -= value

    def concatenate(self, other_list):
        if other_list.root is None:
            return
        
        current = other_list.root
        while current is not None:
            self.insert(current.data)
            current = current.next

    def print_list(self):
        current = self.root
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

class StackOfLists:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, id):
        for item in self.stack:
            if item['id'] == id:
                print("This ID already exists, hence concatenating lists.")
                list_id = item['id']
                self.insert_list(list_id)
                return

        new_list = {'id': id, 'list': LinkedList()}
        print("Enter your desired elements for the list (Enter -1 to stop): ", end="")
        value = int(input())
        while value != -1:
            new_list['list'].insert(value)
            print("Enter your next desired element: ", end="")
            value = int(input())
        
        print("Press 0 for ascending and 1 for descending ", end="")
        choice = int(input())
        if choice == 1:
            new_list['list'].status = 1
        else:
            new_list['list'].status = 0
        
        self.stack.append(new_list)
        print(f"List with the ID {id} is being pushed to stack.")

    def pop(self):
        if self.is_empty():
            print("Unfotunately the stack is empty, hence cannot pop.")
            return

        print(f"Popping list with ID {self.stack[-1]['id']}")
        del self.stack[-1]

    def insert_list(self, id):
        if self.is_empty():
            print("Unfortunately stack is empty, cannot insert list.")
            return

        index = None
        for i, item in enumerate(self.stack):
            if item['id'] == id:
                index = i
                break
        
        if index is None:
            print("This desired ID does not exist in the stack.")
            return

        print(f"Enter elements for list with ID {id} (Enter -1 to stop): ", end="")
        value = int(input())
        while value != -1:
            self.stack[index]['list'].insert(value)
            print("Enter next element: ", end="")
            value = int(input())
        
        print("Press 0 for ascending and 1 for descending ", end="")
        choice = int(input())
        if choice == 1:
            self.stack[index]['list'].status = 1
        else:
            self.stack[index]['list'].status = 0
        
        print(f"List with ID {id} updated.")

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        for item in self.stack:
            print(f"Id = {item['id']}")
            print(f"Sum = {item['list'].sum}")
            print(f"Status = {'1' if item['list'].status == 1 else '0'}")
            print("Data:")
            item['list'].print_list()

    def menu(self):
        while True:
            print("\n1. Push a desired list to stack")
            print("2. Pop a list from stack")
            print("3. Insert elements into the desired list")
            print("4. Print the stack")
            print("5. Exit")
            choice = int(input("Enter the number of your desired function: "))

            if choice == 1:
                id = int(input("Enter ID for the desired list: "))
                self.push(id)
            elif choice == 2:
                self.pop()
            elif choice == 3:
                id = int(input("Enter ID of the desired list to insert elements: "))
                self.insert_list(id)
            elif choice == 4:
                self.print_stack()
            elif choice == 5:
                print("Exiting")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    stack = StackOfLists()
    stack.menu()


##class TreeNode:
##    def __init__(self, value):
##        self.value = value
##        self.left = None
##        self.right = None
##
##class ExpressionTree:
##    def __init__(self):
##        self.root = None
##
##    def construct_tree(self, postfix):
##        stack = []
##        operators = set(['+', '-', '*', '/'])
##        
##        for token in postfix.split():
##            if token not in operators:
##                node = TreeNode(token)
##                stack.append(node)
##            else:
##                node = TreeNode(token)
##                node.right = stack.pop()
##                node.left = stack.pop()
##                stack.append(node)
##        
##        self.root = stack.pop()
##
##    def infix_expression(self, node):
##        if node:
##            if node.left or node.right:
##                return "(" + self.infix_expression(node.left) + node.value + self.infix_expression(node.right) + ")"
##            else:
##                return node.value
##
##    def prefix_expression(self, node):
##        if node:
##            return node.value + " " + self.prefix_expression(node.left) + self.prefix_expression(node.right)
##
##    def evaluate_tree(self, node):
##        if node:
##            if node.value.isdigit():
##                return float(node.value)
##            else:
##                left_val = self.evaluate_tree(node.left)
##                right_val = self.evaluate_tree(node.right)
##
##                if node.value == '+':
##                    return left_val + right_val
##                elif node.value == '-':
##                    return left_val - right_val
##                elif node.value == '*':
##                    return left_val * right_val
##                elif node.value == '/':
##                    if right_val == 0:
##                        raise ZeroDivisionError("Division by zero")
##                    return left_val / right_val
##
##    def evaluate_expression(self, postfix):
##        self.construct_tree(postfix)
##        result = self.evaluate_tree(self.root)
##        # Round the result to the nearest integer if it's a whole number
##        if result.is_integer():
##            return int(result)
##        else:
##            return result
##
### Test cases
##def test_expression_evaluation():
##    expression_tree = ExpressionTree()
##
##    postfix_expressions = [
##        ("3 4 + 2 *", 14),  # (3 + 4) * 2 = 14
##        ("5 2 * 4 + 7 /", 10),  # (5 * 2) + (4 / 7) = 10
##        ("8 2 / 3 *", 12)  # (8 / 2) * 3 = 12
##    ]
##
##    for postfix, expected_result in postfix_expressions:
##        result = expression_tree.evaluate_expression(postfix)
##        assert result == expected_result, f"Expected: {expected_result}, Got: {result}"
##    print("All test cases passed.")
##
##if __name__ == "__main__":
##    test_expression_evaluation()
##'''
