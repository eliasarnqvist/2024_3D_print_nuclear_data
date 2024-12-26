import numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import csv
# from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
# Settings
# =============================================================================

# NOTE: this has been moved to the scad script, do not change here

# in units of mm
max_thick = 1
min_thick = 0
square_size = 1

# =============================================================================
# Import data
# =============================================================================

file_1 = 'nuclear_data_raw\BE_1.csv'
save_path = 'nuclear_data_output\BE_data.csv'

df = pd.read_csv(file_1)

# only keep positive binding energies
df = df[df['bindingEnergy(keV)'] >= 0]
df.loc[len(df)] = [0, 1, 0]

be = df['bindingEnergy(keV)'].to_numpy()
heights = (-be/max(be))*(max_thick-min_thick) + max_thick

df['xx'] = df['n'] * square_size
df['yy'] = df['z'] * square_size
df['zz'] = heights

df.to_csv(save_path, index=False)

with open('positions.scad', 'w') as f:
    f.write('// OpenSCAD script generated from CSV\n')
    f.write('positions = [\n')
    # Loop through each row and write positions
    for index, row in df.iterrows():
        f.write(f'    [{row["xx"]}, {row["yy"]}, {row["zz"]}],\n')
    f.write('];\n\n')

# =============================================================================
# Plot data
# =============================================================================

plt.close('all')

inch_to_mm = 25.4

# fig, ax = plt.subplots(figsize = (110/inch_to_mm, 70/inch_to_mm))
fig = plt.figure(figsize = (110/inch_to_mm, 70/inch_to_mm))
ax = fig.add_subplot(111, projection='3d')

x = df['xx'].to_numpy()
y = df['yy'].to_numpy()
z = df['zz'].to_numpy()

ax.bar3d(x, y, np.zeros_like(z), dx=square_size, dy=square_size, dz=z)

plt.tight_layout(pad = 0.5)
# plt.subplots_adjust(wspace=0, hspace=0)

# plt.savefig(f'plots_2\\{save_name}.jpg', dpi=300)
# plt.savefig(f'plots_2\\{save_name}.pdf')

plt.show()
