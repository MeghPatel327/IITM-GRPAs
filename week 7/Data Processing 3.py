# Take the input from standard input using input()
# and print the output according to the problem .
# Write your code here

def longest_antakshari_subsequence(n, sequences):
    for seq in sequences:
        words = seq.split(",")
        max_length = 1
        current_length = 1

        for i in range(1, len(words)):
            if words[i-1][-1] == words[i][0]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        max_length = max(max_length, current_length)
        print(max_length)

n = int(input())
sequences = [input().strip() for _ in range(n)]

longest_antakshari_subsequence(n, sequences)