
def split_on_strikethrough(text):
    _split = text.split('~~')
    return _split

def loop(part_ii):
    for clause in part_ii:
        # Add each clause content (level 2)
        for content in clause['contents']:
            # Add subtopics (level 3)
            _split = split_on_strikethrough(content['content'])
            if len(_split) > 1:
                for i, chunk in enumerate(_split):
                    print(i, chunk)

            for subtopic in content['subtopics']:
                _split = split_on_strikethrough(subtopic)
                print(_split)

if __name__ == "__main__":
    import json
    from parse_flat_history import parse_flat_history
    with open('full_flat_history.json', 'r') as f:
        flat_history = json.load(f)
    parsed_flat_history = parse_flat_history(flat_history)
    part_ii = parsed_flat_history['part_ii']
    loop(part_ii)