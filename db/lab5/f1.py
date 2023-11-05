import json
from elasticsearch import Elasticsearch

client = Elasticsearch([{"host": "127.0.0.1", "scheme": "http", "port": 9200}])

client.ping()

indexName = "medical"
# client.indices.delete(index=indexName)
# client.indices.create(index=indexName)

diseaseMapping = {
            "properties": {
                "name": {
                    "type": "text",
                    "fielddata": True
                },
                "title": {
                    "type": "text",
                    "fielddata": True
                },
                "fulltext": {
                    "type": "text",
                    "fielddata": True
                }
            }
}

client.indices.put_mapping(index=indexName, 
                            # doc_type="diseases", 
                           # include_type_name="true", 
                           body=diseaseMapping)

with open('data.json', 'r') as f:
    dataStore = json.load(f)

print("json read")
for data in dataStore:
    print("+", end="")
    try:
        client.index(
            index=data["index"],
            # doc_type=data["doc_type"],
            id=data["id"],
            body=data["body"]
        )
    except Exception as e:
        print(e, end="")
print("ok")