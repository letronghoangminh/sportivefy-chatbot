import argparse

from utils.import_json_documents import JsonImporter

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--json", action='store_true')
  parser.add_argument("--json-file", type=str)
  
  args = parser.parse_args()
  
  if args.json and args.json_file:
    importer = JsonImporter()
    
    importer.add_documents_from_json(json_file=args.json_file)