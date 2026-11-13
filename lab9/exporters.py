import csv
import json
from fpdf import FPDF


class Exporter:
    def export(self, data, file_path):
        """Método base que debe ser sobrescrito por las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class TXTExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("--- PRODUCT REPORT ---\n")
            for product in data:
                file.write(f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]}\n")
        print(f"TXT file generated at: {file_path}")


class CSVExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Price"])
            for product in data:
                writer.writerow(product)
        print(f"CSV file generated at: {file_path}")


class JSONExporter(Exporter):
    def export(self, data, file_path):
        products_list = []
        for product in data:
            products_list.append({
                "id": product[0],
                "name": product[1],
                "price": float(product[2])
            })
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(products_list, file, indent=4, ensure_ascii=False)
        print(f"JSON file generated at: {file_path}")


class PDFExporter(Exporter):
    def export(self, data, file_path):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Product Inventory Report", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        for product in data:
            line_text = f"ID: {product[0]} | Product: {product[1]} | Price: ${product[2]}"
            pdf.cell(200, 10, txt=line_text, ln=True)

        pdf.output(file_path)
        print(f"PDF file generated at: {file_path}")