from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
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



sparql.setQuery("""
    SELECT DISTINCT ?placeName WHERE {
     ?placeName a yago:City108524735 ; dbo:country dbr:India
    }

""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print(results)