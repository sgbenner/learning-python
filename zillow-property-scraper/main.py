import os
from ZillowProperties import ZillowProperties
from googleform import GoogleForm

# get properties
properties_for_rent = ZillowProperties().properties_for_rent

for prop in properties_for_rent:
    form = GoogleForm(link_to_property=prop["link"], address=prop["address"], price_per_month=prop["price"])

    form.upload()
