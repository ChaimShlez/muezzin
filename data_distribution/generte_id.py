import hashlib



def generate_id_from_data(item):
    time = item['Creation time']
    name = item['Name']
    combined_string = f"{name}-{time}"
    podcast_id = hashlib.sha256(combined_string.encode()).hexdigest()
    return podcast_id[:8]








