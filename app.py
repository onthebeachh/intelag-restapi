
data = [ {
    "recipe" : {
      "uri" : "http://www.edamam.com/ontologies/edamam.owl#recipe_c468dc28f8b64bb711125cc150b15c25",
      "label" : "Grilled Deviled Chickens Under a Brick",
      "image" : "https://www.edamam.com/web-img/5f5/5f51c89f832d50da84e3c05bef3f66f9.jpg",
      "source" : "Martha Stewart",
      "sourceIcon" : "http://www.marthastewart.com/sites/all/themes/marthastewart/images/favicon.ico",
      "url" : "http://www.marthastewart.com/recipe/grilled-deviled-chickens-under-a-brick",
      "shareAs" : "http://www.edamam.com/recipe/grilled-deviled-chickens-under-a-brick-c468dc28f8b64bb711125cc150b15c25/chicken",
      "yield" : 4.0,
      "dietLabels" : [ "Low-Carb" ],
      "healthLabels" : [ "Paleo", "Dairy-Free", "Gluten-Free", "Egg-Free", "Peanut-Free", "Tree-Nut-Free", "Soy-Free", "Fish-Free", "Shellfish-Free" ],
      "cautions" : [ ],
      "ingredientLines" : [ "4 baby chickens (poussins) or cornish hens (about 1 1/4 pounds each), or 4 chicken breast halves", "3 lemons, plus wedges for garnish", "4 cloves garlic, peeled and smashed", "1 tablespoon crushed red-pepper flakes, or to taste", "1 tablespoon finely chopped fresh thyme", "1 tablespoon finely chopped fresh rosemary", "1/2 cup olive oil", "Salt, to taste" ],
      "ingredients" : [ {
        "text" : "4 baby chickens (poussins) or cornish hens (about 1 1/4 pounds each), or 4 chicken breast halves",
        "quantity" : 5.0,
        "measure" : "lb",
        "food" : "chickens",
        "weight" : 2267.96
      }, {
        "text" : "3 lemons, plus wedges for garnish",
        "quantity" : 3.0,
        "measure" : "lemon",
        "food" : "lemons",
        "weight" : 174.0
      }, {
        "text" : "3 lemons, plus wedges for garnish",
        "quantity" : 1.0,
        "measure" : "wedge",
        "food" : "lemons",
        "weight" : 7.0
      }, {
        "text" : "4 cloves garlic, peeled and smashed",
        "quantity" : 4.0,
        "measure" : "clove",
        "food" : "garlic",
        "weight" : 12.0
      }, {
        "text" : "1 tablespoon crushed red-pepper flakes, or to taste",
        "quantity" : 1.0,
        "measure" : "tbsp",
        "food" : "red pepper flake",
        "weight" : 5.3
      }, {
        "text" : "1 tablespoon finely chopped fresh thyme",
        "quantity" : 1.0,
        "measure" : "tbsp",
        "food" : "fresh thyme",
        "weight" : 2.4
      }, {
        "text" : "1 tablespoon finely chopped fresh rosemary",
        "quantity" : 1.0,
        "measure" : "tbsp",
        "food" : "fresh rosemary",
        "weight" : 1.7
      }, {
        "text" : "1/2 cup olive oil",
        "quantity" : 0.5,
        "measure" : "cup",
        "food" : "olive oil",
        "weight" : 108.0
      }, {
        "text" : "Salt, to taste",
        "quantity" : 0.0,
        "measure" : "medium",
        "food" : "salt",
        "weight" : 2.7997088
      } ]
    }
  }
]

# FLASK BLUEMIX

import os
from flask import Flask, jsonify

app = Flask(__name__)
# Change current directory to avoid exposure of control files
os.chdir('static')

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/recipes', methods=['GET'])
def get_tasks():
    return jsonify({'data': data})

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))

#FIN FLASK BLUEMIX