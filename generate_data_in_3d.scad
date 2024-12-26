include <positions.scad>

// in units of mm
max_thickness = 70;
min_thickness = 1;
square_width = 1.1;

for (pos = positions) {
    
    x = pos[0] * square_width;
    y = pos[1] * square_width;
    z = pos[2] * (max_thickness - min_thickness) + min_thickness;
    
    translate([x, y, z/2]) {
        // echo(pos[2]);
        cube([square_width, square_width, z], true);
    }
}

// yay it works
