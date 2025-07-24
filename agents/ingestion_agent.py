from utils.parser_utils import parse_files

class IngestionAgent:
    def run(self, files):
        chunks = parse_files(files)
        return chunks
