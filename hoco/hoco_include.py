from pyhocon import ConfigFactory, HOCONConverter


conf = ConfigFactory.parse_file('samples/animal.conf')

print("cat says :", conf.get('cat.garfield.say'))
print("dog says :", conf.get('dog.mutt.say'))

## dog.conf has include "cat.conf" and both have key garfield.say. 
## The value from cat (meow) will override that of dog (bobooooo)
print("After merge :", conf.get('dog.mutt.hates.garfield.say'))

with open('samples/expanded_animal.json', "w") as output_json:
    output_json.writelines(HOCONConverter.to_json(conf))

# we can also use json.dumps
#   fd.write(json.dumps(confTree,indent=4))