import pprint
import extraction_graphql.schema


def query_url(url):
    q = """
    {
      website (url: "https://google.com/" ) {
        url
        title
        image
      }
    }
    """
    result = extraction_graphql.schema.schema.execute(q)
    if result.errors:
        if len(result.errors) == 1:
            raise Exception(result.errors[0])
        else:
            raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    results = query_url("https://google.com/")
    pprint.pprint(results)
