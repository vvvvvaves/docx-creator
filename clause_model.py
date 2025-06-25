from pydantic import BaseModel, Field

class ClauseContent(BaseModel):
    clause_content: str = Field(description="The contents of the clause")
    subclauses: list[str] = Field(description="The subclauses of the clause")

class Clause(BaseModel):
    clause_number: str = Field(description="The number of the clause")
    clause_title: str = Field(description="The title of the clause")
    clause_content: list[ClauseContent] = Field(description="The contents of the clause")

class ListOfClauses(BaseModel):
    clauses: list[Clause] = Field(description="The list of clauses")