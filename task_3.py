from typing import Dict, Union, List


def upper_case(func):
    def process_dict(d: dict) -> dict:
        new_dict = {}
        old_dict = d.copy()
        for key, value in d.items():

            new_key = key.upper() if isinstance(key, str) else key
            new_value = value.upper() if isinstance(value, str) else value

            new_dict[new_key] = new_value

            if isinstance(value, dict):
                new_dict.update(process_dict(value))
            elif isinstance(value, list):
                new_dict[new_key] = [process_dict(item) if isinstance(item, dict) else item for item in value]
                old_dict[new_key] = new_value
            old_dict[new_key] = new_value
        d.update(new_dict)
        return old_dict

    def wrapper(*args, **kwargs):
        result_dict = func(*args, **kwargs)
        merged_dict = process_dict(result_dict)
        return merged_dict

    return wrapper


@upper_case
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}


print(f1())


@upper_case
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}


print(f2())


@upper_case
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}


print(f3())


@upper_case
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}


print(f4())
