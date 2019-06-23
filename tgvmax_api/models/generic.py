def from_dict(d, key_list):
    if type(key_list) == str:
        key_list = [key_list]
    d2 = dict(d)
    passed = ''
    for key in key_list:
        if key not in d2:
            raise ValueError(f'"{key}" not in the dict{passed}')
        d2 = d2[key]
        passed += f'[{key}]'
    return d2
