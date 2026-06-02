# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # 1. Initialize the heap with the head node of each non-empty linked list
        # Tuple format: (node_value, unique_list_index, node_object)
        for i, head_node in enumerate(lists):
            if head_node:
                heapq.heappush(min_heap, (head_node.val, i, head_node))
        
        # 2. Create a dummy node to act as the anchor for our merged list
        dummy = ListNode(0)
        curr = dummy
        
        # 3. Pull the lowest node, link it, and replenish the heap
        while min_heap:
            val, i, smallest_node = heapq.heappop(min_heap)
            
            # Attach the smallest node to our growing merged chain
            curr.next = smallest_node
            curr = curr.next  # Advance our tail pointer
            
            # If the popped node has a successor node, push it into the heap
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))
                
        return dummy.next