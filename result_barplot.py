import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Calculate min and max values for MSE and PT_TP
pt_tp_min = data['PT_TP'].min()
pt_tp_max = data['PT_TP'].max()

mse_min = data['MSE'].min()
mse_max = data['MSE'].max()

# Normalize PT_TP to the range of MSE
data['PT_TP_scaled'] = ((data['PT_TP'] - pt_tp_min) / (pt_tp_max - pt_tp_min)) * (mse_max - mse_min) + mse_min

# Set the figure size
plt.figure(figsize=(10, 6))

# Define bar width
bar_width = 0.35

# Define the positions of the bars
index = np.arange(len(data['Model']))

# Create bars for each metric
plt.bar(index, data['MSE'], bar_width, color='skyblue', label='MSE')
plt.bar(index + bar_width, data['PT_TP_scaled'], bar_width, color='salmon', label='PTTP')

# Add labels
plt.xlabel('Model')
plt.ylabel('Score')

# Remove legend from default position and place it above the plot (where the title was)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2, fontsize=12)

# Remove title
plt.xticks(index + bar_width / 2, data['Model'], rotation=45)

# Remove the right and top spines (borders)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Save the plot to a file
plt.tight_layout()
plt.savefig('output_plot.png', format='png')  # Save as PNG
# Or save as PDF
# plt.savefig('output_plot.pdf', format='pdf')

# Show the plot
plt.show()
