from converter import docx_to_pdf

print("=== DOCX to PDF Converter ===")

input_file = input("Masukkan path file DOCX (contoh: docs/contoh.docx): ")
output_file = input("Masukkan path file PDF (contoh: docs/contoh.pdf): ")

docx_to_pdf(input_file, output_file)
