import turtle
from PIL import Image
import matplotlib.pyplot as plt

import time
from colorama import Fore, Back, Style




#https://www.webucator.com/article/python-color-constants-module/
#https://www.rapidtables.com/web/color/RGB_Color.html
#https://en.wikipedia.org/wiki/Magenta#/media/File:RBG_color_wheel.svg
#https://www.canva.com/colors/color-wheel/



PANTS_MATCH = {
    "Beige": ("Aqua", "Blue", "Cyan", "Green", "Light_Blue", "Lime_Green", "Magenta", "Orange", "Pink", "Purple", "Red", "Yellow"),
    "Dark_Blue": ("Green", "Light_Blue", "Lime_Green", "Yellow", "Orange"),
}

color_range_top = {
    "Red": (51,255, 0,204, 0,204),
    "Orange": (51,255, 25,229, 0,204),
    "Yellow": (51,255, 51,255, 0,204),
    "Lime Green": (25,229, 51,255, 0,204),
    "Green": (0,204, 51,255, 0,204),
    "Aqua": (0,204, 51,255, 25,229),
    "Cyan": (0,204, 51,255, 51,255),
    "Light Blue": (0,204, 25,229, 51,255),
    "Blue": (0,204, 0,204, 51,255),
    "Purple": (25,229, 0,204, 51,255),
    "Magenta": (51,255, 0,204, 51,255),
    "Pink": (51,255, 0,204, 25,299),
    # "Black": (0,30, 0,30, 0,30),
    # "White": (230,255, 230,255, 230,255)
}

ColorWheel = {
    "Red": (51,255, 0,204, 0,204),
    "Red-Orange": (51,255, 25,204, 0,204),
    "Orange": (51,255, 25,229, 0,204),
    "Yellow-Orange": (51,255, 51,229, 0,204),
    "Yellow": (51,255, 51,255, 0,204),
    "Yellow-Green": (51,204, 51,255, 0,204),
    "Green": (0,204, 51,255, 0,204),
    "Blue-Green": (0,204, 51,204, 51,204),
    "Blue": (0,204, 0,204, 51,255),
    "Blue-Purple": (25,204, 0,204, 51,255),
    "Purple": (25,229, 0,204, 51,255),
    "Red-Purple": (51,229, 0,204, 0,204),
}

# Match:
# 1. Odds of wearing pants (color)
# 2. Odds of wearing shirt (color)
# 3. Color combo taken



def main(file_root: str, file_end: str):

    def pants_to_Shirt():

        # Dictionary for the file path (pants)
        color_options = {
        "1": "Dark_Blue",
        "2": "Beige",
        }

        # Gets user input to access correct name for file path (pants)
        a = input("Choose your color of pants:\n"
                "1. Dark Blue\n"
                "2. Beige\n"
        )

        color_of_pants = color_options.get(a, "Invalid")

        while (color_of_pants == "Invalid"):
            a = input("\nInvalid choice, choose again\n")
            color_of_pants = color_options.get(a, "Invalid")

        # Builds file path to get the picture for the desired pair of pants
        file_name = file_root + color_of_pants + file_end

        # for test cases
        # file_name = "/Users/aprui/Side_Projects/PerfectCloset/Test_Images/Red-Orange.png"


        picture, image = Load_Picture(file_name)
        x, y = image.size # Sets the value of dimensions to iterate over

        RGB_value = getRGB(picture, x, y)

        RGB_to_Color(RGB_value)
        # This value determines the shirts to load in the next method
        # List_Matches(color_of_pants)
    
#----------------------------------------------------------------------------------------------------

    # Gets user input to access correct name for file path (pants)
    option = input("Choose Settings:\n"
            "1. Pants --> Shirt\n"
            "2. Shirt --> Pants\n"
    )

    while (option not in ("1", "2")):
        option = input("\nInvalid choice, choose again\n")
        print(option)
        print(type(option))


    startime = time.monotonic_ns()


    if (option == "1"):
        print("\n\n")
        pants_to_Shirt()

    elif (option == "2"):
        print("\n\n")
        pass

    endtime = time.monotonic_ns()

    print(f'\n   {(endtime - startime)/10000000000:.4f}s   ')
    return 
# Main


def Load_Picture(file_path: str):
    """
    FILE_PATH: the file path to the selected pair of pants or shirt

    Loads the image and converts the image into an "RGB" image

    Returns: loaded image, image in RGB
    """

    image = Image.open(file_path, "r") # Can be many different formats. Opens image
    image_rgb = image.convert("RGB") # Changes image to rgb format
    picture = image_rgb.load() # Allows us to get the size (coordinates) of the image

    return (picture, image_rgb)
# Load_Picture

