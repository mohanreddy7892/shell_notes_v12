# some code
def all_unique_combinations(words, n):
    words = sorted(words)
    items = list(range(len(words)))
    old_combinations = [[]]
    new_combinations = []

    for i in range(n):
        new_combinations = []
        for combination in old_combinations:
            for item in items:
                if (combination and item > combination[-1]) or len(combination) == 0:
                    new_combinations.append(combination + [item])
                    #old_combinations = new_combinations
        word_combinations = []
        for combaination in new_combinations:
            inside_word = []
            for index in combaination:
                inside_word.append(words[index])
            word_combinations.append(tuple(inside_word))
            print(list(word_combinations))


words = input().split()
n = int(input())

all_combinations = all_unique_combinations(words, n)
for i in all_combinations:
    print("".join(i))
