import csv
import pandas
from pathlib import Path

# this will help you to read top rows
def get_top_rows(file_path: Path, num_rows: int = 5):
    """
    Reads a CSV file and returns the header and top N rows.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        rows = []
        for i, row in enumerate(reader):
            if i >= num_rows:
                break
            rows.append(row)

    return header, rows


def display_table(header, rows):
    """
    Nicely formats and prints tabular data in the console.
    """
    if not header and not rows:
        print("No data available.")
        return

    # Calculate column widths
    columns = [header] + rows if header else rows
    col_widths = [
        max(len(str(item)) for item in col)
        for col in zip(*columns)
    ]

    # Helper for formatting rows
    def format_row(row):
        return " | ".join(f"{str(val):<{w}}" for val, w in zip(row, col_widths))

    separator = "-+-".join("-" * w for w in col_widths)

    if header:
        print(format_row(header))
        print(separator)

    for row in rows:
        print(format_row(row))


def main():
    # Resolve the path to data/employee.csv relative to this script
    base_dir = Path(__file__).resolve().parent.parent
    csv_file_path = base_dir / "data" / "employee.csv"

    print(f"Reading from: {csv_file_path}\n")
    print("Top 5 Rows:")
    print("=" * 60)

    header, top_rows = get_top_rows(csv_file_path, num_rows=5)
    display_table(header, top_rows)


if __name__ == "__main__":
    main()

