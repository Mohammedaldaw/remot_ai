import pandas as pd 
import matplotlib.pyplot as plt 


def main():
    df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
    print("First 5 rows:\n",df.head())

df.plot(kind="bar", x="name", y="score", legend=False, color="skyblue")
plt.title("Student Scores")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

if __name__ == "__main__":
    main()
