from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage != self.capacity:               # IF THE CACHE IS NOT AT CAPACITY THEN DO THIS 
            self.current = self.current.add_to_tail    # ADD ITEM TO THE FRONT OF THE LIST (tail)
            self.capacity += 1                          # INCREASE THE COUNT
        if self.storage == self.capacity:               # IF THE CACHE IS AT CAPACITY 
            self.storage.delete.[self.current.value[0]] # DELETE FROM STORAGE (head)
            self.current.remove_from_head()             # REMOVE THE OLDEST ITEM FROM TAIL 
            self.current = self.current.add_to_tail     # ADD THE NEW ITEM TO THE Tail OF THE LIST 
            self.capacity += 1                          # INCREASE THE CAPACITY 

        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #yes
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
