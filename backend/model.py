from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_model(df):
    df['label'] = df['severity'].apply(lambda x: 1 if x >= 7.0 else 0)

    X_train, X_test, y_train, y_test = train_test_split(df['description'], df['label'], test_size=0.2)

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_vec, y_train)

    return model, vectorizer
