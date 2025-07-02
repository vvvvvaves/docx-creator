def get_title_page_model():
    return {
        "doc_title": "",
        "doc_subtitle": "",
        "date": "",
        "header": "",
        "footer": "",
        "additional_info": ""
    }

def get_preamble_model():
    return {
        "place": {
            "query": "Place:",
            "answer": "",
            "answer_type": ""
        },
        "date": {
            "query": "Date:",
            "answer": "",
            "answer_type": ""
        },
    "owner": {
        "query": "IT IS THIS DAY AGREED between",
        "answer": "",
        "answer_type": ""
    },
    "of_the": {
        "query": "chartered owner/owner (hereinafter called the \"Owner\") of the ",
        "answer": "",
        "answer_type": ""
    },
    "vessel name": {
        "query": "SS/MS",
        "answer": "",
        "answer_type": "(hereinafter called the \"Vessel\")"
    },
    "charterer": {
        "query": "and",
        "answer": "",
        "answer_type": "(hereinafter called the \"Charterer\")"
    },
    "that_the": {
        "query": "",
        "answer": " that the transportation herein provided for will be performed subject to the terms and conditions of this Charter Party, which includes this Preamble and Part I and Part II. In the event of a conflict, the provisions of Part I will prevail over those contained in Part II.",
        "answer_type": ""
    }
    }

def get_part_i_model():
    return {
    "description_of_the_vessel": {
        "query": "A. Description and Position of Vessel:",
        "answer": "",
        "answer_type": ""
    },
    "deadweight": {
        "query": "Deadweight:",
        "answer": "",
        "answer_type": "tons (2240 lbs.)"
    },
    "classed": {
        "query": "Classed:",
        "answer": "",
        "answer_type": ""
    },
    "loaded_draft": {
        "query": "Loaded draft of Vessel on assigned summer freeboard",
        "answer": "",
        "answer_type": "ft."
    },
    "salt_water_draft": {
        "query": "",
        "answer": "",
        "answer_type": "in. in salt water."
    },
    "capacity_for_cargo": {
        "query": "Capacity for cargo:",
        "answer": "",
        "answer_type": "tons (of 2240 lbs. each)"
    },
    "more_or_less_percentage": {
        "query": "",
        "answer": "",
        "answer_type": "% more or less, Vessel's option."
    },
    "coated": {
        "query": "Coated:",
        "answer": "",
        "answer_type": ""
    },
    "coiled": {
        "query": "Coiled:",
        "answer": "",
        "answer_type": ""
    },
    "last_two_cargoes": {
        "query": "Last two cargoes:",
        "answer": "",
        "answer_type": ""
    },
    "now_date": {
        "query": "Now:",
        "answer": "",
        "answer_type": ""
    },
    "expected_ready_date": {
        "query": "Expected Ready:",
        "answer": "",
        "answer_type": ""
    },
    "laydays": {
        "query": "B. Laydays:",
        "answer": "",
        "answer_type": ""
    },
    "commencing_date": {
        "query": "Comencing:",
        "answer": "",
        "answer_type": ""
    },
    "cancelling_date": {
        "query": "Cancelling:",
        "answer": "",
        "answer_type": ""
    },
    "loading_port": {
        "query": "C. Loading Port(s):",
        "answer": "",
        "answer_type": ""
    },
    "discharge_port": {
        "query": "D. Discharging Port(s):",
        "answer": "",
        "answer_type": ""
    },
    "cargo_info": {
        "query": "E. Cargo:",
        "answer": "",
        "answer_type": ""
    },
    "freight_rate": {
        "query": "F. Freight Rate:",
        "answer": "",
        "answer_type": "per ton (of 2240 lbs. each)."
    },
    "freight_payable_to": {
        "query": "Freight Payable to:",
        "answer": "",
        "answer_type": ""
    },
    "freight_payable_at": {
        "query": "at",
        "answer": "",
        "answer_type": ""
    },
    "total_laytime_in_running_hours": {
        "query": "H. Total Laytime in Running Hours:",
        "answer": "",
        "answer_type": ""
    },
    "demurrage_per_day": {
        "query": "I. Demurrage per day:",
        "answer": "",
        "answer_type": ""
    },
    "commission_percentage": {
        "query": "J. Commission of",
        "answer": "",
        "answer_type": "%"
    },
    "commission_payable_to": {
        "query": "is payable by Owner to",
        "answer": "",
        "answer_type": "on the actual amount freight, when and as freight is paid."
    },
    "place_of__proceedings": {
        "query": "K. The place of General Average and arbitration proceedings to be",
        "answer": "",
        "answer_type": ""
    },
    "tovalop": {
        "query": "L. Tovalop:",
        "answer": "Owner warrants Vessel to be a member of TOVALOP scheme and will be so maintained throughout duration of this charter.",
        "answer_type": ""
    },
    "tovalop_cont": {
        "query": "",
        "answer": "",
        "answer_type": ""
    },
    "special_provisions": {
        "query": "M. Special Provisions:",
        "answer": "",
        "answer_type": ""
    },
    "in_witness": {
        "query": "",
        "answer": "IN WITNESS WHEREOF, the parties have caused this Charter, consisting of a Preamble, Parts I and II, to be executed in duplicate as of the day and year first above written.",
        "answer_type": ""
    },
    "witness_1": {
        "query": "Witness the signature of:",
        "answer": "",
        "answer_type": ""
    },
    "witness_1_by": {
        "query": "by",
        "answer": "",
        "answer_type": ""
    },
    "witness_2": {
        "query": " Witness the Signature of:",
        "answer": "",
        "answer_type": ""
    },
    "witness_2_by": {
        "query": "by",
        "answer": "",
        "answer_type": ""
    },
    "note": {
        "query": "",
        "answer": "This Charterparty is a computer generated copy of ASBATANKVOY form, printed under licence from the Association of Ship Brokers & Agents (U.S.A.), Inc., using software which is the copyright of Strategic Software Limited. It is a precise copy of the original document which can be modified, amended or added to only by the striking out of original characters, or the insertion of new characters, such characters being clearly highlighted as having been made by the licensee or end user as appropriate and not by the author.",
        "answer_type": ""
    },
    "additional_info_about_the_vessel": {
        "query": "Additional information about the vessel:",
        "answer": "",
        "answer_type": ""
    }
}
    

