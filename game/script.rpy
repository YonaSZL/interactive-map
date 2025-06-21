# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Define images for our interactive map
image bg map = Solid("#87CEEB")  # Sky blue background for the map

# ALTERNATIVE: Using an actual image file for the map background
# To use a real image file instead of the solid color:
# 1. Place your image in the "images" folder (create it if it doesn't exist)
# 2. Uncomment one of the following lines and comment out the line above
# 3. Replace "map_background.jpg" with your actual filename
#
# Basic usage (original size):
# image bg map = "images/map_background.jpg"
#
# Resize to fit screen:
# image bg map = Transform("images/map_background.jpg", size=(1280, 720))


image house = Composite(
    (200, 150),
    (0, 0), Solid("#8B4513", xysize=(200, 100)),  # Brown house body
    (50, 100), Solid("#8B4513", xysize=(100, 50)),  # Door
    (20, 20), Solid("#ADD8E6", xysize=(50, 50)),  # Window 1
    (130, 20), Solid("#ADD8E6", xysize=(50, 50))  # Window 2
)

# ALTERNATIVE: Using an actual image file for the house
# To use a real image file instead of the composite house:
# 1. Place your complete house image (including roof and all details) in the "images" folder
# 2. Comment out the entire Composite definition above
# 3. Uncomment one of the following options and replace filenames with your actual images
#
# Basic usage (original size):
# image house = "images/house.png"
#
# With resizing to match current dimensions:
# image house = Transform("images/house.png", size=(200, 150))
# 
# Advanced: Using different house styles with ConditionSwitch
# (This allows you to change house styles during gameplay by setting persistent.house_style)
# image house = ConditionSwitch(
#     "persistent.house_style == 'modern'", Transform("images/modern_house.png", size=(200, 150)),
#     "persistent.house_style == 'cottage'", Transform("images/cottage.png", size=(200, 150)),
#     True, Transform("images/default_house.png", size=(200, 150))  # Default fallback
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
    # To use real image files for the imagebutton instead of the "house" displayable:
    # 1. Place your idle and hover state images in the "images" folder
    # 2. Comment out the entire imagebutton block above
    # 3. Uncomment the following block and replace filenames with your actual images
    #
    # imagebutton:
    #     idle Transform("images/house_idle.png", size=(200, 150))  # Image shown normally
    #     hover Transform("images/house_hover.png", size=(200, 150))  # Image shown when mouse hovers over
    #     action Jump("house_location")  # Keep this action to jump to the house location
    #     xalign 0.5  # Center horizontally
    #     yalign 0.5  # Center vertically

    # Add a text label for the house
    text "House" xalign 0.5 yalign 0.6 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
