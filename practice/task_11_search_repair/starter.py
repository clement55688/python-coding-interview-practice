class SearchIndex:
    def __init__(self, documents):
        self.documents = documents

    def search(self, query):
        tokens = query.lower().split(" ")
        results = []
        for doc in self.documents:
            text = doc["title"].lower()
            if any(token in text for token in tokens):
                results.append(doc["id"])
        return sorted(results)
