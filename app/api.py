
def left_space(data, space):
	return (space[0] - 1, space[1])


def right_space(data, space):
	return (space[0] + 1, space[1])


def top_space(data, space):
	return (space[0], space[1] - 1)


def bottom_space(data, space):
	return (space[0], space[1] + 1)


def is_snake(data, space):
	bodies = []
	for snake in data["board"]["snakes"]:
		for bod in snake['body']:
			bodies.append( (bod['x'], bod['y']) )
	return (space in bodies)


def is_wall(data, space):
	wall = (data["board"]["width"], data["board"]["height"])
	if space[0] >= wall[0] or space[0] < 0 or \
	   space[1] >= wall[1] or space[1] < 0:
		return True
	return False


def is_food(data, space):
	food = [(f['x'], f['y']) for f in data["board"]["food"]]
	return (space in food)


def get_head(data):
	return (data['you']['body'][0]['x'], data['you']['body'][0]['y'])


def dont_go(directions, direction):
	if direction in directions:
		directions.remove(direction)
	return directions

def go(directions, direction):
	if direction in directions:
		return [direction]
	else:
		return directions