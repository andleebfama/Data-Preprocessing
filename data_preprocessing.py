##Titanic: Machine Learning from Disaster

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the train dataset
df = pd.read_csv("train.csv")
print("Original Dataset Loaded:")
print(df.head())

# Step 1: Drop column with too many missing values
df = df.drop(columns=['Cabin'])

# Step 2: Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Step 3: Drop columns not useful for preprocessing or modeling
df = df.drop(columns=['PassengerId', 'Name', 'Ticket'])

# Step 4: Convert categorical column 'Sex' and 'Embarked' to numerical (encoding)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Step 5: Normalize numerical features
scaler = MinMaxScaler()
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Step 6: Save the cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)
print("Cleaned dataset saved as 'titanic_cleaned.csv'.")
