from SPARQLWrapper import SPARQLWrapper, JSON
import random
import sys, os


class OntologyModel:

    def __init__(self, queries):
        self.queries = queries
        self.raw_data = self.get_sparql_data()

    def get_sparql_data(self):
        return [self.queries.get_data_from_get_countries(), self.queries.get_data_from_get_capitals_and_countries(),
                self.queries.get_data_from_get_countries_area(), self.queries.get_data_from_get_countries_currency(),
                self.queries.get_data_from_get_countries_population_ranking()]

    def create_country(self):
        for c in self.raw_data["country"]:
            pass
            # create country object
            # return list of countries


if __name__ == '__main__':
    sys.path.insert(0, "../sparql_package")
    from sparql_package import SparqlQueries

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    onto = OntologyModel(s)
    print(onto.raw_data[0])
