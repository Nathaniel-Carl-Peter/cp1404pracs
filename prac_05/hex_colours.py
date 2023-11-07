COLOUR_CODES = {"Absolute Zero": "#0048ba",
                "Acid Green": "#b0bf1a",
                "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636",
                "Amber": "#ffbf00",
                "Apricot": "#fbceb1",
                "Aqua": "#00ffff",
                "Aquamarine1": "#7fffd4",
                "Azure1": "#f0ffff",
                "Blue Violet": "#8a2be2"}
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    print(f" The code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter colour name: ")