def getRGB(picture: Image, length: int, width: int):
        """
        PICTURE: the picture of the shirt or the pair of pants
        LENGTH: the length (x-coordinate) of the picture in pixels
        WIDTH: the width (y-coordinate) of the picture in pixels

        Calculates the average amount of red, green, and blue in the entire picture, getting us 
        the color of the image in RGB

        Returns: the color (in RGB) of the image
        """

        # Stores the amount red, green, and blue in each pixel
        Red = 0
        Green = 0
        Blue = 0

        # Keep track of iterations
        denominator = 0

        # calculates the total amount of red, green, and blue in each pixel (omit black and white colors)
        for x in range(length):
            for y in range(width):
                r, g, b = picture[x,y]
                #rgb_value = np.array([r,g,b])
                

                if (r <= 20 and b <= 20 and g <= 20): # Omits black
                    continue
                if (r >= 230 and b >= 230 and g >= 230): # Omits white
                    continue

                Red += r
                Green += g
                Blue += b

                denominator += 1

        # returns the average amount of red, green, and blue in the entire picture, getting us the color of the image
        return ( (Red//denominator), (Green//denominator), (Blue//denominator) )



def RGB_to_Color(RGB_value: tuple):
    """
    RGB_VALUE: a tuple of the RGB values

    Turns the RGB value into a string version of the color

    RETURN: the color (in string) of the color of shirt/pants
    """
    
    def percentage_difference(given: int, min_color: int, max_color: int, color: str):
        """
        GIVEN: the value of R,G, or B (depending on the iteration)
        MIN_COLOR: the minimum color range of the 'GIVEN'
        MAX_COLOR: the maximum color range of the 'GIVEN'
        COLOR: the string and key of the 'color_range' dictionary

        Finds the percentage of different amongst the values of red, green, or blue,
        comparing the given RGB and the range of the value R, G, or B

        Returns: percent difference of value
        """

        average = ((color_range.get(color)[max_color] + color_range.get(color)[min_color]) // 2)

        return round((abs((given - average) / average) * 100), 2)
    
    def out_of_Range(color: str):
        """
        COLOR: the key for the dictionary to access min and max values of the color

        Checks to see if a color is 'out of range' of another color (i.e the color red could never
        mistaken for a green)

        Returns: True (color is out of range) or False (color is in range)
        """

        # Used to access the min and max values in dictionary for each color
        min_val = 0
        max_val = 1

        # Loops through each color to check if RGB value is within its range
        for color_amount in RGB_value:
            if ((color_amount < color_range.get(color)[min_val]) or (color_amount > color_range.get(color)[max_val])):
                return True
            
            min_val += 2
            max_val += 2

        return False
    

#--------------------------------------------------------------------------------------------------------

    # Each color and their range of RGB values
    color_range = {
    "Red": (51,255, 0,204, 0,204),
    "Orange": (51,255, 25,229, 0,204),
    "Yellow": (51,255, 51,255, 0,204),
    "Lime Green": (25,229, 51,255, 0,204),
    "Green": (0,204, 51,255, 0,204),
    "Aqua": (0,204, 51,255, 25,229),
    "Cyan": (0,204, 51,255, 51,255),
    "Light Blue": (0,204, 25,229, 51,255),
    "Blue": (0,204, 0,204, 51,255),
    "Dark Blue": (0,155, 0,155, 0,155),
    "Purple": (25,229, 0,204, 51,255),
    "Magenta": (51,255, 0,204, 51,255),
    "Pink": (51,255, 0,204, 25,299),
    "Black": (0,51, 0,51, 0,51),
    "White": (230,255, 230,255, 230,255)
}
    
    # Seperates the RGB values into own variable
    r, g, b = (RGB_value)
    

    # Used to access the min and max range of each color in the 'color_range' dictionary
    min_red = 0
    max_red = 1
    min_green = 2
    max_green = 3
    min_blue = 4
    max_blue = 5

    combos = []
    Inrange_combos = []

    # Goes through each color in the dictionary and find the potential values for each color
    for color in color_range.keys():

        x = False

        if (out_of_Range(color)):
            x = True

        rank = [color,0,0,0,0]

        rank[1] = percentage_difference(r,min_red, max_red, color)
        rank[2] = percentage_difference(g,min_green, max_green, color)
        rank[3] = percentage_difference(b,min_blue, max_blue, color)
        
        rank[4] = round(((rank[1] + rank[2] + rank[3]) / 3), 2)

        combos.append(rank)

        if (x == False):
            print("In Range", end=" ")
            print(rank)
            Inrange_combos.append(rank)
        else:
            print("Out of Range", end=" ")
            print(rank)
    

    # Returns the color of the shirt/pants
    if (len(Inrange_combos) == 1):
        return Inrange_combos[0][0]
    
    # Finds color value which has the least percent difference 
    sorted_items = sorted(Inrange_combos, key=lambda x: x[4])
    print(sorted_items[0][0])
    return sorted_items[0][0]
# getRGB


"""
June 13, 2023: created program, allowed program to create turtle, and draw squares in a grid-like format
June 17, 2023: creted code to get the color of an image in (RGB), and created supporting methods
June 21, 2023: added color-code to identfy the range of RGB values to multiple different colors
                Found a way to find the color of something given the rgb value (CAP)
June 26, 2023: truly found a way to calculate the color or something based off of RGB value
"""

file_root = "/Users/aprui/Side_Projects/PerfectCloset/Pants/"
# file_root = "/Users/aprui/Side_Projects/PerfectCloset/Test_Images/"
file_end = ".png" 

main(file_root, file_end)  

Odds_wearing_pants = .50
Odds_wearing_shirt = .50
Taken_Combo = False
