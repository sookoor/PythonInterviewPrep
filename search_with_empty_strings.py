# Given a sorted array of strings which is interspersed with empty
# strings, finds the location of a given string.

def _search_with_empty_strings(query, string_array, lower, upper):
    if upper < lower:
        return -1

    mid = lower + ((upper - lower) // 2)
    mid_val = string_array[mid]

    if mid_val != "":
        if mid_val == query:
            return mid
        elif mid_val < query:
            lower = mid + 1
        else:
            upper = mid
            
        return _search_with_empty_strings(query, string_array, lower, upper)
    else:
        sign = [-1, 1]
        cur_sign = 1
        offset = 0
        
        cur = mid
        cur_mid = None
        while mid_val == "" and cur >= lower and cur <= upper:
            cur_sign = (cur_sign + 1) % 2
            if cur_sign == 0:
                offset += 1
                
            cur = mid + (sign[cur_sign] * offset)
            mid_val = string_array[cur]

        if cur < lower or cur > upper:
            return -1
        elif mid_val == query:
            return cur
        elif mid_val < query:
            
            # If on left of mid, skip over all empty strings
            if cur_sign == 0:
                lower = cur + (2 * offset)
            else:
                lower = cur + 1
        else:
            
            # If on right of mid, skip over all empty strings
            if cur_sign == 1:
                upper = cur - ((2 * offset) + 1)
            else:
                upper = cur
        return _search_with_empty_strings(query, string_array, lower, upper)

def search_with_empty_strings(query, string_array):
    if query is not None and type(query) is str and string_array is not None and len(string_array) > 0:
        return _search_with_empty_strings(query, string_array, 0, len(string_array) - 1)
    else:
        return -1

if __name__ == "__main__":
    string_array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    assert search_with_empty_strings("ball", string_array) == 4
    assert search_with_empty_strings("ballcar", string_array) == -1
