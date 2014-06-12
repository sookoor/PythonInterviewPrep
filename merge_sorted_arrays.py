# Given two sorted arrays, A and B, with A having enough buffer at the end to hold B, merges B into A in sorted order.

def merge_sorted_arrays(A, B):
    cur_A = len(A) - len(B) - 1
    cur_B = len(B) - 1
    cur = len(A) - 1

    while cur_A >= 0 and cur_B >= 0:
        if A[cur_A] > B[cur_B]:
            A[cur] = A[cur_A]
            cur_A -= 1
        else:
            A[cur] = B[cur_B]
            cur_B -= 1
        cur -= 1

if __name__ == "__main__":
    A = [10, 15, 18, 20, 21, 23, 25, None, None, None, None, None, None]
    B = [9, 11, 12, 13, 15, 16]

    merge_sorted_arrays(A, B)
    print A
    
