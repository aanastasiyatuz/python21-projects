def get_obj_or_404(model, attr, val):
    found = False

    for obj in model.objects:
        obj_val = getattr(obj, attr)
        if obj_val == val:
            found = True
            break

    if not found:
        raise Exception(f"404 {model.__name__}  Not Found")
    
    return obj
