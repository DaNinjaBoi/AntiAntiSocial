import pygame

class dropdown:

    def __init__(self, dimensions, color, position):
        self.dimensions = dimensions
        self.color = color
        self.position = position


class background:

    def __init__(self, image):
        self.image = image


"""
1. initial click sidebar appears

2. when sidebar appears all of the dropdowns should be hidden

3. when clicked onto the dropdowns, they should be opened up and animated the dropdown.

4. now we need to make sure that clicking a specific dropdown will hide all of the other ones

"""