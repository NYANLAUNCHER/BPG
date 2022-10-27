# the default parameters for the generator
# unit = mm
import cadquery as cq

# define export params
file_name = "models/butt_plug.step"
file_type = "STEP"

length = 5 * 25.4

# this is the diameter at the base
base_diameter = 3 * 25.4
# height of the base
base_height = 10

# this is the gape diameter
diameter = base_diameter

# between 0 and the diameter
inset_diameter = diameter / 2
inset_height = .8 * 25.4

# outer arc height above the inset
outer_arc_height = .3 * 25.4

# 0 turns it to a strait line
outer_arc = 0
inner_arc = 0

tip_radius = .2 * 25.4

threaded_hole_id = 0

