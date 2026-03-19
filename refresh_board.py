# Refresh donor data from NCBO Airtable
from airtable import Airtable
import json
import yaml
from datetime import datetime
import pytz
import os

airtable_base_id = os.environ.get('AIRTABLE_BASE_ID')
airtable_api_key = os.environ.get('AIRTABLE_API_KEY')

if airtable_base_id is None or airtable_api_key is None:
    print(f"Environment variables are not set.")
    exit(1)

airtable = Airtable(airtable_base_id, 'Board', api_key=airtable_api_key)

records = airtable.get_all()
formatted_records = []

for record in records:
    new_rec = {}
    fields = record['fields']

    # Adding fields
    new_rec['boardmember'] = fields.get('Name', '')
    new_rec['position'] = fields.get('Position', '')
    

    formatted_records.append(new_rec)

yaml.dump(formatted_records, default_flow_style=False, allow_unicode=True, stream=open('_data/board.yml', 'w', encoding='utf-8'))
