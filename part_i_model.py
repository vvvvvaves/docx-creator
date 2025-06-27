from pydantic import BaseModel, Field

class QueryModel(BaseModel):
    query: str = Field(description="The query to be answered by the model", allow_mutation=False)
    answer: str = Field(description="The answer to the query", allow_mutation=True)
    answer_type: str = Field(description="The type of answer to the query", allow_mutation=False)
    is_mutable: bool = Field(description="Whether the query is mutable", allow_mutation=False)

class PartIModel(BaseModel):
    description_of_the_vessel: QueryModel = Field(default=QueryModel(query="A. Description and Position of Vessel:", answer="", answer_type="", is_mutable=False), allow_mutation=False)
    deadweight_tonnage: QueryModel = QueryModel(query="Deadweight:", answer="", answer_type="tons (2240 lbs.)", is_mutable=True)
    classed: QueryModel = QueryModel(query="Classed:", answer="", answer_type="", is_mutable=True)
    loaded_draft: QueryModel = QueryModel(query="Loaded draft of Vessel on assigned summer freeboard", answer="", answer_type="ft.", is_mutable=True)
    loaded_draft_cont: QueryModel = QueryModel(query="", answer="", answer_type="in. in salt water.", is_mutable=True)
    capacity: QueryModel = QueryModel(query="Capacity for cargo:", answer="", answer_type="tons (of 2240 lbs. each)", is_mutable=True)
    capacity_cont: QueryModel = QueryModel(query="", answer="", answer_type="% more or less, Vessel's option.", is_mutable=True)
    coated: QueryModel = QueryModel(query="Coated:", answer="", answer_type="", is_mutable=True)
    coiled: QueryModel = QueryModel(query="Coiled:", answer="", answer_type="", is_mutable=True)
    last_two_cargoes: QueryModel = QueryModel(query="Last two cargoes:", answer="", answer_type="", is_mutable=True)
    now: QueryModel = QueryModel(query="Now:", answer="", answer_type="", is_mutable=True)
    expected_ready: QueryModel = QueryModel(query="Expected Ready:", answer="", answer_type="", is_mutable=True)
    
    laydays: QueryModel = Field(default=QueryModel(query="B. Laydays:", answer="", answer_type="", is_mutable=False), allow_mutation=False)
    commencing_laydays: QueryModel = QueryModel(query="Comencing:", answer="", answer_type="", is_mutable=True)
    cancelling_laydays: QueryModel = QueryModel(query="Cancelling:", answer="", answer_type="", is_mutable=True)

    loading_ports: QueryModel = QueryModel(query="C. Loading Port(s):", answer="", answer_type="", is_mutable=True)
    discharging_ports: QueryModel = QueryModel(query="D. Discharging Port(s):", answer="", answer_type="", is_mutable=True)
    cargo: QueryModel = QueryModel(query="E. Cargo:", answer="", answer_type="", is_mutable=True)
    freight_rate: QueryModel = QueryModel(query="F. Freight Rate:", answer="", answer_type="per ton (of 2240 lbs. each).", is_mutable=True)
    freight_payable_to: QueryModel = QueryModel(query="Freight Payable to:", answer="", answer_type="", is_mutable=True)
    freight_payable_at: QueryModel = QueryModel(query="at", answer="", answer_type="", is_mutable=True)
    total_laytime: QueryModel = QueryModel(query="H. Total Laytime in Running Hours:", answer="", answer_type="", is_mutable=True)
    demurrage_per_day: QueryModel = QueryModel(query="I. Demurrage per day:", answer="", answer_type="", is_mutable=True)
    commission_of_the_charterer: QueryModel = QueryModel(query="J. Commission of", answer="", answer_type="%", is_mutable=True)
    is_payable_by: QueryModel = QueryModel(query="is payable by Owner to", answer="", answer_type="on the actual amount freight, when and as freight is paid.", is_mutable=True)
    place_of_GA: QueryModel = QueryModel(query="K. The place of General Average and arbitration proceedings to be", answer="", answer_type="", is_mutable=True)
    tovalop: QueryModel = Field(default=QueryModel(query="L. Tovalop:", answer="Owner warrants Vessel to be a member of TOVALOP scheme and will be so maintained throughout duration of this charter.", answer_type="", is_mutable=False), allow_mutation=False)
    tovalop_cont: QueryModel = QueryModel(query="", answer="", answer_type="", is_mutable=True)
    special_provisions: QueryModel = Field(default=QueryModel(query="M. Special Provisions:", answer="", answer_type="", is_mutable=False), allow_mutation=False)
    in_witness: QueryModel = Field(default=QueryModel(query="", answer="IN WITNESS WHEREOF, the parties have caused this Charter, consisting of a Preamble, Parts I and II, to be executed in duplicate as of the day and year first above written.", answer_type="", is_mutable=False), allow_mutation=False)
    witness_1: QueryModel = QueryModel(query="Witness the signature of:", answer="", answer_type="", is_mutable=True)
    witness_1_by: QueryModel = QueryModel(query="by", answer="", answer_type="", is_mutable=True)
    witness_2: QueryModel = QueryModel(query=" Witness the Signature of:", answer="", answer_type="", is_mutable=True)
    witness_2_by: QueryModel = QueryModel(query="by", answer="", answer_type="", is_mutable=True)
    note: QueryModel = Field(default=QueryModel(query="", answer="This Charterparty is a computer generated copy of ASBATANKVOY form, printed under licence from the Association of Ship Brokers & Agents (U.S.A.), Inc., using software which is the copyright of Strategic Software Limited. It is a precise copy of the original document which can be modified, amended or added to only by the striking out of original characters, or the insertion of new characters, such characters being clearly highlighted as having been made by the licensee or end user as appropriate and not by the author.", answer_type="", is_mutable=False), allow_mutation=False)

def save_part_i_data_as_dict(data: PartIModel):

    list_of_rows = []
    empty_part_i_model = PartIModel().model_dump()
    for key, value in data.items():
        if empty_part_i_model[key]['is_mutable']:
            list_of_rows.append({
                "query": empty_part_i_model[key]['query'],
                "answer": value['answer'],
                "answer_type": empty_part_i_model[key]['answer_type'],
            })
        else:
            list_of_rows.append({
                "query": empty_part_i_model[key]['query'],
                "answer": empty_part_i_model[key]['answer'],
                "answer_type": empty_part_i_model[key]['answer_type'],
            })
    
    file_name = "part_i_rows.json" 
    save_file(file_name, list_of_rows)