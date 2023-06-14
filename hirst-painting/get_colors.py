import colorgram

class Colors:
    def __init__(self, image_path, top_n_colors):
        self.image_path = image_path
        self.top_n_colors = top_n_colors
        self.colors = self.get_colors(image_path)

    def get_colors(self, image_path):
        colors = colorgram.extract(self.image_path, self.top_n_colors)

        colors_list = []

        for color in colors:
            color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
            colors_list.append(color_tuple)

        return colors_list
