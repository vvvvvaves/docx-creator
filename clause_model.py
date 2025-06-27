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

def save_clause_data_as_dict(data: ListOfClauses):
    import os

    file_name = "part_ii_clauses.json" 
    if os.path.exists(get_real_filename(file_name)):
        with file_lock:
            clauses = read_file(file_name)
    else:
        clauses = []

    clauses += data['clauses']
    
    with file_lock:
        save_file(file_name, clauses)

    print(f'Clause was saved into {get_real_filename(file_name)}')