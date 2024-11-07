
def attr_is_faceset(attr):
    if attr.is_internal:
        return False
    
    if attr.data_type != "BOOLEAN":
        return False
    
    return True