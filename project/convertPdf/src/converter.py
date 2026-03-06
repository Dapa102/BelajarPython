from docx2pdf import convert
import os
import platform
import shutil
import subprocess

def docx_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        print("❌ File DOCX tidak ditemukan!")
        return

    system = platform.system().lower()

    # docx2pdf only works on Windows/macOS with MS Word; on Linux use LibreOffice.
    if system == "linux":
        libreoffice = shutil.which("libreoffice") or shutil.which("soffice")
        if not libreoffice:
            print("❌ LibreOffice tidak ditemukan. Install dulu (mis. sudo apt install libreoffice).")
            return

        output_dir = os.path.dirname(os.path.abspath(output_path)) or os.getcwd()
        os.makedirs(output_dir, exist_ok=True)

        try:
            subprocess.run(
                [libreoffice, "--headless", "--convert-to", "pdf", "--outdir", output_dir, os.path.abspath(input_path)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            print("✅ Convert berhasil (LibreOffice)!")
        except subprocess.CalledProcessError as exc:
            print("❌ Gagal convert via LibreOffice:", exc)
        return

    # Default path (Windows/macOS with Word installed)
    convert(input_path, output_path)
    print("✅ Convert berhasil!")

