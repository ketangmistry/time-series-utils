import pytest
import json
from src.value_utils import get_value_arrays_from_json

def test_get_value_arrays_from_json(tmp_path):
    # Create a temporary JSON file
    test_data = {
        "level1": {
            "value": [1, 2, 3],
            "level2": {
                "value": [4, 5, 6],
                "level3": {
                    "not_value": [7, 8, 9],
                    "value": [10, 11, 12]
                }
            }
        }
    }
    test_file = tmp_path / "test.json"
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    
    # Call the function and check the result
    result = get_value_arrays_from_json(test_file)
    expected = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
    assert result == expected

def test_get_value_arrays_from_grafana_json():
    # Load the existing JSON file
    with open('data/grafana_cloud_usage_metrics.json', 'r') as f:
        grafana_data = json.load(f)
    
    # Call the function and check the result
    result = get_value_arrays_from_json('data/grafana_cloud_usage_metrics.json')
    
    # Check that all values in the arrays are 1
    for array in result:
        assert all(value == 1 for value in array)

# Run the tests
if __name__ == "__main__":
    pytest.main()
