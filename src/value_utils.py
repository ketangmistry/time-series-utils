import json

def get_value_arrays_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    def find_value_arrays(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'value' and isinstance(value, list):
                    yield value
                else:
                    yield from find_value_arrays(value)
        elif isinstance(obj, list):
            for item in obj:
                yield from find_value_arrays(item)
    
    return list(find_value_arrays(data))

# Example usage
# value_arrays = get_value_arrays_from_json('/path/to/your/json/file.json')
# print(value_arrays)