from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlQueries : 
    def __init__(self, sparql):
        self.sparql = sparql
        
    def get_countries(self):
        self.sparql.setQuery("""
        PREFIX dbo: <http://dbpedia.org/ontology/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 

        select distinct ?countrylabel
        where { 
            ?country a <http://dbpedia.org/class/yago/WikicatMemberStatesOfTheUnitedNations> .
            ?country rdfs:label ?countrylabel .
            FILTER ( lang(?countrylabel) = 'fr')
        }
        """)
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert()

    def get_capitals_and_countries(self):
        self.sparql.setQuery("""
            PREFIX dbo: <http://dbpedia.org/ontology/>
            PREFIX dbr: <http://dbpedia.org/resource/>

            SELECT ?country ?capital
            WHERE {
            ?country a <http://dbpedia.org/class/yago/WikicatMemberStatesOfTheUnitedNations>  .
            ?country dbp:capital ?capital.
            ?country rdfs:label ?countrylabel .
            FILTER ( lang(?countrylabel) = 'fr')
            } """)
        self.sparql.setReturnFormat(JSON)
        print(self.sparql.query().convert())
        return self.sparql.query().convert()
    
    def get_countries_area(self) :
        self.sparql.setQuery("""
            PREFIX  dbo:  <http://dbpedia.org/ontology/>
            PREFIX  yago: <http://dbpedia.org/class/yago/>
            PREFIX  dbp:  <http://dbpedia.org/property/>
            PREFIX  dct:  <http://purl.org/dc/terms/>

            SELECT DISTINCT  *
            WHERE
            { ?country  a  <http://dbpedia.org/class/yago/WikicatMemberStatesOfTheUnitedNations>.
            ?country  dbp:areaKm  ?area.
           }
            """)
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert() 
    
        
    def get_countries_currency(self) :
        self.sparql.setQuery("""
            PREFIX  dbo:  <http://dbpedia.org/ontology/>
            PREFIX  yago: <http://dbpedia.org/class/yago/>
            PREFIX  dbp:  <http://dbpedia.org/property/>
            PREFIX  dct:  <http://purl.org/dc/terms/>

            SELECT DISTINCT ?country, ?currency
            WHERE
            { ?country  a  <http://dbpedia.org/class/yago/WikicatMemberStatesOfTheUnitedNations>.
            ?country  dbp:currency  ?currency.
            }
            """)
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert() 

    def get_countries_population_ranking(self):
        self.sparql.setQuery("""
            PREFIX  dbo:  <http://dbpedia.org/ontology/>
            PREFIX  yago: <http://dbpedia.org/class/yago/>
            PREFIX  dbp:  <http://dbpedia.org/property/>
            PREFIX  dct:  <http://purl.org/dc/terms/>

            SELECT DISTINCT  *
            WHERE
            { ?country  a  <http://dbpedia.org/class/yago/WikicatMemberStatesOfTheUnitedNations>.
              ?country dbo:populationTotalRanking ?ranking.
               }
            """)
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert() 
      
    def get_data_from_get_countries(self):
        return [d["countrylabel"]["value"] for d in self.get_countries()["results"]["bindings"]]
    
    def get_data_from_get_capitals_and_countries(self):
        return  [(d["country"]["value"].split('/')[-1], d["capital"]["value"].split('/')[-1]) for d in self.get_capitals_and_countries()["results"]["bindings"]]
    
    def get_data_from_get_countries_area(self):
        return  [( d["country"]["value"].split('/')[-1], d["area"]["value"]) for d in self.get_countries_area()["results"]["bindings"]]
    
    def get_data_from_get_countries_currency(self):
        return  [( d["country"]["value"].split('/')[-1], d["currency"]["value"]) for d in self.get_countries_currency()["results"]["bindings"]]
    
    def get_data_from_get_countries_population_ranking(self):
        return  [( d["country"]["value"].split('/')[-1], d["ranking"]["value"]) for d in self.get_countries_population_ranking()["results"]["bindings"]]

      
if __name__ == '__main__':
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    
    #print(s.get_data_from_get_countries())
    print(s.get_data_from_get_capitals_and_countries())
    #print(s.get_data_from_get_countries_area())
    #print(s.get_data_from_get_countries_wealth())
    #print(s.get_data_from_get_countries_population_ranking())
