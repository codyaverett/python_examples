#!/bin/python3

import math
import os
import random
import re
from sre_compile import isstring
import sys

Coordinates = tuple[int, int, int]

# crop coordinates
crop_ref = {0: 'corn', 1: 'soy', 2: 'wheat'}
crops = [(251, 236, 94), (13, 138, 4), (245, 222, 180)]


def get_euclidean_distance(coords1: Coordinates, coords2: Coordinates):

    # convert coords1 to a Coordinate type if it isn't already
    if not isinstance(coords1, tuple) and isstring(coords1):
        # create a tuple from a string
        coords1 = tuple(map(int, coords1.split(',')))

    # err ValueError: too many values to unpack (expected 3)
    (x1, y1, z1) = coords1
    (x2, y2, z2) = coords2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)


# find closest crop to each pixel
def find_closest_match(coords: Coordinates, crops: list[Coordinates]) -> Coordinates:
    min_distance = math.inf
    closest_match = None
    for crop in crops:
        distance = get_euclidean_distance(coords, crop)
        if distance < min_distance:
            min_distance = distance
            closest_match = crop
    return closest_match


def count_crops(image_data: list[list[float]]) -> list[float]:

    # defined above: crop_ref = { 0: 'corn', 1: 'soy', 2: 'wheat' }
    crop_counts = [0.0, 0.0, 0.0]

    for row in image_data:
        for pixel in row:
            crop = find_closest_match(pixel, crops)
            # todo: add branching logic for half matches
            crop_counts[crops.index(crop)] += 1
    return crop_counts


if __name__ == '__main__':
    # from ast import literal_eval
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # image_data = literal_eval(input().strip())
    # BAD DATA look like this: [['(248, 229, 137)', '(9, 144, 0)'], ['(254, 226, 84)', '(255, 221, 185)']]
    image_data = [[(248, 229, 137), (9, 144, 0)], [
        (254, 226, 84), (255, 221, 185)]]

    result = count_crops(image_data)

    print(list(zip(crop_ref, result)))

    # fptr.write(str(result) + '\n')

    # fptr.close()
