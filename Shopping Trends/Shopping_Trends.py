import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('shopping_trends_updated.csv')

sns.set(style="whitegrid")

# Distribution of Customer Ages
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Customer Ages', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# Average Purchase Amount by Category
plt.figure(figsize=(10, 6))
category_avg_purchase = data.groupby('Category')['Purchase Amount (USD)'].mean().sort_values()
sns.barplot(x=category_avg_purchase.values, y=category_avg_purchase.index, palette='viridis')
plt.title('Average Purchase Amount by Category', fontsize=16)
plt.xlabel('Average Purchase Amount (USD)', fontsize=12)
plt.ylabel('Category', fontsize=12)
plt.show()

# Number of Purchases by Gender
plt.figure(figsize=(8, 6))
gender_purchases = data['Gender'].value_counts()
sns.barplot(x=gender_purchases.index, y=gender_purchases.values, palette='coolwarm')
plt.title('Number of Purchases by Gender', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Number of Purchases', fontsize=12)

gender_avg_purchase = data.groupby('Gender')['Purchase Amount (USD)'].mean()
for i, gender in enumerate(gender_avg_purchase.index):
    plt.text(i, gender_purchases[gender] + 5, f'${gender_avg_purchase[gender]:.2f}', ha='center', fontsize=12, color='black')

plt.show()

# Most Commonly Purchased Items by Category
plt.figure(figsize=(14, 8))
most_purchased_items = data.groupby(['Category', 'Item Purchased']).size().reset_index(name='Counts')
most_purchased_items = most_purchased_items.sort_values('Counts', ascending=False).groupby('Category').head(3)
sns.barplot(x='Counts', y='Item Purchased', hue='Category', data=most_purchased_items, dodge=False, palette='pastel')
plt.title('Most Commonly Purchased Items by Category', fontsize=16)
plt.xlabel('Number of Purchases', fontsize=12)
plt.ylabel('Item Purchased', fontsize=12)
plt.legend(title='Category')
plt.show()

# Total Spending by Season
plt.figure(figsize=(10, 6))
season_avg_purchase = data.groupby('Season')['Purchase Amount (USD)'].sum().sort_values()
sns.barplot(x=season_avg_purchase.index, y=season_avg_purchase.values, palette='autumn')
plt.title('Total Spending by Season', fontsize=16)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Total Spending (USD)', fontsize=12)
plt.show()

# Distribution of Payment Methods
plt.figure(figsize=(8, 6))
payment_method_counts = data['Payment Method'].value_counts()
sns.barplot(x=payment_method_counts.index, y=payment_method_counts.values, palette='muted')
plt.title('Distribution of Payment Methods', fontsize=16)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Number of Transactions', fontsize=12)
plt.show()

# Frequency of Purchases Across Age Groups
bins = [18, 25, 35, 45, 55, 65, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

plt.figure(figsize=(10, 6))
age_group_purchases = data['Age Group'].value_counts().sort_index()
sns.barplot(x=age_group_purchases.index, y=age_group_purchases.values, palette='coolwarm')
plt.title('Frequency of Purchases Across Age Groups', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Number of Purchases', fontsize=12)
plt.show()

# Popularity of Colors Among Customers
plt.figure(figsize=(10, 6))
color_popularity = data['Color'].value_counts()
sns.barplot(x=color_popularity.index, y=color_popularity.values, palette='Set2')
plt.title('Popularity of Colors Among Customers', fontsize=16)
plt.xlabel('Color', fontsize=12)
plt.ylabel('Number of Purchases', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Average Purchase Amount by Review Rating
avg_purchase_by_rating = data.groupby('Review Rating')['Purchase Amount (USD)'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Review Rating', y='Purchase Amount (USD)', data=avg_purchase_by_rating, palette='Blues_d')
plt.title('Average Purchase Amount by Review Rating', fontsize=16)
plt.xlabel('Review Rating', fontsize=12)
plt.ylabel('Average Purchase Amount (USD)', fontsize=12)
plt.yticks(np.arange(0, avg_purchase_by_rating['Purchase Amount (USD)'].max() + 100, 100))
plt.show()

# Relationship Between Customer Age and Product Category
plt.figure(figsize=(14, 8))
sns.violinplot(x='Category', y='Age', data=data, palette='muted', inner=None)
sns.swarmplot(x='Category', y='Age', data=data, color='black', alpha=0.5, size=3)
plt.title('Relationship Between Customer Age and Product Category', fontsize=18)
plt.xlabel('Product Category', fontsize=14)
plt.ylabel('Age', fontsize=14)
plt.xticks(rotation=45)
plt.ylim(15, 75)
plt.show()

print("Graphs generated for questions 1 to 7, 10, 11, 14, 16, and 18. Extend the script for additional insights.")