from ants import *
from ants_plans import *
#
# Create a test layout where the gamestate is a single row with 3 tiles
beehive, layout = Hive(make_test_assault_plan()), dry_layout
dimensions = (1, 3)
gamestate = GameState(beehive, ant_types(), layout, dimensions)
#
# Simple test for Place
place0 = Place('place_0')
print(place0.entrance)