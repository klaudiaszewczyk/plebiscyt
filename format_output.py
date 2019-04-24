def format_output(ranking):
    ranking = [{key: ranking[key]} for key in ranking.keys()]
    ranking = sorted(ranking, key=lambda x:list(x.values())[0], reverse=True)
    out_str = ''

    for place, entry in enumerate(ranking):
        disc_name = list(entry.keys())[0]
        points = str(entry[disc_name])
        out_str += str(place + 1) + '. '  + disc_name + ' ' + points + '\n'

    return out_str
