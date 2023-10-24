import numpy as np

import pandas as pd

from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report



# Function to create an artificial dataset

def create_artificial_data(size=100):

    # Generate random data for demonstration

    np.random.seed(42)

    features = np.random.rand(size, 4)

    labels = np.random.choice(['L', 'B', 'R'], size=size)

    artificial_data = pd.DataFrame(data=np.column_stack((labels, features)), columns=['Class', 'F1', 'F2', 'F3', 'F4'])

    return artificial_data



# Function to split the dataset

def splitdataset(balance_data):

    X = balance_data.values[:, 1:5]

    Y = balance_data.values[:, 0]



    X_train, X_test, y_train, y_test = train_test_split(

        X, Y, test_size=0.3, random_state=100)



    return X, Y, X_train, X_test, y_train, y_test



# Function to perform training with giniIndex

def train_using_gini(X_train, X_test, y_train):

    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)

    clf_gini.fit(X_train, y_train)

    return clf_gini



# Function to perform training with entropy

def train_using_entropy(X_train, X_test, y_train):

    clf_entropy = DecisionTreeClassifier(

        criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)

    clf_entropy.fit(X_train, y_train)

    return clf_entropy



# Function to make predictions

def prediction(X_test, clf_object):

    y_pred = clf_object.predict(X_test)

    print("Predicted values:")

    print(y_pred)

    return y_pred



# Function to calculate accuracy

def cal_accuracy(y_test, y_pred):

    print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))

    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)

    print("Report : ", classification_report(y_test, y_pred))



# Driver code

def main():

    data = create_artificial_data(size=100)  # Use the artificial dataset

    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)

    clf_gini = train_using_gini(X_train, X_test, y_train)

    clf_entropy = train_using_entropy(X_train, X_test, y_train)



    # Operational Phase

    print("Results Using Gini Index:")

    y_pred_gini = prediction(X_test, clf_gini)

    cal_accuracy(y_test, y_pred_gini)



    print("Results Using Entropy:")

    y_pred_entropy = prediction(X_test, clf_entropy)

    cal_accuracy(y_test, y_pred_entropy)



if __name__ == "__main__":

    main()

