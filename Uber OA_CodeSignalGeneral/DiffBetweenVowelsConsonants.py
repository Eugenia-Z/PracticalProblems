# Kaiqi's Solution
# Idea: 
# 1. use a function to count difference, parameter being a word; 
# 2. then traverse the text, use a dic to map the word to the diff
# 3. for sorting use lambda function, passing the keys diff value as the first, word itself as the second 
# to deal with the situation that there is a tie.

def calculateDiff(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_of_vowels = 0
    num_of_connosants = 0
    for char in word:
        if char in vowels:
            num_of_vowels += 1
        else:
            num_of_connosants += 1
    return abs(num_of_vowels - num_of_connosants)

def solution1(text):
    list_of_words = text.split(" ")
    word_to_diff = {}
    for word in list_of_words:
        word_to_diff[word] = calculateDiff(word)
    
    word_to_diff_sorted = dict(sorted(word_to_diff.items(), key=lambda item: (item[1], item[0])))
    return word_to_diff_sorted.keys()



# GPT's Solution
# optimization: 
# 1. a neat way to calculate the absolute diff between vowels and consonants
# 2. instead of using a dict to map word and diff, compute the diff on the fly and pass into sort function immediately

def solution2(text):
    # Define vowels
    vowels = set('aeiou')
    
    def vowel_consonant_diff(word):
        vowel_conut = sum(1 for char in word if char in vowels)  # neat way of using list comprehension
        consonant_count = len(word) - vowel_conut
        return abs(vowel_conut - consonant_count)
    
    words = text.split()
    words.sort(key=lambda word:(vowel_consonant_diff(word),word))  # note the way of passing two keys to lambda, also compute diff on the go
    return words

if __name__ == "__main__":
    text = "penelope lives in hawaii"
    print(solution2(text))