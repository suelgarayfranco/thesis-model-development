import json
import csv

description_ids = []
annotations = []

with open('ner-annotations.json', 'r', encoding='utf-8') as nerfile:
    data: list = json.load(nerfile)
    if data and len(data) > 0:
        description_ids = [description['expr_id'] for description in data]

with open('ner-annotations.conll', 'r', encoding='utf-8') as nerfile:
    next(nerfile)
    sentences = nerfile.read().split('\n\n')
    for sentence in sentences:
        annotation = ''
        if '-X-' in sentence: 
            tokens = sentence.split('\n')
            for token in tokens:
                parts = token.split('-X-')
                word = parts[0].strip()
                entity = parts[1].split('_')[1].strip()
                annotation += f' {word} [{entity}]'

            annotation = annotation.strip()
            annotations.append(annotation)

curated_annotations = []
for id, annotation in zip(description_ids, annotations):
    curated_annotations.append({"expr_id":id, "labeled_text":annotation})

fields = ['expr_id', 'labeled_text']
filename = "labeled_descriptions.csv"

# writing to csv file 
with open(filename, 'w', encoding="utf-8") as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator='\n')

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(curated_annotations)