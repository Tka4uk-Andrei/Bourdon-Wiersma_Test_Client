from matplotlib import pyplot as plt


def print_plot(time_arr, val_arr):
    plt.plot(time_arr, val_arr, label = 'Показактель пользователя = Unknown') 
    plt.xlabel('Время в секундах') 
    plt.ylabel('Показатель коэффициента')
    plt.title('Переключаемость внимания')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    val_arr = [1, 0.95, 0.8, 0.48, 0.60, 0.78, 0.97]
    time_arr = [i * 10 for i in range(len(val_arr))]
    print_plot_for(time_arr, val_arr)