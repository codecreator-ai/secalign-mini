import matplotlib.pyplot as plt
import csv

labels = []
asr = []
counts = []

with open("results.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        labels.append(row["Setup"])
        asr.append(float(row["ASR"]))
        counts.append(row["Raw_Counts"])

plt.bar(labels, asr, color=['red', 'green'])
plt.ylabel('Attack Success Rate')
plt.title('Mini SecAlign Replication')
plt.ylim(0, max(asr) + 0.05)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate bars with exact numbers
for i, val in enumerate(asr):
    plt.text(i, val + 0.005, f"{val:.2f} ({counts[i]})", ha='center')
plt.savefig("asr_comparison.png", dpi=300, bbox_inches='tight')
plt.show()
