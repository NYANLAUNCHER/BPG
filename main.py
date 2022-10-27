# The entry point for bpg
import cadquery as cq
from params.default import *

#result1 = (
#    cq.Workplane("front")
#    .box(2, 2, 0.5)
#    .faces(">Z")
#    .workplane()
#    .rect(1.5, 1.5, forConstruction=True)
#    .vertices()
#    .hole(0.125)
#)

result = (
    cq.Workplane("front")
    .hLine(base_diameter/2)
    .vLine(base_height)
    .hLineTo(inset_diameter/2)
    .vLine(inset_height)
    .lineTo(diameter/2, base_height+inset_height+5)
    .lineTo(tip_radius, length-tip_radius)
    .radiusArc((0, length), -tip_radius)
    .close()
)

result = result.revolve()

cq.exporters.export(result, file_name, file_type)

