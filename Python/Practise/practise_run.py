# Write function to take string as input and provide output with below condition: First letter of word always have to be capital If preceding letter occurs earlier in dictionary then letter has to be capital If preceding letter occurs later in dictionary then letter has to be small If preceding letter is same as current letter then no change in case. Example: applE is fruit => APple IS FRUiT A => 1st Letter(upper), 1st P => Preceding(A) occur earlier (upper), 2nd P => Preceding(P) same(no_change), L => Preceding(P) occurs later (small), e => Preceding(L) occurs later(small), I => 1st letter(upper) and so on. explain the question. explain in simplest way
def string_case_convertor():
    sentence = input("Enter the sentence: ")
    words = sentence.split()
    result = []

    for word in words:
        new_word = word[0].upper()  # first letter always uppercase

        for i in range(1, len(word)):
            prev = word[i - 1].lower()
            curr = word[i]

            if prev < curr.lower():
                new_word += curr.upper()
            elif prev > curr.lower():
                new_word += curr.lower()
            else:
                new_word += curr  # no change

        result.append(new_word)

    return " ".join(result)


print(string_case_convertor())
