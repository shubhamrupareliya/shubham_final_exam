import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading and Initial Inspection (EDA)
# Load the CSV file. Replace 'RUPARELIYA SHUBHAM JAGDISHBHAI.csv' if your file name differs.
df = pd.read_csv("RUPARELIYA SHUBHAM JAGDISHBHAI.csv")

print("--- Initial Data Inspection ---")
print(f"Shape: {df.shape}")
print("\nColumn Data Types:")
df.info()

# Data Processing/Cleaning

# The dataset contains columns related to a Naive Bayes model output and a client ID.
# These are not useful features for initial EDA or modeling and should be dropped.
cols_to_drop = [
    'CLIENTNUM',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
]
df_cleaned = df.drop(columns=cols_to_drop)
print("\n--- Data Cleaning: Dropped 3 Irrelevant Columns ---")
print(f"New Shape: {df_cleaned.shape}")

# Set a consistent style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150
plt.rcParams['figure.figsize'] = (8, 5)

# =========================================================
# Analysis and Visualization (5 Charts)
# =========================================================

# --- Chart 1: Customer Attrition Rate (Bar Chart) ---
plt.figure(figsize=(6, 4))
# Calculate the count and percentage of each group
attrition_counts = df_cleaned['Attrition_Flag'].value_counts()
total = len(df_cleaned)
attrition_percentages = (attrition_counts / total) * 100

ax1 = sns.barplot(x=attrition_counts.index, y=attrition_counts.values, palette=['#4e79a7', '#e15759'])
plt.title('1. Distribution of Attrition Flag (Customer Status)', fontsize=12)
plt.xlabel('Customer Status')
plt.ylabel('Number of Customers')

# Add percentages on top of the bars
for i, count in enumerate(attrition_counts.values):
    ax1.text(i, count + 50, f'{attrition_percentages.iloc[i]:.2f}%', ha='center', fontsize=10)

plt.tight_layout()
plt.show() # Use plt.show() in Colab

# --- Chart 2: Attrition by Gender (Stacked Bar Chart) ---
# Create a cross-tabulation table normalized by Gender (row)
gender_attrition = pd.crosstab(df_cleaned['Gender'], df_cleaned['Attrition_Flag'], normalize='index') * 100

plt.figure(figsize=(6, 4))
# Plot a stacked bar chart (Red for Attrited, Blue for Existing)
ax2 = gender_attrition.plot(kind='bar', stacked=True, color=['#e15759', '#4e79a7'], ax=plt.gca())
plt.title('2. Attrition Rate by Gender', fontsize=12)
plt.xlabel('Gender')
plt.ylabel('Percentage of Customers')
plt.xticks(rotation=0)
plt.legend(title='Customer Status', loc='center left', bbox_to_anchor=(1.0, 0.5))

# Add percentages inside the bars for better readability
for bar in ax2.patches:
    width = bar.get_width()
    height = bar.get_height()
    x, y = bar.get_xy()
    if height > 0:
        ax2.text(x + width/2, y + height/2, f'{height:.1f}%', ha='center', va='center', fontsize=8, color='black')

plt.tight_layout()
plt.show()

# --- Chart 3: Attrition by Total Relationship Count (Stacked Bar Chart) ---
# Relationship count (number of products) is often inversely related to churn.
rel_count_attrition = pd.crosstab(df_cleaned['Total_Relationship_Count'], df_cleaned['Attrition_Flag'], normalize='index') * 100

plt.figure(figsize=(8, 5))
ax3 = rel_count_attrition.plot(kind='bar', stacked=True, color=['#e15759', '#4e79a7'], ax=plt.gca())
plt.title('3. Attrition Rate by Total Relationship Count (Number of Products)', fontsize=12)
plt.xlabel('Total Relationship Count')
plt.ylabel('Percentage of Customers')
plt.xticks(rotation=0)
plt.legend(title='Customer Status', loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.tight_layout()
plt.show()

# --- Chart 4: Total Transaction Amount Distribution (KDE Plot) ---
# Analyze if attrited customers transact less frequently/spend less overall.
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df_cleaned, x='Total_Trans_Amt', hue='Attrition_Flag', fill=True, alpha=0.6, common_norm=False, palette=['#e15759', '#4e79a7'])
plt.title('4. Distribution of Total Transaction Amount by Customer Status', fontsize=12)
plt.xlabel('Total Transaction Amount (in $)')
plt.ylabel('Density')
plt.tight_layout()
plt.show()

# --- Chart 5: Contacts Count vs. Transaction Count (Box Plot) ---
# Check the relationship between proactive contacts and transaction volume for churned vs. existing.
plt.figure(figsize=(7, 5))
ax5 = sns.boxplot(x='Contacts_Count_12_mon', y='Total_Trans_Ct', hue='Attrition_Flag', data=df_cleaned, palette=['#e15759', '#4e79a7'])
plt.title('5. Total Transaction Count by Contacts Count and Customer Status', fontsize=12)
plt.xlabel('Contacts Count in Last 12 Months')
plt.ylabel('Total Transaction Count')
plt.legend(title='Customer Status')
plt.tight_layout()
plt.show()
