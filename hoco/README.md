### HOCON is similar to JSON but with more flexibility

    HOCON configurations can be used in patterns where we deal with multiple configurations
    - helps in merging from multiple configurations
    - helps when we include or refer to other configurations

### Setup
    https://github.com/typesafehub/config/blob/master/HOCON.md
    https://github.com/chimpler/pyhocon

    HOCON in javascript: https://github.com/josephtzeng/hocon-parser and https://github.com/maor-rosenfeld/hocon-js

    cd hoco
    prox (enabled)
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

    (pip install pyhocon
    pip freeze > requirements.txt)

### Test run
    python hoco1.py

### Convert to other formats
    cat samples/database.conf | pyhocon -f json
    cat samples/database.conf | pyhocon -f yaml
    cat samples/database.conf | pyhocon -f properties

### Using Includes option i.e refering other configs
    dog.conf include "cat.conf" and both have key garfield.say. The value from cat (meow) will override dog (bobooooo)
        
        python hoco_include.py

### Consolidating multiple configurations using include and writing the final o/p

    pyhocon -i samples/animal.conf -o samples/animal_expanded.json

    In python:
        from pyhocon import ConfigFactory, HOCONConverter
        conf = ConfigFactory.parse_file('samples/animal.conf')
        HOCONConverter.to_json(conf)

### HOCON in Java
        Use below maven dependencies:
            <dependency>
                <groupId>com.typesafe</groupId>
                <artifactId>config</artifactId>
                <version>1.3.0</version>
            </dependency>
        and then use....
            Config config = ConfigFactory.parseString(text);
            String id = config.getString("id");
            Long model = config.getLong("model");
            
