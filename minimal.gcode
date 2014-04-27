; filename = composition.3w
; print_time = 196;
; machine = daVinciF10
; material = abs
; layer_height = 0.2
; total_layers = 173
; total_filament = 0.00
; extruder = 1
G21 ; set units to millimeters
M107
M190 S100 ; wait for bed temperature to be reached
M104 S230 ; set temperature
M109 S230 ; wait for temperature to be reached
G90 ; use absolute coordinates

G92 E0
M82 ; use absolute distances for extrusion
G1 F1800.000 E-1.00000

G92 E0
G1 Z0.300 F7800.000
G1 X81.765 Y82.676 F7800.000
G1 E1.00000 F1800.000
G1 X82.795 Y81.666 E1.10023 F540.000
G1 X83.405 Y81.116 E1.15730
G1 X84.135 Y80.496 E1.22385
G1 X84.725 Y80.026 E1.27626
G1 F1800.000 E10.96694

G92 E0
M107
M84


