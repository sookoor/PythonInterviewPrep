import operator

def most_common_characters(input_string, N):
    count = {}
    for char in inputString:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    sorted_freq = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)

    for i in range(min(N, len(sorted_freq))):
        print sorted_freq[i][0]
        
def main():
    most_common_characters("aaaaaaaaaaaaaaaaaaakkkkkkkkkkkkkkkkkkkddddddddddddhhhhhhhhhbbbbbbbeeeewqqqer", 10)
    
if __name__ == "__main__":
    main()
