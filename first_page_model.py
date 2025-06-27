from pydantic import BaseModel, Field

class FirstPage(BaseModel):
    doc_title: str = Field(description = "Title of the document.")
    doc_subtitle: str = Field(description = "Subtitle of the document.")
    date: str = Field(description = "Date of the document. Contains month followed by a year.")
    header: str = Field(description = "Header of the document.")
    footer: str = Field(description = "Footer of the document.")

def save_first_page_data(data: FirstPage):
    file_name = "doc_data.json" 
    real_filename = get_real_filename(file_name)
    save_file(real_filename, data)
