# 2024_3D_print_nuclear_data
Scripts that can be used to generate stl-files from nuclear data, which can then be 3D printed. Useful for teaching applications or just for fun. 

The Python script generates positions.scad to be read in OpenSCAD and then made into a 3D stl file. Cura can be used to get gcode from the stl for 3D printing. 

On my system, OpenSCAD takes several minutes to render the stl file. This feels too long. Maybe I can optimize something or my 3D model is just large. 

In this example, the data is from https://www.nndc.bnl.gov/nudat3/

Inspiration from https://github.com/cl-fontana

Fall 2024
