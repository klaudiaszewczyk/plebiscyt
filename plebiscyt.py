import os

from format_output import format_output

lists_dir_prefix = 'listy'
output_filename = 'suma.txt'
top_list = {}

if os.path.isfile(os.path.join(lists_dir_prefix, output_filename)):
    os.remove(os.path.join(lists_dir_prefix, output_filename))

for filename in os.listdir('listy'):
    with open(os.path.join(lists_dir_prefix, filename), 'r') as open_file:
        top_list_raw = open_file.readlines()

    # nazwa plyty - klucz
    # liczba punktow - wartosc

    for index, entry in enumerate(top_list_raw):
        disc_name = ' '.join(entry.split()[1:])

        points = 30 - index
        if disc_name in top_list:
            top_list[disc_name] += int(points)
        else:
            top_list[disc_name] = int(points)

with open(os.path.join(lists_dir_prefix, output_filename), 'w') as fp:
    fp.write(format_output(top_list))
