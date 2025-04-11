def most_occuring_first_letter(passage: str) -> str:
    first_letters = [word[0] for word in passage.split()]
    return max(first_letters, key=first_letters.count).lower()