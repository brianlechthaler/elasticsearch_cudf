import elasticsearch as es

##############################################
### Elasticsearch Connection Configuration ###
##############################################

# Set the target index to pull data from, or set to '*' to pull from all indices.
ElasticsearchIndex = 'logstash-*'
# Set the API key ID. Refer to this documentation:
# https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html
ElasticsearchAPIID = 'Your_Elasticsearch_API_ID'
# Set the API key. Refer to this documentation:
# https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html
ElasticsearchAPIKey = 'Your_Elasticsearch_API_Key'
# Set the host. Defaults to localhost over HTTPS
ElasticsearchHost = 'https://localhost:9243'
# Set default timeout to 5 minutes for large amounts of data or slow clusters that will take longer than 10sec to respond to our queries
ElasticsearchQueryTimeoutInSeconds = 300

# Create Elasticsearch connection object from variables specified above. 
# Hint: You probably shouldn't touch this unless you know what you're doing
connection = es.Elasticsearch([ElasticsearchHost], api_key=(ElasticsearchAPIID, ElasticsearchAPIKey), timeout=ElasticsearchQueryTimeoutInSeconds)
