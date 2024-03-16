COLOUR_CODES = {"buff": "#f0dc82", "cadetblue": "#5f9ea0",
                "camel": "#c19a6b", "Daffodil": "#ffff31",
                "brown": "#a52a2a", "Dandelion": "#f0e130",
                "gray": "#bebebe", "Indigo": "#4b0082",
                "lemon": "#fff700", "plum": "#8e4585",}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()