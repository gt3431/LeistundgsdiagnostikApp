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
    plt.xlabel("Time")
    plt.ylabel("Power")
    plt.gca().set_yticklabels([f'{int(w)} W' for w in plt.gca().get_yticks()])
    plt.gca().set_xticklabels([f'{int(w)} s' for w in plt.gca().get_xticks()])
    plt.grid(True)
    
    plt.savefig('figures/sortetpower.png')
    plt.show()
    
