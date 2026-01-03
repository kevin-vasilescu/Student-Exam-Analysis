import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the sample data
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Math': [85, 92, 78, 95, 88, 76, 91, 89],
    'English': [90, 88, 82, 93, 85, 80, 94, 87],
    'Science': [88, 90, 75, 96, 92, 79, 89, 91],
    'History': [92, 85, 88, 91, 87, 83, 90, 86]
}

df = pd.DataFrame(data)

print("=" * 50)
print("STUDENT EXAM ANALYSIS")
print("=" * 50)
print("\nDataset Overview:")
print(df)

print("\n" + "=" * 50)
print("BASIC STATISTICS")
print("=" * 50)
print("\nMean scores by subject:")
print(df.mean(numeric_only=True))

print("\nMedian scores by subject:")
print(df.median(numeric_only=True))

print("\nStandard deviation by subject:")
print(df.std(numeric_only=True))

# Calculate average score for each student
df['Average'] = df[['Math', 'English', 'Science', 'History']].mean(axis=1)
print("\nStudent averages:")
print(df[['Student', 'Average']].sort_values('Average', ascending=False))

print("\n" + "=" * 50)
print("DATA INSIGHTS")
print("=" * 50)
print(f"\nTop performer: {df.loc[df['Average'].idxmax(), 'Student']} (Average: {df['Average'].max():.2f})")
print(f"Lowest performer: {df.loc[df['Average'].idxmin(), 'Student']} (Average: {df['Average'].min():.2f})")
print(f"Overall class average: {df[['Math', 'English', 'Science', 'History']].values.mean():.2f}")

print("\n" + "=" * 50)
print("GENERATING VISUALIZATIONS...")
print("=" * 50)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Student Exam Analysis Dashboard', fontsize=16, fontweight='bold')

# 1. Box plot of scores by subject
ax1 = axes[0, 0]
df[['Math', 'English', 'Science', 'History']].boxplot(ax=ax1)
ax1.set_title('Score Distribution by Subject')
ax1.set_ylabel('Score')
ax1.grid(True, alpha=0.3)

# 2. Bar chart of average scores by student
ax2 = axes[0, 1]
df_sorted = df.sort_values('Average', ascending=True)
ax2.barh(df_sorted['Student'], df_sorted['Average'], color='skyblue')
ax2.set_title('Student Average Scores')
ax2.set_xlabel('Average Score')
ax2.grid(True, alpha=0.3, axis='x')

# 3. Line chart of scores for each subject
ax3 = axes[1, 0]
for subject in ['Math', 'English', 'Science', 'History']:
    ax3.plot(df['Student'], df[subject], marker='o', label=subject)
ax3.set_title('Score Comparison Across Subjects')
ax3.set_ylabel('Score')
ax3.set_xlabel('Student')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='x', rotation=45)

# 4. Histogram of average scores
ax4 = axes[1, 1]
ax4.hist(df['Average'], bins=5, color='lightcoral', edgecolor='black')
ax4.set_title('Distribution of Student Average Scores')
ax4.set_xlabel('Average Score')
ax4.set_ylabel('Number of Students')
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('exam_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'exam_analysis.png'")
plt.show()

print("\n" + "=" * 50)
print("Analysis complete!")
print("=" * 50)
