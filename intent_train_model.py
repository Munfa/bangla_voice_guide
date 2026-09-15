import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("bangla_intent.csv")
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
# print(df.head())

vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2,5)
)

model = LogisticRegression(max_iter=1000)

X = df["utterance"]
y = df["intent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)

# report = classification_report(y_test, y_pred)
# print(report)

# new_sentences = [
#     "রকেট থেইকা আরেকজনরে টাকা পাঠামু",
#     "আমার বিকাশের ব্যালেন্সটা কই দেখমু",
#     "বিদ্যুৎ বিলটা নগদ দিয়া দিতে চাই"
# ]

# predictions = model.predict(
#     vectorizer.transform(new_sentences)
# )

# for text, pred in zip(new_sentences, predictions):
#     print(text, "->", pred)

# cm = confusion_matrix(y_test, y_pred)

# disp = ConfusionMatrixDisplay(
#     confusion_matrix=cm,
#     display_labels=model.classes_
# )

# disp.plot(xticks_rotation=90)
# plt.tight_layout()
# plt.show()

artifacts = {
    "vectorizer": vectorizer,
    "model": model
}

joblib.dump(artifacts, "joblibs/intent_model_and_vectorizer.joblib")