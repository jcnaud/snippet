# coding: utf-8


from deepdiff import DeepDiff  # For Deep Difference of 2 objects

from deepdiff import DeepSearch  # For finding if item exists in an object

import logging

def main():
    t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
    t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 3]}}

    ddiff = DeepDiff(t1, t2, ignore_order=True)
    print(ddiff)
    # {}
    
    ddiff = DeepDiff(t1, t2, ignore_order=True, report_repetition=True)
    print(ddiff)
    # {'repetition_change': {"root[4]['b'][2]": {'new_indexes': [1, 3], 'value': 3, 'old_repeat': 1, 'new_repeat': 2, 'old_indexes': [2]}}}

    l1 = logging.getLogger("test")
    l2 = logging.getLogger("test2")
    t1 = {"log": l1, 2: 1337}
    t2 = {"log": l2, 2: 1337}
    print(DeepDiff(t1, t2, exclude_types={logging.Logger}))
    # {}

    t1 = {"for life": "vegan", "ingredients": ["no meat", "no eggs", "no dairy"]}
    t2 = {"for life": "vegan", "ingredients": ["veggies", "tofu", "soy sauce"]}
    print (DeepDiff(t1, t2, exclude_paths={"root['ingredients']"}))
    # {}


    t1 = {1:1, 3:3, 4:4}
    t2 = {1:1, 3:3, 5:5, 6:6}
    ddiff = DeepDiff(t1, t2)
    print(ddiff)
    # {'dictionary_item_added': {'root[5]', 'root[6]'},
    #  'dictionary_item_removed': {'root[4]'}}

    ## More exemple on https://github.com/seperman/deepdiff

if __name__ == "__main__":
    main()