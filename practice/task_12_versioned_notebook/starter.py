class NotebookStore:
    def __init__(self): raise NotImplementedError
    def create(self, entry_id, fields): raise NotImplementedError
    def update(self, entry_id, changes): raise NotImplementedError
    def get(self, entry_id, version=None): raise NotImplementedError
    def history(self, entry_id): raise NotImplementedError
    def revert(self, entry_id, version): raise NotImplementedError
