
class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
            return None
            
        self.r = []
        self.inorder(root)
        
        head = node = DoublyListNode(self.r[0])
        for i in range(1, len(self.r)):
            node.next = DoublyListNode(self.r[i])
            node.next.prev = node
            node = node.next
            
        return head    
        
        
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.r.append(root.val)
        self.inorder(root.right)
        
    def inorder_with_last(self, root, p_last_node):
        if not root:
            return
        
        self.inorder_with_last(root.left, p_last_node)
        
        root.left = p_last_node
        if p_last_node:
            p_last_node.right = root
            
        p_last_node = root
        self.inorder_with_last(root.left, p_last_node)
        
    def convert(self, root):
        p_last_node = None
        self.inorder_with_last(eoor, p_last_node)
        
        while p_last_node and p_last_node.left:
            p_last_node = p_last_node.left
            
        return p_last_node.left
