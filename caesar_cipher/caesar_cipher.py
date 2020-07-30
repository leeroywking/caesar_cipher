def c_encrypt(input: str, key) -> str:
    input = input.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mapped_letters = {}
    for i in range(len(alphabet)):
        mapped_letters[alphabet[i]] = alphabet[(i + key) % 26]
    output = ""
    for lett in input:
        if lett not in alphabet:
            output += lett
        else:
            output += mapped_letters[lett]
    return output

def c_decrypt(input: str, key) -> str:
    return c_encrypt(input, -key)



def load_words():
    with open('./caesar_cipher/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def brute_force_c_decrypt(input: str) -> str:
    all_words = load_words()
    results = []
    for i in range(26):
        current_attempt = c_decrypt(input, i)
        success_words = 0
        total_words = 0
        for word in current_attempt.split(" "):
            if word in all_words:
                success_words += 1
            total_words += 1
        results.append({"ratio_correct": success_words/ total_words, "key": i})
    best_result = {"ratio_correct": 0}
    for result in results:
        if result["ratio_correct"] > best_result["ratio_correct"]:
            best_result = result
    return c_decrypt(input, best_result["key"])
        