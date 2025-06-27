from pydantic import BaseModel, Field

class QueryModel(BaseModel):
    query: str = Field(description="The query to be answered by the model", allow_mutation=False)
    answer: str = Field(description="The answer to the query", allow_mutation=True)
    answer_type: str = Field(description="The type of answer to the query", allow_mutation=False)
    is_mutable: bool = Field(description="Whether the query is mutable", allow_mutation=False)

class PreambleModel(BaseModel):
    it_is_this_day: QueryModel = QueryModel(query="IT IS THIS DAY AGREED between", answer="", answer_type="", is_mutable=True)
    owner_of_the: QueryModel = QueryModel(query="'chartered owner/owner (hereinafter called the \"Owner\") of the '", answer="", answer_type="", is_mutable=True)
    vessel: QueryModel = QueryModel(query="SS/MS", answer="", answer_type="(hereinafter called the \"Vessel\")", is_mutable=True)
    charterer: QueryModel = QueryModel(query="and", answer="", answer_type="(hereinafter called the \"Charterer\")", is_mutable=True)
    that_the: QueryModel = Field(default=QueryModel(query="", answer=" that the transportation herein provided for will be performed subject to the terms and conditions of this Charter Party, which includes this Preamble and Part I and Part II. In the event of a conflict, the provisions of Part I will prevail over those contained in Part II.", answer_type="", is_mutable=False), allow_mutation=False)

def save_preamble_data_as_dict(data: PreambleModel):

    list_of_rows = []
    empty_preamble_model = PreambleModel().model_dump()
    for key, value in data.items():
        if empty_preamble_model[key]['is_mutable']:
            list_of_rows.append({
                "query": empty_preamble_model[key]['query'],
                "answer": value['answer'],
                "answer_type": empty_preamble_model[key]['answer_type'],
            })
        else:
            list_of_rows.append({
                "query": empty_preamble_model[key]['query'],
                "answer": empty_preamble_model[key]['answer'],
                "answer_type": empty_preamble_model[key]['answer_type'],
            })
    
    file_name = "preamble_rows.json" 
    save_file(file_name, list_of_rows)