#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    best_key = ""
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > best_score:
            best_score = v
            best_key = k
