from owlready2 import *

onto = get_ontology('http://geography-ontology.org')

with onto:

    class Continent(Thing):
        pass


    class Country(Thing):
        pass


    class CapitalCity(Thing):
        pass


    class HeadOfSate(Thing):
        pass
