# Returns the stack of boxes with the tallest height possible where
# the height is the sum of the heights, h(i), of each box.  The boxes
# cannot be rotated and a box can only be stacked on top of another
# that is larger than or equal to it in terms of width, height, and
# depth 
#
#Input: [[w(1), h(1), d(1)], [w(2), h(2), d(2)], ... , [w(i), h(i),
# d(i)]]

def stack_boxes(boxes):
    if boxes is None or len(boxes) == 0:
        return []

    boxes = sorted(boxes, key = lambda x : (x[0], x[1], x[2]), reverse = True)

    memos = []

    for box in boxes:
        cur_height = box[1]

        # Stack: Bottom ==> Top
        cur_stack = [box]

        if len(memos) > 0:
            for memo in memos:
                
                # If the box can be placed on the stack
                if memo[1][-1][1] >= box[1] and memo[1][-1][2] >= box[2]:
                    new_height = memo[0] + box[1]
                
                    # If placing the box on the stack at memo
                    # increases the stack height
                    if new_height > cur_height:
                        cur_height = new_height
                        cur_stack = memo[1] + [box]
        memos.append((cur_height, cur_stack))

    return max(memos)[1]


if __name__ == "__main__":
    
    boxes = [[2, 2, 2], [5, 5, 5], [4, 4, 4]]
    assert stack_boxes(boxes) == [[5, 5, 5], [4, 4, 4], [2, 2, 2]]

    assert stack_boxes([[5, 5, 5], [3, 2, 3], [2, 3, 4]]) == [[5, 5, 5], [2, 3, 4]]

    assert stack_boxes([[3, 5, 4], [3, 6, 3], [5, 7, 3], [4, 8, 4]]) == [[4, 8, 4], [3, 6, 3]]

    assert stack_boxes([]) == []

    assert stack_boxes([[1, 2, 100], [10, 20, 100], [5, 10, 200], [1, 1, 300]]) == [[10, 20, 100], [1, 2, 100]]
