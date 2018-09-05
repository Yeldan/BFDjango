def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    return cigars >= 40 and cigars <= 60