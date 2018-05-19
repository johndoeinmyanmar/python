
# coding: utf-8

# # Linked lists

# In linked lists, the elements are linked together in a way that can be categorized into following ..
# - Singly linked lists
# - Circularly linked lists
# - Doubly linked lists
# - Positional lists

# ## Singly linked list

# A singly linked list, in its simplest form, is a collection of nodes that form linear sequence. Each node has a reference to the contained object and reference to the next node, but not the node before. The first node is called the head, and it don't have the pointer from the previous node, cuz it is the very first node. And the end node is called the tail and it points to None.

# In[ ]:


class _Node():
    """Light-weight, non-public class for storing singly linked node"""
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next


# Since singly linked list is the collection of nodes which comprise of elements and next pointer, each node supposes to be an object with both element and next. That is what the above class does. 

# In[2]:


class Empty(Exception):
    pass


# In[3]:


class LinkedStack:
    """LIFO stack implementation with the singly linked list for data storage,
    instead of python list"""
    #--------------------Nested Node class-----------------------
    class _Node:
        """Light-weight, non-public class for storing singly linked list"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    #-------------------Stack methods-------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the length of the stack"""
        return self._size
    
    def is_empty(self):
        """Return True if the size is zero"""
        return self._size == 0
    
    def push(self, e):
        """Add element e at the top of the stack"""
        self._head = self._Node(e,self._head)
        self._size += 1
    
    def top(self):
        """Return (but do not return ) the element at the top of the stack
        
        Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        """Return and remove the element from the top of the stack
        
        Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    


# Here is the use of the LinkedStack class

# In[4]:


# creating the instance of the LinkedStack() class
stack = LinkedStack()
# adding an element 'a' and 'b' to the top of the stack
stack.push('a')
stack.push('b')
# finding the len of the stack
len(stack)
# removing the first element from the stack
stack.pop()


# ### Implementing Queue with Singly linked list

# In[5]:


class LinkedQueue:
    """FIFO queue implementation using the singly linked list as storage"""
    
    class _Node:
        """light-weight, non-public class for linked node"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            """Create a node"""
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the length of the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return the first element from the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def dequeue(self):
        """Return and remove the first element of the queue(FIFO)
        raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        """Add an element e to the back of the queue"""
        newest = self._Node(e, self._head)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        


# In[6]:


queue = LinkedQueue()


# In[7]:


queue.enqueue('a')
queue.enqueue('b')


# In[8]:


queue.first()


# ## Circularly Linked List
# Just like the other types of linked list, circularly linked list also has nodes conntecting each other but in circularly linked list, tail node points its next reference to the head. So it seems like circular. And if you know the reference of the tail, you figure out where the head node will be.
# 
# Below is the circularly linked list implementation of the circular queue.

# In[9]:


class CircularQueue:
    """Circular Queue implementation using circular linked list as storage"""
    
    class _Node:
        """Light weight, non-public class for storing the node element"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty circular queue"""
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Return the size of the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the size of the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return the first element (head) of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        """Return and remove the first element of the queue (FIFO) 
           
           raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element
    
    def enqueue(self, e):
        """Add an element e between the head and tail node"""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest           # new node becomes the tail
        self._size += 1
        
    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next


# In[21]:


a = CircularQueue()


# In[22]:


for x in range(10):
    a.enqueue(x)


# In[23]:


len(a)


# In[24]:


a.dequeue()


# In[25]:


a.first()


# In[31]:


a.rotate()
a.first()


# ## Doubly Linked List
# In doubly linked list, each node has the reference to its previous and next node. 
# Another thing to note is that the whole node sequence is in between two empty nodes, header and trailer. By having that two nodes, we don't have to worry about the special case when the list is empty. In doubly linked list, insertion and deletion in O(1) worst case time.

# In[32]:


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""
    
    class _Node:
        """light-weight, non-public class for storing the each node"""
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            """Create an empty node"""
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        """Create a structure with two empty nodes, headers and tailer"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        """Return the size of the list"""
        return self._size
    
    def is_empty(self):
        """Return True if the list is empty"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Insert an element e between predecessor and successor"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinal node from the list and return the element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
        
        


# In[33]:


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on doubly linked list"""
    
    def first(self):
        """Return the first element(the next element of the header) in list"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._header._next._element
    
    def last(self):
        """Return the last element from the list"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Insert an element e between header and the first element"""
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        """Insert an element e between the trailer and the last node"""
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        """Remove and return the element  from the first of the deque"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the back of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._delete_node(self._trailer._prev)
    


# In[34]:


d = LinkedDeque()


# In[35]:


d.insert_first('a')
d.insert_last('b')


# In[36]:


d.first()


# In[37]:


d.last()


# In[38]:


d.delete_first()


# In[39]:


d.delete_last()


# In[40]:


len(d)

