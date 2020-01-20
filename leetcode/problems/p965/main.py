class Solution:
    def isUnivalTree(self, root):
        """ Create stack"""
        s = list()

        s.append(root)
        init_val = root.val
        while len(s) > 0:
            curr_node = s.pop()
            if curr_node.val != init_val:
                return False

            if curr_node.right:
                s.append(curr_node.right)
            
            if curr_node.left:
                s.append(curr_node.left)
        
        return True
