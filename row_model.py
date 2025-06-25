from pydantic import BaseModel, Field

class Row(BaseModel):
    query: str = Field(description="The query of the row")
    answer: str = Field(description="The answer of the row")
    answer_type: str = Field(description="The type of the answer")

class ListOfRows(BaseModel):
    rows: list[Row] = Field(description="The list of rows")