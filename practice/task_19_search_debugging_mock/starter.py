import re


class SearchIndex:
    def __init__(self, documents: list[dict]):
        self.documents = documents
        self.by_token: dict[str, set[str]] = {}
        for document in documents:
            for token in document.get("text", "").split(" "):
                self.by_token.setdefault(token, set()).add(document.get("id"))

    def search(self, query: str) -> list[dict]:
        words = query.split()
        matches: set[str] = set()
        filters: dict[str, str] = {}
        for word in words:
            if ":" in word:
                key, value = word.split(":")
                filters[key] = value
            else:
                matches.update(self.by_token.get(word, set()))

        result = []
        for document in reversed(self.documents):
            if document.get("id") in matches and all(document.get(k) == v for k, v in filters.items()):
                result.append(document)
        return result


def normalize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text)
