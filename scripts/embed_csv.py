#!/usr/bin/env python3
"""Replace the bundled dataset in index.html with a new comma-separated CSV.

Usage:
    python scripts/embed_csv.py path/to/your_export.csv
    python scripts/embed_csv.py path/to/data.csv --html index.html

Only uses the Python standard library. The original CSV is not overwritten.
"""
import argparse
import csv
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', type=Path, help='UTF-8 CSV file to embed')
    parser.add_argument('--html', type=Path, default=Path(__file__).resolve().parents[1] / 'index.html', help='Target HTML file (default: repository index.html)')
    args = parser.parse_args()

    with args.csv_file.open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.reader(handle)
        headers = next(reader, None)
        if not headers:
            parser.error('CSV must contain a header row.')
        if len(set(headers)) != len(headers):
            parser.error('CSV has duplicate header names. Please make them unique.')
        rows = [[row[i] if i < len(row) else '' for i in range(len(headers))] for row in reader if any(value for value in row)]

    data = {'name': args.csv_file.name, 'headers': headers, 'rows': rows}
    # Unicode is JSON-escaped, so hostile CSV text cannot terminate the HTML script tag.
    safe_json = json.dumps(data, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c')
    page = args.html.read_text(encoding='utf-8')
    pattern = r'(<script type="application/json" id="embedded-data">)(.*?)(</script>)'
    new_page, count = re.subn(pattern, lambda match: match.group(1) + safe_json + match.group(3), page, count=1, flags=re.S)
    if count != 1:
        parser.error('Could not find the embedded-data script in the target HTML.')
    args.html.write_text(new_page, encoding='utf-8')
    print(f'Updated {args.html}: {len(rows):,} records, {len(headers)} columns from {args.csv_file.name}')


if __name__ == '__main__':
    main()
