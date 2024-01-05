# Refresh event data from NCBO Airtable
from airtable import Airtable
import json
import yaml
from datetime import datetime
import pytz
import os

airtable_base_id = os.environ.get('AIRTABLE_BASE_ID')
airtable_api_key = os.environ.get('AIRTABLE_API_KEY')

print(f"AIRTABLE_BASE_ID: {airtable_base_id}"  )
print(f"AIRTABLE_API_KEY: {airtable_api_key}"  )
if airtable_base_id is None or airtable_api_key is None:
    print(f"Environment variables are not set.")
    exit(1)

airtable = Airtable(airtable_base_id, 'Events', api_key=airtable_api_key)

records = airtable.get_all()
formatted_records = []

for record in records:
    new_rec = {}
    fields = record['fields']

    #Rename fields
    new_rec['heading'] = fields.get('EventName', '')

    # convert new_rec['DateTime'] to MM/DD/YYYY
    dt = fields.get('DateTime', '01/01/2100T00:00:00.000Z')
    if dt.split('T')[0] == '01/01/2100':
        continue

    utc_dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Set the timezone for the datetime object to UTC
    utc_dt = utc_dt.replace(tzinfo=pytz.utc)

    # Convert to New York time
    ny_tz = pytz.timezone("America/New_York")
    ny_dt = utc_dt.astimezone(ny_tz)

    new_rec['eventdate'] = ny_dt.strftime('%m/%d/%Y')
    new_rec['eventtime'] = ny_dt.strftime('%I:%M %p')
    new_rec['venue'] = fields.get('Venue', '')
    new_rec['description'] = fields.get('Event info', '')
    new_rec['address'] = fields.get('Address', '')
    if fields.get('MapURL', '') != '':
        new_rec['mapurl'] = fields.get('MapURL', '')
    if fields.get('TicketURL', '') != '':
        new_rec['ticketurl'] = fields.get('EventDetailsURL', '')
    if fields.get('EventImageURL', '') != '':
        new_rec['eventimageurl'] = fields.get('EventImageURL', '')
    if fields.get('EventDetailsURL', '') != '':
        new_rec['eventdetailsurl'] = fields.get('EventDetailsURL', '')

    formatted_records.append(new_rec)

# sort formatted_records by eventdate
formatted_records = sorted(formatted_records, key=lambda k: k['eventdate'])

yaml.dump(formatted_records, default_flow_style=False, allow_unicode=True, stream=open('_data/events.yml', 'w', encoding='utf-8'))