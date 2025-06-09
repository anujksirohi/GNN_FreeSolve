import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("groupwise_results.csv")
groups = df.iloc[:, 0].tolist()
rmse = df.iloc[:, 2].tolist()
mea = df.iloc[:, 3].tolist()
r_2 = df.iloc[:, 4].tolist()
pearson = df.iloc[:, 5].tolist()
# print(groups)
# print(rmse)
# print(mea)
# print(r_2)
# print(pearson)


cmap = plt.get_cmap('viridis')  # You can try 'Set2' or 'tab20' for pastel/discrete
#cmap = plt.get_cmap('plasma')
#cmap = plt.get_cmap('tab20')
colors = [cmap(i / len(groups)) for i in range(len(groups))]

plt.figure(figsize=(10, 10), dpi=300)
#plt.bar(groups, rmse)
plt.bar(groups, pearson, color=colors)


plt.xlabel(r'Groups', fontsize=24, fontweight='bold')
plt.ylabel(r'Pearson Correlation $Pr$', fontsize=24, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tick_params(axis='both', which='major', labelsize=25, width=1, length=6)
plt.tick_params(axis='both', which='minor', labelsize=25, width=0.5, length=3)

plt.savefig('pr.eps', dpi=300, bbox_inches='tight', format='eps')
plt.tight_layout()
#plt.show()