def unique_vowels(s: str) -> set:
    out = []
    for ele in s:
        if ele in 'aeiou' or ele in 'AEIOU':
            out.append(ele)
    return set(out)