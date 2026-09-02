# Import built-in CSV module for reading delimited files
import csv
# Import Path from pathlib for cross-platform file path manipulation
from pathlib import Path

#this is the test
def get_top_rows(file_path: Path, num_rows: int = 15):
    """
    Reads a CSV file and returns the header and top N rows.
    """
    # Check if the specified file exists before attempting to open it
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Open the CSV file in read mode with UTF-8 encoding
    with open(file_path, mode="r", encoding="utf-8", newline="") as f:
        # Create a CSV reader object to iterate over lines
        reader = csv.reader(f)
        
        # Read the first line as the column headers (or None if the file is empty)
        header = next(reader, None)
        
        # List to store the extracted rows
        rows = []
        
        # Iterate over the data rows and collect up to num_rows
        for i, row in enumerate(reader):
            # Stop once the desired number of rows is reached
            if i >= num_rows:
                break
            rows.append(row)

    # Return a tuple containing the header list and the list of row lists
    return header, rows


def display_table(header, rows):
    """
    Nicely formats and prints tabular data in the console.
    """
    # If there is neither header nor rows, nothing to display
    if not header and not rows:
        print("No data available.")
        return

    # Combine header and rows to compute maximum width for each column
    columns = [header] + rows if header else rows
    
    # Determine the maximum character length for each column across all rows
    col_widths = [
        max(len(str(item)) for item in col)
        for col in zip(*columns)
    ]

    # Helper function to pad values to column width and join with pipe separator
    def format_row(row):
        return " | ".join(f"{str(val):<{w}}" for val, w in zip(row, col_widths))

    # Construct a horizontal separator line matching column widths
    separator = "-+-".join("-" * w for w in col_widths)

    # Print the header row followed by the divider line if header exists
    if header:
        print(format_row(header))
        print(separator)

    # Print each data row formatted according to column widths
    for row in rows:
        print(format_row(row))


def main():
    # Determine the project root directory relative to the current script file
    base_dir = Path(__file__).resolve().parent.parent
    
    # Construct the full path to data/employee.csv
    csv_file_path = base_dir / "data" / "employee.csv"

    # Display informative message about the file being read
    print(f"Reading from: {csv_file_path}\n")
    print("Top 5 Rows:")
    print("=" * 60)

    # Fetch the header and the first 5 records from the CSV
    header, top_rows = get_top_rows(csv_file_path, num_rows=5)
    
    # Print the fetched records in a formatted table
    display_table(header, top_rows)


# Standard Python boilerplate to execute main() when run as a script
if __name__ == "__main__":
    main()
