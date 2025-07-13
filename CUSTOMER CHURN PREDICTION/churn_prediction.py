import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv('churn.csv')
print("Data loaded:")
print(data.head())

# Drop customerID
data.drop('customerID', axis=1, inplace=True)

# Convert TotalCharges to numeric
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data.dropna(inplace=True)

# Encode categorical variables
categorical_cols = data.select_dtypes(include='object').columns.tolist()
categorical_cols.remove('Churn')  # Exclude target column

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

# Encode target variable
data['Churn'] = data['Churn'].map({'No': 0, 'Yes': 1})

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop('Churn', axis=1))
X = pd.DataFrame(scaled_features, columns=data.columns[:-1])
y = data['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ========== 1. Logistic Regression ==========
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

print("\n--- Logistic Regression ---")
print(classification_report(y_test, log_preds))
print("Accuracy:", accuracy_score(y_test, log_preds))

# ========== 2. Random Forest ==========
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

print("\n--- Random Forest ---")
print(classification_report(y_test, rf_preds))
print("Accuracy:", accuracy_score(y_test, rf_preds))

# ========== 3. Gradient Boosting ==========
gb_model = GradientBoostingClassifier()
gb_model.fit(X_train, y_train)
gb_preds = gb_model.predict(X_test)

print("\n--- Gradient Boosting ---")
print(classification_report(y_test, gb_preds))
print("Accuracy:", accuracy_score(y_test, gb_preds))

# Confusion Matrix for Gradient Boosting
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, gb_preds), annot=True, fmt='d', cmap='Purples')
plt.title('Confusion Matrix - Gradient Boosting')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()