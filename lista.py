# Creamos la clase node
# este es un comentario



class node:
    def __init__(self, posx = None, posy = None, next = None):
        self.posx = posx
        self.posy = posy
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos de primero en la lista
    def add_at_first(self, posx,posy):
        new_nodo = node(posx=posx,posy=posy, next=self.head)
        self.head = new_nodo  

    # Método para verificar la existencia de elementos
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_to_the_end(self, posx,posy):
        if self.head is None:
            self.head = node(posx=posx,posy=posy)
            return
        temporal = self.head
        while temporal.next is not None:
            temporal = temporal.next
        temporal.next = node(posx=posx,posy=posy)
    
    # Método para eleminar de la lista
    def delete_node(self, posx,posy):
        temporal = self.head
        prev = None
        while temporal and temporal.posx !=posx and temporal.posy != posy:
            prev = temporal
            temporal = temporal.next
        if prev is None:
            self.head = temporal.next
        elif temporal:
            prev.next = temporal.next
            temporal.next = None
    def delete_first(self):
        if self.head is not None:
            temporal = self.head
            temporal = temporal.next
            self.head = temporal
    # Método para obtener el ultimo nodo de la lista
    def delete_last(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        temp.next= None
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para recorrer la edd
    def print_list( self ):
        node = self.head
        while node != None:
            print(str(node.posx)+" "+str(node.posy), end =" => ")
            node = node.next
        print("null")

