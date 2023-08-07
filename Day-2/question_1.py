def unique_sorted_words(input_str):
    words = input_str.split(',')
    unique_words = sorted(set(words))
    return unique_words

def unique_sorted_words_method3(input_str):
    words = input_str.split(',')
    unique_words = sorted(set(word for word in words))
    return unique_words



user_input = input("Enter a comma-separated sequence of words: ")
result = unique_sorted_words(user_input)
res=unique_sorted_words_method3(user_input)

print("Unique words in sorted order:", ", ".join(result))
print(",".join(res))