def find_by_id(flat_history, id):
    messages = flat_history['messages']
    return [message for message in messages if id in message['id']]

def parse_title_page(flat_history):
    import json
    title_page_data = json.loads(find_by_id(flat_history, 'Name+Header+footer')[0]['content'])

    title_page_model = get_title_page_model()
    title_page_model['doc_title'] = title_page_data['charter_party_name']
    title_page_model['doc_subtitle'] = 'Voyage Charter Party'
    title_page_model['date'] = title_page_data['charter_party_date']
    title_page_model['header'] = f"{title_page_data['charter_party_name']} – Voyage Charter Party"
    title_page_model['footer'] = f"{title_page_data['company_issues_charter_party']} – {title_page_data['charter_party_date']}"
    
    return title_page_model

def parse_preamble(flat_history):
    import json

    preamble_data = json.loads(find_by_id(flat_history, 'Preamble')[0]['content'])
    preamble_model = get_preamble_model()
    for key, value in preamble_data.items():
        if key in preamble_model:
            preamble_model[key]['answer'] = value
        else:
            print(f"WARNING: Key not found in preamble_model: {key}")

    parsed_preamble_data = []
    for key, value in preamble_model.items():
        parsed_preamble_data.append({
            "query": value.get('query', ''),
            "answer": value.get('answer', ''),
            "answer_type": value.get('answer_type', '')
        })
    return parsed_preamble_data

def parse_part_i(flat_history):
    import json

    part_i_data = find_by_id(flat_history, 'Part_1')
    part_i_data = [json.loads(data_point['content']) for data_point in part_i_data]

    part_i_model = get_part_i_model()

    merged_part_i_data = {}
    for data_point in part_i_data:
        for key, value in data_point.items():
            if key not in merged_part_i_data:
                merged_part_i_data[key] = value
            else:
                print(f"WARNING: Duplicate key: {key}")

    for key, value in merged_part_i_data.items():
        if key in part_i_model:
            part_i_model[key]['answer'] = value
        else:
            print(f"WARNING: Key not found in part_i_model: {key}")

    parsed_part_i_data = []
    for key, value in part_i_model.items():
        parsed_part_i_data.append({
            "query": value.get('query', ''),
            "answer": value.get('answer', ''),
            "answer_type": value.get('answer_type', '')
        })

    return parsed_part_i_data

def parse_part_ii(flat_history):
    import json
    part_ii_data = find_by_id(flat_history, 'Part_2')
    # part_ii_data += find_by_id(flat_history, 'Rewrite documents')
    part_ii_data = [json.loads(data_point['content'])['topics_data'] for data_point in part_ii_data]
    merged_part_ii_data = []
    for data_point in part_ii_data:
        merged_part_ii_data += data_point

    for i in range(len(merged_part_ii_data)):
        merged_part_ii_data[i]['number'] = i + 1

    return merged_part_ii_data

def parse_part_iii(flat_history):
    import json

    part_iii_data = find_by_id(flat_history, 'Rewrite documents')
    part_iii_data = [json.loads(data_point['content'])['topics_data'] for data_point in part_iii_data]
    merged_part_iii_data = []
    for data_point in part_iii_data:
        merged_part_iii_data += data_point

    return merged_part_iii_data

def parse_flat_history(flat_history):
    title_page_model = parse_title_page(flat_history)
    preamble_model = parse_preamble(flat_history)
    part_i_model = parse_part_i(flat_history)
    part_ii_model = parse_part_ii(flat_history)
    part_iii_model = parse_part_iii(flat_history)

    return {
        'title_page': title_page_model,
        'preamble': preamble_model,
        'part_i': part_i_model,
        'part_ii': part_ii_model,
        'part_iii': part_iii_model
    }

if __name__ == "__main__":
    import json
    with open('full_flat_history.json', 'r') as f:
        flat_history = json.load(f)
    parsed_flat_history = parse_flat_history(flat_history)
    part_ii = parsed_flat_history['part_ii']
   
    part_ii = sorted(part_ii, key=lambda x: x['number'])
    for clause in part_ii:
        print(clause['number'], clause['name'])
    

    
    # print(json.dumps(parsed_flat_history, indent=4))