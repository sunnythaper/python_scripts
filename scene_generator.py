# Pass the following:
#
# {
#     "domain": "light",
#     "attributes": ["brightness, color_temp, xy_color, rgb_color"]
# }


domain = data.get('domain')
attributes = data.get('attributes')

# DEBUGGING
text = "\n\n"
text = text + "DEBUG: domain - {} \n".format(domain)
text = text + "DEBUG: attributes - {} \n".format(attributes)

# PRINT NICELY FORMATTED HEADER
text = text + "\n\n"
text = text + "#############################################\n"
text = text + "## " + domain + "\n"
text = text + "#############################################\n\n"


entities = hass.states.entity_ids(domain)

for i in entities:
    entity = ("%r" % i).strip("'")
    status = hass.states.get(entity)

    text = text + entity + ":\n"
    text = text + "  state: " + status.state + "\n"

    if status.state == 'on':
        for i in attributes:
            attributeState = ("%r" % i).strip("'")

            if status.attributes.get(attributeState):
                text = text + "  " + attributeState + ": " + str(status.attributes.get(attributeState)) + "\n"

    text = text + "\n"

logger.warning(text)
hass.bus.fire(text)
