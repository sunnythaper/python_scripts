def format_header(domain):
    return f"\n#############################################\n## {domain}\n#############################################\n\n"

def format_entity_status(entity, status, attributes):
    attribute_texts = [f"  {attribute}: {str(status.attributes.get(attribute))}\n"
                       for attribute in attributes if status.attributes.get(attribute)]
    return f"{entity}:\n  state: {status.state}\n" + "".join(attribute_texts) + "\n"

def process_domain(domain, attributes):
    text_lines = [format_header(domain)]
    entities = hass.states.entity_ids(domain)
    for entity_id in entities:
        entity_status = hass.states.get(entity_id)
        text_lines.append(format_entity_status(entity_id, entity_status, attributes))
    return "".join(text_lines)

def process_domains(domains, attributes):
    return "".join(process_domain(domain, attributes) for domain in domains)

def export_results(text, save_file):
    if save_file:
        hass.services.call("notify", "scene_generator", {"message": "{}".format(text)})
    else:
        logger.info(text)

domains = data.get('domains', ['light','switch','fan'])
attributes = data.get('attributes', ['brightness','color_temp','xy_color','rgb_color'])
save_file = data.get('save_file')

text = process_domains(domains, attributes)
export_results(text, save_file)
