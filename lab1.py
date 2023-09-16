# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
from lab1_utils import TextbookStack


def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    # Create a queue with the initial stack and flip sequence as the first element.
    queue = deque([(stack, flip_sequence)])

    while queue:
        current_stack, current_flip_sequence = queue.popleft()  # Dequeue the first item from the queue.

        # Check if the current stack is already sorted.
        if current_stack.check_ordered():
            return current_flip_sequence  # If sorted, return the flip sequence.

        for i in range(1, stack.num_books + 1):
            new_stack = current_stack.copy()  # Create a copy of the current stack.
            new_stack.flip_stack(i)  # Apply a flip operation to the new stack.

            # Create a new flip sequence by appending the current flip sequence with the flip operation.
            new_flip_sequence = current_flip_sequence + [i]

            # Enqueue the new stack and its corresponding flip sequence for further exploration.
            queue.append((new_stack, new_flip_sequence))

    return flip_sequence
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    # Create a deque to manage the stack states and their corresponding flip sequences.
    node_deque = deque()

    # Initialize the selected stack as the input stack.
    selected_stack = stack

    # Initialize the current book number (to be flipped) as the last book in the stack.
    current_book_number = stack.num_books - 1

    # Append the initial stack and an empty flip sequence to the deque.
    node_deque.append([selected_stack, []])

    while node_deque:  # Continue the loop while there are nodes in the deque.
        selected_node = node_deque.popleft()  # Dequeue the first node from the deque.
        selected_stack = selected_node[0]  # Extract the stack from the selected node.

        for i in range(stack.num_books):  # Loop through all possible book positions (0-based index).
            temp_stack = selected_stack.copy()  # Create a copy of the current stack.

            temp_stack.flip_stack(i + 1)  # Flip the stack from the current book position.

            # Create a new node with the updated stack and append the flip operation to the flip sequence.
            node = [temp_stack, selected_node[1].copy() + [i + 1]]
            node_deque.append(node)

        if selected_stack.check_ordered():  # Check if the current stack is sorted.
            flip_sequence = selected_node[1]  # If sorted, assign the flip sequence to flip_sequence.
            break  # Exit the loop since sorting is achieved.

    return flip_sequence
    # ---------------------------- #


# test = TextbookStack(initial_order=[3, 2, 1, 0], initial_orientations=[0, 0, 0, 0])
# sequence1 = depth_first_search(test)
# sequence2 = breadth_first_search(test)
# print(sequence1, sequence2)
