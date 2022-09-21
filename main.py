# The entry point for bpg
import cadquery as cq
from params.default import *

result = (
    cq.Workplane("front")
    .box(2, 2, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 1.5, forConstruction=True)
    .vertices()
    .hole(0.125)
)

cq.exporters.export(result, file_name, file_type)
