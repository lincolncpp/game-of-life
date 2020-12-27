# Window configuration
window_width = 640
window_height = 480
square_size = 10

# Game configuration
rules = [[2, 3], [3]]
generation_ms = 200

# Cell initial state
box_width = window_width//square_size
box_height = window_height//square_size
state = [[False for y in range(0, box_height)] for x in range(0, box_width)]
