from j2g import convert
import sys
import json
from datetime import datetime
import os

def cli():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file path>', file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path) as f:
        schema = f.read()
        schema = convert(schema)
        schema = {k: v for (k,v) in schema}
        schema = {
            '//': f'Generated by j2g at {datetime.utcnow()}. DO NOT EDIT',
            'columns': schema,
        }

        print(json.dumps(schema, indent=2))
