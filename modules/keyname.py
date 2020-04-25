def keyname(**kwargs):
    
    # Make an empty list to put all the key words into
    key = []
    
    # Loop through all possible variables provided, and add to list if it exists. else, skip it
    for var in ['basin','period','loc','dep','vartype']:
        try:
            var = kwargs[var]
            key.append(str(var))
        except:
            continue

    key = '_'.join(key)
    return(key)