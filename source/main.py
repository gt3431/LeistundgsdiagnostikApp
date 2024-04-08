from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data = load_data('data/activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])     

    plt.plot(sorted_power_W[::-1])
    plt.title("Powercurve")
    plt.xlabel("t / s")
    plt.ylabel("P / W")
    plt.savefig('figures/sortetpower.png')
    plt.show()
