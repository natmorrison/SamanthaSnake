
def left_space(data, space):
    return (space[0] - 1, space[1])


def right_space(data, space):
    return (space[0] + 1, space[1])


def top_space(data, space):
    return (space[0], space[1] - 1)


def bottom_space(data, space):
    return (space[0], space[1] + 1)


def is_snake(data, space):
    snakes = [ [ (s['x'], s['y']) for s in body ] for body in data["board"]["snakes"]["body"] ]
    return (space in snakes)


def is_wall(data, space):
    wall = (data["board"]["width"], data["board"]["height"])
    if space[0] >= wall[0] or space[0] < 0 or
       space[1] >= wall[1] or space[1] < 0:
        return True
    return False


def is_food(data, space):
    food = [(f['x'], f['y']) for f in data["board"]["food"]]
    return (space in food)


def get_head(data):
    return (data['board']['you']['body'][0]['x'], data['board']['you']['body'][0]['y'])
