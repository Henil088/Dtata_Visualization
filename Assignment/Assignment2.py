import pandas as pd
import matplotlib.pyplot as plt


file_path = r"D:\Data_Visualization\Assignment\employee_data.csv"
df = pd.read_csv(file_path)


#OUTPUT:
#    ID Gender  Experience (Years)               Position  Salary
# 0   1      F                   4        DevOps Engineer  109976
# 1   2      M                   6        DevOps Engineer  120088
# 2   3      M                  17          Web Developer  181301
# 3   4      M                   7  Systems Administrator   77530
# 4   5      F                  13  Systems Administrator  152397


# 1. Average Salary of each Position
avg_salary_position = df.groupby('Position')['Salary'].mean()
plt.figure(figsize=(10, 6))
avg_salary_position.plot(kind='bar', edgecolor='black', color='skyblue')
plt.title('Average Salary by Position')
plt.xlabel('Position')
plt.ylabel('Average Salary')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 2. Total number of Male and Female employees
gender_count = df['Gender'].value_counts()
plt.figure(figsize=(6, 6))
gender_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 3. Salary for employees with 10-15 years of experience
exp_salary = df[(df['Experience (Years)'] >= 10) & (df['Experience (Years)'] <= 15)]
plt.figure(figsize=(12, 6))
plt.bar(exp_salary['ID'].astype(str), exp_salary['Salary'], color='orange', edgecolor='black')
plt.title('Salary for Employees with 10-15 Years of Experience')
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 4. Number of positions in the company
position_count = df['Position'].value_counts()
plt.figure(figsize=(10, 6))
position_count.plot(kind='bar', color='green', edgecolor='black')
plt.title('Number of Positions in the Company')
plt.xlabel('Position')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 5. Which position is better in terms of salary
sorted_salary_position = avg_salary_position.sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sorted_salary_position.plot(kind='bar', color='purple', edgecolor='black')
plt.title('Positions Ranked by Average Salary')
plt.xlabel('Position')
plt.ylabel('Average Salary')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Print summary data
print("\nAverage Salary by Position:\n", avg_salary_position)
print("\nGender Count:\n", gender_count)
print("\nEmployees with 10-15 Years Experience:\n", exp_salary[['ID', 'Experience (Years)', 'Salary']])
print("\nNumber of Positions:\n", position_count)


# # Import libraries
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# file_path = r"D:\Data_Visualization\Assignment\Flipkart-Laptops.csv"
# df = pd.read_csv(file_path)  # Change the path if needed

# # =======================
# # 1. Data Preprocessing
# # =======================

# # Show basic info
# print("Initial Data Info:")
# print(df.info())

# # Remove duplicate rows
# df.drop_duplicates(inplace=True)

# # Fill missing values
# df.fillna(method='ffill', inplace=True)  # Forward fill for simplicity

# # Clean Price column (if exists)
# if 'Price' in df.columns:
#     df['Price'] = df['Price'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
#     df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# # Clean Rating column (if exists)
# if 'Rating' in df.columns:
#     df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# print("\nCleaned Data Info:")
# print(df.info())
# print("\nSample Data:\n", df.head())

# # =======================
# # 2. Data Visualization
# # =======================

# # 2.1 Price Distribution
# if 'Price' in df.columns:
#     plt.figure(figsize=(8, 5))
#     df['Price'].hist(bins=30, color='skyblue', edgecolor='black')
#     plt.title("Laptop Price Distribution")
#     plt.xlabel("Price (INR)")
#     plt.ylabel("Count")
#     plt.show()

# # 2.2 Top Brands (if Brand column exists)
# if 'Brand' in df.columns:
#     top_brands = df['Brand'].value_counts().head(10)
#     top_brands.plot(kind='bar', color='green', edgecolor='black')
#     plt.title("Top 10 Laptop Brands")
#     plt.xlabel("Brand")
#     plt.ylabel("Count")
#     plt.xticks(rotation=45)
#     plt.show()

# # 2.3 Average Price by Brand (if Brand column exists)
# if 'Brand' in df.columns and 'Price' in df.columns:
#     avg_price = df.groupby('Brand')['Price'].mean().sort_values(ascending=False).head(10)
#     avg_price.plot(kind='bar', color='orange', edgecolor='black')
#     plt.title("Average Price by Brand (Top 10)")
#     plt.xlabel("Brand")
#     plt.ylabel("Average Price")
#     plt.xticks(rotation=45)
#     plt.show()

# # 2.4 Price vs Rating (if both exist)
# if 'Rating' in df.columns and 'Price' in df.columns:
#     plt.figure(figsize=(8, 5))
#     plt.scatter(df['Rating'], df['Price'], color='red', alpha=0.5)
#     plt.title("Price vs Rating")
#     plt.xlabel("Rating")
#     plt.ylabel("Price (INR)")
#     plt.grid(True)
#     plt.show()

# print("\nData Preprocessing and Visualization Completed!")
