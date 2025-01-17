#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
        # print(hash_table_retrieve(ht, weights[i])

    for i in range(0, length):
        one = i
        two = hash_table_retrieve(ht, limit - weights[i])
        print(one)
        print(two)
        if one is not None and two is not None:
            return (two, one)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([4, 4], 2, 8)
