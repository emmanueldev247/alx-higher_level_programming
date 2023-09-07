#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_in_module = dir(hidden_4)
    filtered_names = [name for name in names_in_module if not name.startswith("__")]

    for name in filtered_names:
        print(name)
