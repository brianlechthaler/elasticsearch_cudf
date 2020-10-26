# elasticsearch_cudf
Query data from Elasticsearch, then store it in a CUDA DataFrame. The RAPIDS cuDF library allows us to store massive dataframes directly in GPU memory where transforms can be made at extremely low latency. Think of it like using a GPU-powered Pandas.


## Prerequisites
You must have the following installed:
* JupyterLab, JupyterNotebook, JupyterHub, etc. (to use included notebooks)
* An up-and-running Elasticsearch instance with data in it, that you can connect to with credentials you provide in the `connect.py` configuration file in this repository
* RAPIDS CLX: https://github.com/rapidsai/clx
* CUDA 11
* Any NVidia GPU since the Pascal architecture (just use AWS if you don't own an NVidia GPU)


## Contents

### Basic ETL with cuDF
* Link: https://github.com/brianlechthaler/elasticsearch_cudf/blob/origin/Basic_ETL_With_cuDF.ipynb
* Description: Simple examples for querying Elasticsearch, and loading the resulting response from Elasticsearch into a cuDF dataframe. Once the data is loaded into the GPU dataframe, we perform a simple transform to deduplicate a list of IP addresses. You could probably just write an Elasticsearch query to return unique IPs, but this is just a simple demonstration of performing a single transform on predictable and structured data.


## Project Lifecycle Notes
* Currently needs lots of work, at the moment all we have is just a few IPy notebooks with some proofs-of-concepts 
