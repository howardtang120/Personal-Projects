import matplotlib.pyplot as plt

def main():
    # the dress
    color_count = {'red': 15197, 'yellow': 86235, 'green': 267196, 'cyan': 739, 'blue': 59089, 'purple': 0, 'black': 0, 'grey': 571443, 'white': 101}
    light_count = {'bright': 24484, 'neutral': 847808, 'dark': 127708}
    saturation_count = {'high': 134, 'mid': 428322, 'low': 571544}
    plot_color(color_count)
    plot_light(light_count)
    plot_saturation(saturation_count)
    plt.show()

# Plotting Color Count
def plot_color(color_count):
    fig, ax = plt.subplots()
    ax.bar(list(color_count.keys()), list(color_count.values()))
    ax.set_title('Color Count')
    ax.set_xlabel('Colors')
    ax.set_ylabel('Count')

# Plotting Light Count
def plot_light(light_count):
    fig, ax = plt.subplots()
    ax.bar(list(light_count.keys()), list(light_count.values()))
    ax.set_title('Light Count')
    ax.set_xlabel('Lightness')
    ax.set_ylabel('Count')

# Plotting Saturation Count
def plot_saturation(saturation_count):
    fig, ax = plt.subplots()
    ax.bar(list(saturation_count.keys()), list(saturation_count.values()))
    ax.set_title('Saturation Count')
    ax.set_xlabel('Saturation')
    ax.set_ylabel('Count')

if __name__ == "__main__":
    main()
