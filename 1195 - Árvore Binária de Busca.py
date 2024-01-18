class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_parent(root, value):
    if root is None:
        return None
    else:
        if value <= root.value:
            if root.left is None:
                return root
            else:
                return find_parent(root.left, value)
        else:
            if root.right is None:
                return root
            else:
                return find_parent(root.right, value)

def print_order(root, order_type):
    if root is not None:
        if order_type == 1:
            print(f" {root.value}", end="")
            print_order(root.left, order_type)
            print_order(root.right, order_type)
        elif order_type == 2:
            print_order(root.left, order_type)
            print(f" {root.value}", end="")
            print_order(root.right, order_type)
        elif order_type == 3:
            print_order(root.left, order_type)
            print_order(root.right, order_type)
            print(f" {root.value}", end="")

def print_tree_case(case_number, root):
    print(f"Case {case_number}:")

    print("Pre.:", end="")
    print_order(root, 1)
    print("\nIn..:", end="")
    print_order(root, 2)
    print("\nPost:", end="")
    print_order(root, 3)

    print("\n")

def main():
    num_cases = int(input())

    for case in range(1, num_cases + 1):
        root = None

        num_elements = int(input())
        elements = map(int, input().split())

        for node_value in elements:
            new_node = TreeNode(node_value)
            new_node.left = None
            new_node.right = None

            parent = find_parent(root, node_value)
            if parent is None:
                root = new_node
            else:
                if node_value <= parent.value:
                    parent.left = new_node
                else:
                    parent.right = new_node

        print_tree_case(case, root)

if __name__ == "__main__":
    main()
