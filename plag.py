import re
from collections import Counter
from math import sqrt


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def preprocess_code(code):
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'\s+', ' ', code)
    return code.lower()


def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]


def cosine_similarity(code1, code2):
    words1 = code1.split()
    words2 = code2.split()

    freq_map1 = Counter(words1)
    freq_map2 = Counter(words2)

    dot_product = sum(freq_map1[word] * freq_map2.get(word, 0) for word in freq_map1)
    magnitude1 = sqrt(sum(freq**2 for freq in freq_map1.values()))
    magnitude2 = sqrt(sum(freq**2 for freq in freq_map2.values()))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


def is_code(text):
    semicolon_count = text.count(';')
    brace_count = text.count('{') + text.count('}')
    keywords = ['if', 'else', 'for', 'while', 'return', 'def', 'class', 'public', 'private', 'int', 'void']
    keyword_count = sum(text.count(keyword) for keyword in keywords)
    return (semicolon_count > 5) or (brace_count > 2) or (keyword_count > 3)


def choose_algorithm(code1, code2):
    if is_code(code1) and is_code(code2):
        return 'levenshtein'
    return 'cosine'


def check_files(file1, file2):
    code1 = preprocess_code(read_file(file1))
    code2 = preprocess_code(read_file(file2))

    algo = choose_algorithm(code1, code2)

    if algo == 'cosine':
        similarity = cosine_similarity(code1, code2)
        sim_percentage = round(similarity * 100, 2)
        print(f"Cosine Similarity between '{file1}' and '{file2}': {sim_percentage}%")
    else:
        distance = levenshtein_distance(code1, code2)
        max_length = max(len(code1), len(code2))
        similarity = 1 - distance / max_length
        sim_percentage = round(similarity * 100, 2)
        print(f"Levenshtein Similarity between '{file1}' and '{file2}': {sim_percentage}%")

    if sim_percentage >= 50:
        print("Plagiarism detected")
    else:
        print("No plagiarism detected")


def main():
    file1 = './Test/test1.txt'
    file2 = './Test/test2.txt'

    check_files(file1, file2)


if __name__ == "__main__":
    main()
