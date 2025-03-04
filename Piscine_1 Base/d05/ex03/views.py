from django.shortcuts import render


# Create your views here.
def generate_shade(color, num_shades=50):
    shades = []
    for i in range(num_shades):
        shades_value = int(255 - (i * 255 // (num_shades - 1)))
        if color == "red":
            shade = f'rgb({shades_value}, 0, 0)'
        elif color == "green":
            shade = f'rgb(0, {shades_value}, 0)'
        elif color == "blue":
            shade = f'rgb(0, 0, {shades_value})'
        shades.append(shade)
    return shades


def color(request):
    colors = ['red', 'green', 'blue']
    color_shades = {
        color: generate_shade(color) for color in colors
    }

    return render(request, 'color.html', {'color_shades': color_shades})