from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# read the file
df = pd.read_csv("exercise_2_data.csv")

# change the response to binary
df["y"] = pd.factorize(df.y)[0]

X = df.drop("y", axis=1)
y = df["y"]

x_test = pd.DataFrame([[0,0,0]], columns=["x1", "x2", "x3"])

for n in [1, 3]:
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X, y)
    response = knn.predict(x_test)

    if response == 1:
        print(f"When n is {n}, predict says green")
    
    elif response == 0:
        print(f"When n is {n}, predict says red")

    else:
        print("something went wrong")