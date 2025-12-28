import os
import re
import sqlite3
import pdfplumber

# Ruta de los PDFs
PDF_FOLDER = "bills"

# Expresión regular del CUFE
CUFE_REGEX = re.compile(r"(\b([0-9a-fA-F]\n*){95,100}\b)")

# Base de datos SQLite
DB_NAME = "info_data.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            pages INTEGER,
            cufe TEXT,
            file_size INTEGER
        )
    """)
    conn.commit()
    conn.close()


def extract_cufe_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = len(pdf.pages)
        first_page_text = pdf.pages[0].extract_text() or ""

        match = CUFE_REGEX.search(first_page_text)
        cufe = match.group(0).replace("\n", "") if match else None

    return pages, cufe


def save_to_db(file_name, pages, cufe, file_size):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO info (file_name, pages, cufe, file_size)
        VALUES (?, ?, ?, ?)
    """, (file_name, pages, cufe, file_size))
    conn.commit()
    conn.close()


def main():
    create_database()

    for file in os.listdir(PDF_FOLDER):
        if file.lower().endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER, file)
            file_size = os.path.getsize(file_path)

            pages, cufe = extract_cufe_from_pdf(file_path)
            save_to_db(file, pages, cufe, file_size)

            print(f"Procesado: {file}")


if __name__ == "__main__":
    main()
