import random

SCREEN_SIZE = 800


def get_random_coordinates():
    minimum = int(SCREEN_SIZE / 2 * -1 + 100)
    maximum = int(SCREEN_SIZE / 2 - 100)
    x = random.randint(minimum, maximum)
    y = random.randint(minimum, maximum)
    coords = (x, y)
    return coords


def get_random_heading():
    headings = [0, 90, 180, 270]
    return random.choice(headings)


def modify_coordinates(coords, heading):
    x = coords[0]
    y = coords[1]

    if heading == 90:
        y -= 20
    elif heading == 270:
        y += 20
    elif heading == 0:
        x -= 20
    elif heading == 180:
        x += 20

    new_coords = (x, y)
    return new_coords
