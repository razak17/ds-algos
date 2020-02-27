from trees import LinkedBinaryTree
from maps import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    # sorted map imple using a binary search tree

    #------------------------------ override Position class -------------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            # return key of maps (k, v) pair
            return self._element()._key
        
        def value(self):
            return self._element()._value

    #------------------------------ nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        # Return position of p's substring having key k, or last node searched
        if k == p.key():
            return p
        elif k < p.key():
            if self._left(p) is not None:
                return self._subtree_search(self.left(p), k)
            else:
                if self._right(p) is not None:
                    return self._subtree_search(self._right(p), k)
            return p
    
    def _subtree_first_position(self, p):
        # Return position of first item in subtree rooted at p
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        # Return Position of last item in subtree rooted at p

        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        # First position in tree
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        # Last position in tree
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        # Position just before p in natural order
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk up
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def after(self, p):
        """ Position just after p in natural order
        symmetric to before(p)"""
        self.validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        # Position with key k, else neighbor
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            # Hook for balanced tree subclass
            self._s_access(p)
            return p
    
    def find_min(self):
        # Return (k, v) pair with minimum key
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        # (k, v) pair with least key >= k
        if self._empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
        
    def find_range(self, start, stop):
        """Iterate all (k,v) pairs such that start <= key < stop
        
        if start is None, iteration begins with min key of map.
        if stop is None, iteration continues through the max key"""
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)
    
    def __getitem__(self, k):
        # value associated with key k
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        # Assign value v to k 
        if self._empty():
            leaf = self._add_root(self._item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        # Iteration of all keys in map in order
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        # Remove itam at given position
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error ' + repr(k))

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        # Relink parent node with child node
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, parent):
        # Rotate position p above its parent
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            # x becomes root
            self._root = x
            x._parent = None
        else:
            # x becomes direct child of z
            self._relink(z,x,y == z._left)
            # now rotate x and y, including transfer of a middle subtree
            if x == y._left:
                self._relink(y, x._right, True)
                self._relink(x, y, False)
            else:
                self._relink(y, x._left, False)
                self._relink(x, y, True)

    def _restructure(self, x):
        # Perform trinode restructure of Pos x with parent/grandp
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


""" AVL Trees

"""

class AVLTreeMap(TreeMap):
    # Sorted Map implementaion of AVL tree

    #---------------------- nested _Node class -----------------------
    class _Node(TreeMap._Node):
        # maintains height value for rebalancing
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

        def _recompute_height(self, p):
            p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

        def _isbalanced(self, p):
            return abs(p._node.left_height() - p._node.right_height()) <= 1

        def _tall_child(self, p, favorleft=False):
            if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
                return self.left(p)
            else:
                return self.right(p)

        def _tall_grandchild(self, p):
            child = self._tall_child(p)
            alignment = (child == self.left(p))
            return self._tail_child(child, alignment)

        def _rebalance(self, p):
            while p is not None:
                old_height = p._node._height     # trivially 0 if new node
                if not self.isbalanced(p):       # imbalance detected
                    # perform trinode restructuring setting p as resulting root, compute new local heights after restructuring
                    p = self._restructure(self._tall_grandchild(p))
                    self._recompute_height(self.left(p))
                    self._recompute_height(self.right(p))
                self._recompute_height(p)
                if p._node._height == old_height:
                    p = None
                else:
                    p = self.parent(p)

        #---------------- overrride balancing hooks -----------------
        def _rebalance_insert(self, p):
            self._rebalance(p)

        def _rebalance_delete(self, p):
            self._rebalance(p)


"""Splay Trees

"""
class SplayTreeMap(TreeMap):
    #  Sorted map implementation of splay tree
    #---------------- splay operation ----------------------
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand - self.parent(parent)
            if grand is None:
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                self.rotate(parent)
                self.rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)
    
    #----------------------override balancing hooks ---------------
    def _rebalance(self, p):
        self._splay(p)
    
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)



""" Red Black Trees

"""

class RedBlackTree(TreeMap):
    # Sorted map implementation of a red-black tree
    class _Node(TreeMap._Node):
        # Node class for red-black tree maintains bit that denotes color
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True      # new node red by default

    #------------ positional-based utility methods -------------
    # we consider a non-existing child to be trivially black
    def _set_red(self, p): p._node._red = True

    def _set_black(self, p): p._node._red = False
    
    def _set_color(self, p, make_red): p._node._red = make_red

    def _is_red(self, p): return p is not None and p._node._red

    def _is_red_leaf(self, p): return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        # Return red child of p
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    #------------------ support for insertions --------------------
    def _rebalance_insert(self, p):
        self._resolve_red(p)        # New node is always red

    def _resolve_red(self, p):
        if self.is_root(p):
            self._set_black(p)      # make root black
        else:
            parent = self.parent(p)
            if self._is_red(parent):        # Double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):
                    middle = self._restructure(p)
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)

    #-------------------support for deletion --------------------
    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_black(self.root())    # ensure root is black
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
            elif n == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        # Rsolve black deficit at z, where y is root of z's heavier subtree
        if not self._is_red(y):
            x = self._get_red_child(y)
            if x is not None:
                # Case 1: y is black and has red child x
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                # Case 2: y is black, but no red children
                self._set_red(y)
                if self._is_red(y):
                    self._set_black(z)
                elif not sself.is_root(z):
                    self._fix_deficit(self.parent(z), self.sibling(z))
        else:
            # Case 3: y is red
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))