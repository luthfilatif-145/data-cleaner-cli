import json
import click
from typing import Any, Dict, List
from src.cleaner import clean_and_validate_row

@click.command()
@click.option('--file', '-f', required=True, type=click.Path(exists=True), help='Path ke file JSON data')
def process_data(file: str) -> None:
    """Membaca dan membersihkan data dari file JSON."""
    click.echo(f"Memproses file: {file}...\n")
    
    with open(file, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    cleaned_results: List[Dict[str, Any]] = []
    error_logs: List[Dict[str, Any]] = []

    for index, row in enumerate(data):
        cleaned_row, errors = clean_and_validate_row(row)
        if errors:
            error_logs.append({"baris": index + 1, "errors": errors})
        elif cleaned_row:
            cleaned_results.append(cleaned_row)

    click.echo(f"Status Selesai:")
    click.echo(f"- Data Valid  : {len(cleaned_results)}")
    click.echo(f"- Data Error  : {len(error_logs)}")

    if error_logs:
        click.echo("\nRincian Error:")
        for err in error_logs:
            click.echo(f" Baris {err['baris']}: {', '.join(err['errors'])}")

if __name__ == '__main__':
    process_data()