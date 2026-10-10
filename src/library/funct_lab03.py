def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: text = text.casefold()
    else: text = text.lower()

    if yo2e: text = text.replace('ё','е')

    text = text.split()
    ans = ' '.join(text)
    return ans
# print("ПрИвЕт\nМИр\t", '->', normalize("ПрИвЕт\nМИр\t"))
# print("ёжик, Ёлка", '->', normalize("ёжик, Ёлка"))
# print("Hello\r\nWorld", '->', normalize("Hello\r\nWorld"))
# print("  двойные   пробелы  ", '->', normalize("  двойные   пробелы  "))

def tokenize(text: str) -> list[str]:
    import re
    znaki = r'\w+(?:-\w+)*'
    ans = re.findall(znaki, text)
    return ans
# print("привет мир", '->', tokenize("привет мир"))
# print("hello,world!!!", '->', tokenize("hello,world!!!"))
# print("по-настоящему круто", '->', tokenize("по-настоящему круто"))
# print("2025 год", '->', tokenize("2025 год"))
# print("emoji 😀 не слово", '->', tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    d = {}
    for i in tokens: d[i] = d.get(i,0) +1
    return d


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # freq = count_freq(freq)
    # for i in range(len(freq)):
    #     if freq.get(i) == freq.get(i+1):
    #         return sorted(freq.items())
    #     else: 
    #         return len(freq)              #уничтожить, функцию реализовал ужасно
    items = freq.items()
    ans = sorted(items, key = lambda p: (-p[1], p[0]))
    return ans[:n]
# print(["a","b","a","c","b","a"], '->', count_freq(["a","b","a","c","b","a"]))
# print(["a","b","a","c","b","a"], '->', top_n(count_freq(["a","b","a","c","b","a"])))
# print(["bb","aa","bb","aa","cc"], '->', count_freq(["bb","aa","bb","aa","cc"]))
# print(["bb","aa","bb","aa","cc"], '->', top_n(count_freq(["bb","aa","bb","aa","cc"])))