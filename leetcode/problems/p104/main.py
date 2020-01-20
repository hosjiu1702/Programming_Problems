class Solution:
    def maxDepth(self, root):
        LEFT = 0
        RIGHT = 1
        LEAF = 2
        NON_LEAF = 3

        stack = list()
        max_depth = 0
        d = 0
        stack.append(root)
        is_root = True
        prev_node = None
        while stack:
            node = stack.pop()
            temp_node = list()
            num_childs = 0

            if node.right:
                stack.append([node.right, RIGHT])
                num_childs += 1
            if node.left:
                stack.append([node.left, LEFT])
                num_childs += 1

            if is_root:
                d = d + 1
                is_root = False
            else:
                """ Leaf or Non-Leaf """
                temp_node.append(LEAF) if num_childs > 0 else temp_node.append(NON_LEAF)
                
                """ Number of its chlildrens """
                temp_node.append(num_childrens)
                
                """ Position """
                temp_node.append(node[1])
                

            if d > max_depth:
                max_depth = d

