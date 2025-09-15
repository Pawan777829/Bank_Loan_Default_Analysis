import pandas as pd
import random

# Step 1: Create CSV File
random.seed(42)
n = 50  

data = {
    "LoanID": range(1, n+1),
    "CustomerID": [f"CUST{1000+i}" for i in range(n)],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(n)],
    "Age": [random.randint(21, 60) for _ in range(n)],
    "Income": [random.randint(20000, 120000) for _ in range(n)],
    "LoanAmount": [random.randint(5000, 50000) for _ in range(n)],
    "LoanTerm": [random.choice([12, 24, 36, 48, 60]) for _ in range(n)],
    "CreditScore": [random.randint(300, 850) for _ in range(n)],
    "Default": [random.choice(["Yes", "No"]) for _ in range(n)]
}

df = pd.DataFrame(data)
df.to_csv("loan_data.csv", index=False)
print("✅ loan_data.csv file created successfully!")

# Step 2: Load and Explore CSV
df = pd.read_csv("loan_data.csv")

print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Summary Statistics:")
print(df.describe())

# Step 3: Data Analysis
print("\n🔹 Default Count:")
print(df["Default"].value_counts())

print("\n🔹 Average Income by Default:")
print(df.groupby("Default")["Income"].mean())

print("\n🔹 Average Credit Score by Default:")
print(df.groupby("Default")["CreditScore"].mean())

print("\n🔹 Loan Amount by Default:")
print(df.groupby("Default")["LoanAmount"].mean())

print("\n🔹 Default Rate by Loan Term:")
print(df.groupby("LoanTerm")["Default"].value_counts(normalize=True).unstack())

# Step 4: Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Default count
sns.countplot(data=df, x="Default")
plt.title("Loan Default Count")
plt.show()

# 2. Default by Gender
sns.countplot(data=df, x="Gender", hue="Default")
plt.title("Loan Default by Gender")
plt.show()

# 3. Credit Score distribution for Defaulters
sns.histplot(data=df[df["Default"]=="Yes"], x="CreditScore", bins=10, kde=True, color="red")
plt.title("Credit Score Distribution (Defaulters)")
plt.show()

# 4. Income vs Default
sns.boxplot(data=df, x="Default", y="Income")
plt.title("Income vs Loan Default")
plt.show()

# 5. Loan Term vs Default
sns.countplot(data=df, x="LoanTerm", hue="Default")
plt.title("Default by Loan Term")
plt.show()

