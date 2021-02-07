from SPARQLWrapper import SPARQLWrapper, JSON
import random
import sys, os

class OntologyModel:

    def __init__(self, queries):
        self.queries = queries
        self.raw_data = get_sparql_data()
        self.list_

    def get_sparql_data(self):
        #run qparql queries
        pass

    def create_country(self):
        for c in self.raw_data["country"]:
            #create country object
        return list of countries

    ...




if __name__ == '__main__':
    
    sys.path.insert(0, "../sparql")
    from sparql import SparqlQueries
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    onto = OntologyModel(s)

    print(onto.get_random_country())
    print(onto.get_random_capital())
    print(onto.get_capital("France"))
    print(onto.get_country("Paris"))
    print(onto.get_area("France"))
    # France is not in query of Currency
    print(onto.get_currency("Belgium"))
    print(onto.get_currency("France"))
    print(onto.get_pop_ranking("France"))