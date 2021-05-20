'''Problem : BINARY TREE LEVEL ORDER TRAVERSAL '''

#CODE :


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            levelLen = len(queue)
            levelNodes =[]
            for i in range(levelLen):
                cur = queue.popleft()
                levelNodes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(levelNodes)
        return res
