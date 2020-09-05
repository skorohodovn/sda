
def get_drink_by_profession(param):
    switcher = {
            "jabroni":	"Patron Tequila",
            "school counselor":	"Anything with Alcohol",
            "programmer":	 "Hipster Craft Beer",
            "bike gang member":	"Moonshine" ,
            "politician":	"Your tax dollars" ,
            "rapper":	"Cristal"
            }
    output = switcher.get(param.lower(), "Beer")
    print(output)


get_drink_by_profession(None)
