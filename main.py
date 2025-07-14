import pandas as pd 
import matplotlib.pyplot as plt 


def main():
    df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
    print("First 5 rows:\n",df.head())

    plt.figure(figsize=(12, 5))
    plt.plot(df["selling_price"].values, color="green")
    plt.title("Used Car Selling Prices")
    plt.xlabel("Car Index")
    plt.ylabel("Selling Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()
