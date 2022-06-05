---
author: ''
category: Python
date: '2022-05-06'
summary: ''
title: Linked Lists
---

## linked lists

I have never been good at linked lists and even more broader - pointer logic. In this post I want to show a practical example of a linked list implementation in python and how to use it.

The main advantage of a linked list is that it does not need to be stored in a continuous block in memory and can live in a random place. The disadvantage is we can't just access a node - the list has to be traversed.

### The Python Implementation

This Singly linked list implementation was taken from [hackerrank](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists):

    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def insert_node(self, node_data):
            node = SinglyLinkedListNode(node_data)

            if not self.head:
                self.head = node
            else:
                self.tail.next = node

            self.tail = node

To use it:

    my_linked_list = SinglyLinkedList()
    my_linked_list.insert_node(1)
    my_linked_list.insert_node(2)
    my_linked_list.insert_node(3)

### Moving it Around

Instead of passing the linked list around. Sometimes it is preferable to just send a single node (really? when is that preferable and why? - recursion?)

That is all the current function needs to know as the node has the reference to the `next` and the function can iterate from the current node till the tail of the linked list.

### Printing a linked list

To print a linked list you can use a while loop or recursion.

The recursion example:

    def print_linked_list(head):
        '''
        Print a singly linked list
        '''
        print(head.data)
        if head.next:
            print_linked_list(head.next)

> what happens is you print the current nodes data attribute then if the current node has a next node - run the function to print the linked list with that node.

The while example:

    def print_linked_list_while(head):
        '''
        Print a single linked list in a while loop
        '''
        while(head):
            print(head.data)
            head = head.next

The timing were inconclusive:

* `while` loop: 10000 times - 0.702690217, 50000 times - 8.423126091
* `recursion`: 10000 times - 0.388262048, 50000 times - 7.361549832

### Inserting a node at the Tail

My successful attempt (but probably not optimal):

    def insertNodeAtTail(head, data):
        initial_node = head
        node = SinglyLinkedListNode(data)
        if head is None:
            return node
        # Get the the end
        while (head.next is not None):
            head = head.next
        # Set the next node as the new tail node
        head.next = node
        return initial_node

## Inserting a node at the head

    def insertNodeAtHead(llist, data):
        node = SinglyLinkedListNode(data)
        node.next = llist
        return node

## Inserting a node within a linkedlist

> Whenever dealing with positions not at the start or the end - a temporary node is needed to do changes and switches

    def insertNodeAtPosition(llist, data, position):
        head = llist
        new_node = SinglyLinkedListNode(data)
        if llist is None:
            return new_node
        else:
            # index position form 0
            position = position - 1
            while (position > 0 and llist.next is not None):
                llist = llist.next
                position -= 1
            temp = llist.next
            llist.next = new_node
            new_node.next = temp
        return head

## Deleting a Node

> When deleting a node a reference will always be needed to the prior node as the prior nodes `next` attribute will (the case of the first and last node are handled with if statements)

    def deleteNode(llist, position):
        if position == 0:
            return llist.next
        head = llist
        prior_node = llist
        
        position -= 1
        while (position > 0):
            prior_node = prior_node.next
            position -= 1
        
        current_node = prior_node.next
        if current_node.next is not None:
            next_node = current_node.next
        else:
            next_node = None
        
        prior_node.next = next_node
        return head

## Print in Reverse

> Since the linked list can only be processed in a single direction - we could read the entire list until `node.next == None` then print it and set the prior nodes next to `None`

I went with using a list:

    def reversePrint(llist):
        items = []
        while (llist):
            items.append(llist.data)
            llist=llist.next
        for item in items[::-1]:
            print(item)

## Reverse a Linked List

> Reversing a linked list - at the core is changing the next to point to the prior node - instead of the next one - for all nodes along the chain. We can process it one way - swapping the next references all the way until the end returning the head. Whenever making changes in teh middle - we require a temporary node and have references to 3 nodes at a time

    def reverse(llist):
        prior_node = None
        current_node = llist
        next_node = llist.next
        
        while(current_node):
            temp = current_node.next 
            current_node.next = prior_node
            prior_node = current_node
            current_node = temp
        
        # at this point the prior_node is the head of the list
        return prior_node

## Comparing 2 Linked Lists

    def compare_lists(llist1, llist2):
        while(llist1.data == llist2.data):
            llist1 = llist1.next
            llist2 = llist2.next
            if not llist1 and not llist2:
                return 1
            elif not llist1 or not llist2:
                return 0
        return 0

## Delete Even numbers in a linked list

    def delete_even_nodes(head):
        '''
        Remove nodes that are even
        '''
        odd_head = head
        while (head.data % 2 == 0):
            head = head.next
        
        odd_head = head
        current_node = odd_head.next
        prior_node = odd_head
        while (current_node):
            next_node= current_node.next
            if current_node.data % 2 == 0:
                # skip it
                prior_node.next = next_node
            else:
                # otherwise ensure current node is maintained
                prior_node = current_node
            current_node = next_node
            
        return odd_head


## Sources

* [Python linked list implementation](https://www.studytonight.com/code/python/ds/singly-linked-list-in-python.php)