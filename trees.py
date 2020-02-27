""" Trees
        hierarchical ADTs witha root at the top. Trees have children which relationships between each other such as descendants, ancestors, siblings or a leaf(which is atree with no descendants. )


"""
class Tree:

    #-----------------------------------Nested Position class ------------------------------------

    class Position:

        def element(self):
            # return element stored at this position
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            # return true if other position reps same position
            raise NotImplementedError('must be implemeted in subclass')
        def __ne__(self, other):
            # return true if other does not rep same location
            return not(self == other)
    
    #-----------------Abstract methods that concrete sub-class must support --------------------

    def root(self):
        # return positon repping trees root
        raise NotImplementedError('must be implemented by subclass')
    def parent(self, p):
        # position repping p's parent
        raise NotImplementedError('must be implemented in subclasss')
    def num_children(self, p):
        # number of children p has
        raise NotImplementedError('must be implemented in subclass')
    def children(self, p):
        # iteration of positions repping p's children
        raise NotImplementedError('must be implemented in subclass')
    def __len__(self):
        # total number of elements in tree
        raise NotImplementedError('must be implemented in subclass')
    def __iter__(self):
        # iteration of the trees elements
        for p in self.positions():
            yield p.element()
    
    """ Preorder Traversal """

    def preorder(self):
        # generate a preorder iteration of positions in the tree
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    def _subtree_preorder(self, p):
        # Generate a preorder iteration of positions in subtree rooted at p
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
    def positions(self):
        # generate iterations of the tree positions
        return self.preorder()
    
    """ Postorder traversal """

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    def _subtree_postorder(self):
        # generate a postorder iteration of positions in subtree rooted at p
        for c in self.chilren(p):
            for other in self._subtree_postorder(c):
                yield other
            yield p
    
    """ Breadfirst Traversal """
    
    def breadthfirst(self):
        # generate a breadth-first iteration of the positions of tree
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
    
    """ Inorder traversal """

    def inorder(self):
        # inorder iteration of positions in tree
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self, p):
        # iteration of positions in subtree rooted at p.
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # ---------------------------Concrete methods implemented in class --------------------------

    def is_root(self, p):
        # return true if p reps root of tree
        return self.root() == p
    def is_leaf(self, p):
        # return true if p has no children
        return self.num_children(p) == 0
    def is_empty(self):
        returnlen(self) == 0
    
    # Depth
    """ Number of ancestors of p excluding p itself """

    def depth(self, p):
        # number of levels separating p from root
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))


    # Height
    """ The height of a non empty tree is equal to the max of depths of its leaf positions """

    def _height1(self):
        # return height of tree
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        # return height of subtree rooted at Position p
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    """ Public method that computes the height of a subtree rooted at a given position or the entire tree if p is not specified"""

    def height(self, p=None):
        # return height of subtree rooted at position p
        if p is None:
            p = self.root()
        return self._height2(p)




"""
Binary Trees
    An ordered tree with 2 children at most(left child and right child). A left child precedes a right child.
"""


class  BinaryTree(Tree):
    # Abstract class repping a binary tree structure

    #--------------------additional abstract methods ---------------------
    
    def left(self, p):
        # return a position repping p's left child
        raise NotImplementedError("must be implemented by subclass")
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    #--------------------------concrete methods implemented in this class ------------------------------
    
    def sibling(self, p):
        # return position p repping p's sibling
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.roght(parent)
            else:
                return self.left(parent)
    def children(self, p):
        # iteration of positions repping p's children
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # override inherited version to make inorder the default
    def positions(self):
        # iteration of the tree positions
        return self.inorder()



""" Linked Binary Tree
        Linked representation of binary tree

"""

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        # An abstraction repping the location of a single element

        def __init__(self, container, node):
            # Constructor should not invoked by user
            self._container = container
            self._node = node
        def element(self):
            # return element stored at this position
            return self._node._element
        def __eq__(self, other):
            # return true if other is a Position repping the same location
            return type(other) is type(self) and other._node is self._node
        def validate(self, p):
            # return associated node if Position is valid
            if not isinstance(p, self.Position):
                raise TypeError("p must be proper position type.")
            if p._container is not self:
                raise ValueError("p does not belong to this container.")
            if p._node._parent is p._node:
                raise ValueError("p is no longer valid!")
            return p._node
        def _make_position(self, node):
            # return position instance for a given node
            return self.Position(self, node) if node is not None else None

        #-----------------binary tree ----------------------
        def __init__(self):
            self._root = None
            self._size = 0

        #----------------public accessor  ------------------
        def __len__(self):
            # total number of elements in tree
            return self._size
        def root(self):
            # root postion of tree
            return self._make_position(self._root)
        def parent(self, p):
            # position of p's parent
            node = self._validate(p)
            return self._make_position(node._parent)
        def left(self, p):
            # position of p's left child (None if no left child)
            node = self._validate(p)
            return self._make_position(node._left)
        def right(self, p):
            node = self._validate(p)
            return self._make_position(node._right)
        def num_children(self, p):
            # number of children of position p
            node = self._validate(p)
            count = 0
            if node._left is not None:
                count += 1
            if node._right is not None:
                count += 1
            return count
        def _add_root(self, e):
            """ 
            place element at root of Tree and return new position
            raise ValueError if p is nonempty
            """
            if self._root is not None:
                raise ValueError("Root exists")
            self._size = 1
            self._root = self._Node(e)
            return self._make_position(self._root)
        def _add_left(self, p, e):
            """
                Create new child for Position p, storing element e
                Return the position of the new node
                Raise Value Error if Position p is invalid or already has right child
            """
            node = self._validate(p)
            if node._left is not None:
                raise ValueError("Left child exists")
            self._size += 1
            node._left = self._Node(e, Node)
            return self._make_position(node._left)
        def _add_right(self, p, e):
            node = self._validate(p)
            if node._right is not None:
                raise ValueError("Right child exists")
            self._size += 1
            node._right = self._Node(e, Node)
            return self._make_positon(node._right)
        def _replace(self, p, e):
            # replace element at position p with e and return old element
            node = self._validate(p)
            old = node._element
            node._element = e
            return old
        def delete(self, p):
            """ Delete element at position p and replace it with its child
                Return the element that had been stored at Position P
            Raise ValueError if position p is invalid or has 2 children
            """
            node = self._validate(p)
            if self.num_children(p) == 2:
                raise ValueError('p has two children')
            child = node._left if node._left else node._right
            if child is not None:
                child._parent = node._parent
            if node is self._root:
                self._root = child
            else:
                parent = node._parent
                if node is parent._left:
                    parent._left = child
                else:
                    parent._right = child
            self._size -= 1
            node._parent = node
            return node._element
        def _attach(self, p, t1, t2):
            # Attach trees t1 and t2 as left and right subtrees of external tree p
            node = self._validate(p)
            if not self.is_leaf(p):
                raise ValueError("position must be leaf.")
            if not type(self) is type(t1) is type(t2):
                raise TypeError("Tree types must match.")
            self._size += len(t1) + len(t2)
            if not t1.id_empty():
                t1._root._parent = node
                node._left = t1._root
                t1.root = None
                t1._size = 0
            if not t2.is_empty():
                t2._root._parent = node
                node._right = t2._root
                t2.root = None
                t2.size = 0