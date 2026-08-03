from services.document_processor import DocumentProcessor

processor = DocumentProcessor()

result = processor.process("uploaded_reports/report1.pdf")

print(result)