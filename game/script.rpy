# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Define images for our interactive map
image bg map = Solid("#87CEEB")  # Sky blue background for the map

# ALTERNATIVE: Using an actual image file for the map background
# image bg map = "images/map_background.jpg"  # Replace with your image path
# image bg map = Transform("images/map_background.jpg", size=(1280, 720))  # Resize to fit screen

image roof = Transform(Solid("#A52A2A", xysize=(200, 50)), rotate=45, yanchor=0.5, ypos=0)

# ALTERNATIVE: Using an actual image file for the roof
# image roof = "images/roof.png"  # Replace with your image path
# image roof = Transform("images/roof.png", size=(200, 50), rotate=45, yanchor=0.5, ypos=0)  # Resize and transform

image house = Composite(
    (200, 150),
    (0, 0), Solid("#8B4513", xysize=(200, 100)),  # Brown house body
    (50, 100), Solid("#8B4513", xysize=(100, 50)),  # Door
    (20, 20), Solid("#ADD8E6", xysize=(50, 50)),  # Window 1
    (130, 20), Solid("#ADD8E6", xysize=(50, 50)),  # Window 2
    (0, -25), "roof"  # Roof using a transformed rectangle
)

# ALTERNATIVE: Using an actual image file for the house
# image house = "images/house.png"  # Replace with your image path
# image house = Transform("images/house.png", size=(200, 150))  # Resize to match current dimensions
# 
# You can also use ConditionSwitch to have different house images for different states:
# image house = ConditionSwitch(
#     "persistent.house_style == 'modern'", Transform("images/modern_house.png", size=(200, 150)),
#     "persistent.house_style == 'cottage'", Transform("images/cottage.png", size=(200, 150)),
#     True, Transform("images/default_house.png", size=(200, 150))
# )

# The game starts here.
label start:
    jump map_screen

# Map screen where player can click on locations
label map_screen:
    scene bg map

    # Display instructions
    e "Welcome to the interactive map! Click on the house to visit it."

    # Show the house as a clickable object
    show house at truecenter

    # Make the house clickable
    call screen map_navigation

    # This will be called after returning from the house
    e "You're back at the map."

    # End the game
    return

# House location
label house_location:
    scene bg room
    show eileen happy

    e "Welcome to my house!"
    e "This is a simple demonstration of an interactive map in Ren'Py."
    e "Click anywhere to return to the map."

    # Wait for a click to return to the map
    pause

    jump map_screen

# Define a screen for map navigation
screen map_navigation():
    # Make the house clickable
    imagebutton:
        idle "house"
        hover "house"
        action Jump("house_location")
        xalign 0.5
        yalign 0.5

    # ALTERNATIVE: Using actual image files for the imagebutton with different idle/hover states
    # imagebutton:
    #     idle Transform("images/house_idle.png", size=(200, 150))
    #     hover Transform("images/house_hover.png", size=(200, 150))
    #     action Jump("house_location")
    #     xalign 0.5
    #     yalign 0.5

    # Add a text label for the house
    text "House" xalign 0.5 yalign 0.6 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
