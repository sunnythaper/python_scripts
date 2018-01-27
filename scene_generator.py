# Pass the following:
#
# {
#     "domains": ["light", "switch"],
#     "attributes": ["brightness", "color_temp", "xy_color", "rgb_color"],
#     "save_file": true
# }

# SETUP VARIABLES FROM HASS CALL
domains = data.get('domains')
attributes = data.get('attributes')
save_file = data.get('save_file')

# ACCOUNT FOR DEPRECIATED SETTINGS
if data.get('domain'):
    domains = [data.get('domain')]

# SET YAML RECEIVER VARIABLE
text = ""

# PROCESS EACH DOMAIN
for i in domains:

    # GET DOMAIN
    domain = ("%r" % i).strip("'")

    # PRINT NICELY FORMATTED HEADER
    text = text + "\n"
    text = text + "#############################################\n"
    text = text + "## " + domain + "\n"
    text = text + "#############################################\n\n"

    # FIND ALL ENTITIES BY DOMAIN
    entities = hass.states.entity_ids(domain)

    # GET ENTITY STATE & ATTRIBUTES
    for i in entities:

        # GET ENTITY DATA FROM HASS
        entity = ("%r" % i).strip("'")
        status = hass.states.get(entity)

        # ENTITY STATE
        text = text + entity + ":\n"
        text = text + "  state: " + status.state + "\n"

        # ENTITY ATTRIBUTES WHEN STATE IS ON
        if status.state == 'on':
            for i in attributes:

                # GET ATTRIBUTE BY JSON ARRAY PASSED BY HASS CALL
                attributeState = ("%r" % i).strip("'")

                # DISPLAY ATTRIBUTE IF NOT EMPTY
                if status.attributes.get(attributeState):
                    text = text + "  " + attributeState + ": " + str(status.attributes.get(attributeState)) + "\n"

        # GIVE THE PO DECLARATION SOME SPACE
        text = text + "\n"

if save_file:
    # SAVE SCENE CONFIGURATION TO FILE
    hass.services.call("notify", "scene_generator", {"message": "{}".format(text)})
else:
    # OUTPUT FORMATTED YAML TO LOG FILE
    logger.warning(text)
