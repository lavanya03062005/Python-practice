"""
Create two classes Writer and Reader with methods write() and read().
Derive a class Editor that inherits from both and uses both methods.
"""

class Writer:
    def write(self):
        return "Writing content..."
class Reader:
    def read(self):
        return "Reading content..."
class Editor(Writer, Reader):
    def edit(self):
        return "Editing content..."
editor = Editor()
print(editor.write())
print(editor.read())
print(editor.edit())
