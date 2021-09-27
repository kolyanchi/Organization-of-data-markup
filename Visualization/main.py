from PIL import Image, ImageDraw
import json
import os


for js in os.listdir("json"): # Selecting a json file from the directory
    for foto in os.listdir("img"): # Selecting an image from the catalog
        if js[:js.find(".json")] == foto: # If the names of the two files are equal
            with open("json/"+ js) as json_file: 
                data = json.load(json_file)
                for value in data["objects"]: # Loop for getting coordinates
                    img = Image.open("img/"+foto) # Opening an image from a catalog
                    draw = ImageDraw.Draw(img)
                    # Drawing a triangle by coordinates
                    draw.polygon([(value["points"]['exterior'][0][0],value["points"]['exterior'][0][1]), (value["points"]['exterior'][1][0], value["points"]['exterior'][1][1]), (value["points"]['exterior'][2][0],value["points"]['exterior'][2][1])], fill = None,outline="red")
                    img.save(foto)
                    os.replace(foto, "viz_img/" + foto)
                    break
            break

