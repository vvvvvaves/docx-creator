from docx import Document

def extract_style(doc):
    style = doc.styles['MyStyle']
    return style

if __name__ == "__main__":
    doc = Document("Clause Template.docx")
    style = extract_style(doc)
    print(style)