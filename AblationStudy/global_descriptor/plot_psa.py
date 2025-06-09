
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Metric names
metrics = ['MAE', 'RMSE']

# Values and standard deviations
with_descriptor = [0.64, 1.04]
with_descriptor_std = [0.06, 0.05]

without_descriptor = [0.79, 1.14]
without_descriptor_std = [0.11, 0.10]

# X-axis positions
x = np.arange(len(metrics))
width = 0.35  # width of the bars

# Colormap and color selection
cmap = plt.get_cmap('Set2')
colors = [cmap(i) for i in range(4)]  # 4 distinct colors

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot bars individually to allow separate colors
bar1 = ax.bar(x[0] - width/2, with_descriptor[0], width, yerr=with_descriptor_std[0], 
              color=colors[0], capsize=5)
bar2 = ax.bar(x[1] - width/2, with_descriptor[1], width, yerr=with_descriptor_std[1], 
              color=colors[1], capsize=5)
bar3 = ax.bar(x[0] + width/2, without_descriptor[0], width, yerr=without_descriptor_std[0], 
              color=colors[2], capsize=5)
bar4 = ax.bar(x[1] + width/2, without_descriptor[1], width, yerr=without_descriptor_std[1], 
              color=colors[3], capsize=5)

# Custom legend handles
legend_elements = [
    Patch(facecolor=colors[0], label='MAE (All Global Features)'),
    Patch(facecolor=colors[2], label='MAE (No PSA)'),
    Patch(facecolor=colors[1], label='RMSE (All Global Features)'),
    Patch(facecolor=colors[3], label='RMSE (No PSA)')
]

# Formatting
ax.set_ylabel('Error Value (mol kcal$^{-1}$)', fontsize=24, fontweight='bold')
ax.set_xticks(x)
ax.tick_params(axis='y', labelsize=28)
ax.set_xticklabels(metrics, fontsize=24, fontweight='bold')
ax.tick_params(axis='y', labelsize=18)
ax.legend(handles=legend_elements, fontsize=16)
plt.tight_layout()
plt.savefig("mae_rmse_psa.eps", format='eps', dpi=300)
#plt.show()
