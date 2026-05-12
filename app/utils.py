import hashlib


def create_edge_id(source, target, relation_id):
    return hashlib.md5(
        f"{source}_{target}_{relation_id}".encode()
    ).hexdigest()
