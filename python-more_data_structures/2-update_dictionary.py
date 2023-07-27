#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# Test the function using the provided main file
if __name__ == "__main__":
    def print_sorted_dictionary(my_dict):
        keys = sorted(my_dict.keys())
        for k in keys:
            print("{}: {}".format(k, my_dict[k]))