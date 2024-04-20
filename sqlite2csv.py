import argparse
import sqlite3
import csv


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='src', type=str, default=None)
    parser.add_argument('-t', dest='table', type=str, default="contents")
    parser.add_argument('-o', dest='output', type=str, default=None)

    args = parser.parse_args()

    with sqlite3.connect(args.src) as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {args.table}")
        rows = cursor.fetchall()

        cursor.execute(f"PRAGMA table_info({args.table})")
        columns = [[row[1] for row in cursor.fetchall()]]

        csv_filename = args.src + '.csv' if args.output is None else args.output

        with open(csv_filename, 'w', newline='') as csv_file:
            print(f"Saved: {csv_filename}")
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(columns)
            csv_writer.writerows(rows)
