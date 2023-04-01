import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

sample_dataset = "src/data/sample_imdb_data.csv"
build_model = "src/model/pickles/model.pkl"
build_vectorizer = "src/model/pickles/vectorizer.pkl"
# Load the data
df = pd.read_csv(sample_dataset)
print(df.columns)

# Preprocess the data
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Save the model
import pickle
with open(build_model, 'wb') as f:
    pickle.dump(clf, f)

# save the CountVectorizer instance to file
with open(build_vectorizer, 'wb') as f:
    pickle.dump(vectorizer, f)

