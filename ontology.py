from owlready2 import *

onto = get_ontology('http://geography-ontology.org')

with onto:

    class Country(Thing): pass


    class Capital(Thing): pass


    class Area(Thing): pass


    class Currency(Thing): pass


    class PopRanking(Thing): pass

    # data properties
    class is_capital_of(Capital >> Country, FunctionalProperty): pass


    class has_an_area_of(Country >> Area, FunctionalProperty): pass


    class is_currency_of(Currency >> Country, FunctionalProperty): pass


    class has_a_pop_ranking_of(Country >> PopRanking, FunctionalProperty): pass

france = Country(name="France")
print(france.name)
paris = Capital(name="Paris")
paris.is_capital_of = france
area = Area(area=1212)
print(area.area)


