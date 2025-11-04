import matplotlib.pyplot as plt
import numpy as np

# Metrics
metrics = ['Response Time (ms)', 'Throughput (ops/sec)', 'Availability (%)']

# Sample values (replace with your actual experimental results)
paxos_values = [120, 500, 85]  # Example: Response Time high, Throughput moderate, Availability moderate
eventual_values = [40, 1200, 95]  # Example: Response Time low, Throughput high, Availability high

x = np.arange(len(metrics))  # metric positions
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(8,5))
bars1 = ax.bar(x - width/2, paxos_values, width, label='Paxos', color='skyblue')
bars2 = ax.bar(x + width/2, eventual_values, width, label='Eventual', color='salmon')

# Add labels and title
ax.set_ylabel('Value')
ax.set_title('Comparison of Paxos and Eventual Consistency')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Add value labels on top of bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0,3),
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

plt.tight_layout()
plt.show()
