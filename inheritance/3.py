"""
Create a base class Logger with a method log().
Derive a class FileLogger that overrides log() but still calls the parent method using super().
"""

class Logger:
    def log(self, message):
        return f"Logging message: {message}"
class FileLogger(Logger):
    def log(self, message):
        parent_log = super().log(message)
        return f"{parent_log} (also saved to file)"
file_logger = FileLogger()
print(file_logger.log("This is a log message."))
