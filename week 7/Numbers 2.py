def create_indexed_dict(items: list) -> dict:
    return {i: items[i] for i in range(len(items))}