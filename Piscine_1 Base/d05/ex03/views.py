from django.shortcuts import render

def generate_shades(num_shades=50):
    shades = []
    for i in range(num_shades):
        shade_value = int(255 - (i * 255 // (num_shades - 1)))
        shades.append({
            'red': f'rgb({shade_value}, 0, 0)',
            'green': f'rgb(0, {shade_value}, 0)',
            'blue': f'rgb(0, 0, {shade_value})',
            'black': f'rgb({shade_value}, {shade_value}, {shade_value})',
        })
    return shades

def color(request):
    color_shades = generate_shades()
    return render(request, 'color.html', {'color_shades': color_shades})
