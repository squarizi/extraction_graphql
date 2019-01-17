
This repository is an Example project using [Graphene](https://graphene-python.org/)
and [flask-graphql](https://github.com/graphql-python/flask-graphql) to create a [GraphQL](https://graphql.org/)
server and client pair in Python.

The example server will crawl websites and extract summaries using the [extraction](https://github.com/lethain/extraction)
library (mostly relying on Opengraph metadata).

You can query the server via [GraphiQL](https://github.com/graphql/graphiql) by running
the server and visiting `http://localhost:5000`.

---

Queries against the server look like:

    {
      website(url: "https://google.com") {
        title
	      image
	      description
      }
    }

And responses look like:

    {
      "data": {
        "website": {
	        "title":"Google",
	        "image":"https://google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png",
	        "description":"© 2019 - Privacidade - Termos"
        }
	    }
    }

Take a look at the `extraction_graphql` directory for more.

## Setup

    git clone git@github.com:squarizi/extraction_graphql.git
    cd extraction_graphql
    python3 -m venv env
    . ./env/bin/activate
    pip install -r requirements.txt
    pip install -e .
    python extraction_graphql/server.py &
    python extraction_graphql/http_client.py


