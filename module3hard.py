def calculate_structure_sum(data):
    def recursive_sum(item):
        total = 0
        if isinstance(item, (list, tuple, set)):
            for sub_item in item:
                total += recursive_sum(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                total += recursive_sum(key)
                total += recursive_sum(value)
        elif isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total += len(item)
        return total

    return recursive_sum(data)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)