def serialise_list(objects):
    result = [obj.as_dict() for obj in objects]
    return result
