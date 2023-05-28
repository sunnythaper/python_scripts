def format_header(domain):
    return f"\n#############################################\n## {domain}\n#############################################\n\n"

def format_entity_status(entity, status, attributes):
    if status is None:
        logger.warning(f"Entity '{entity}' not found.")
        return f"# Entity '{entity}' not found.\n"
    attribute_texts = [f"  {attribute}: {str(status.attributes.get(attribute))}\n"
                       for attribute in attributes if status.attributes.get(attribute)]
    return f"{entity}:\n  state: {status.state}\n" + "".join(attribute_texts) + "\n"

def process_entities(entities, attributes):
    text_lines = []
    for entity_id in entities:
        entity_status = hass.states.get(entity_id)
        text_lines.append(format_entity_status(entity_id, entity_status, attributes))
    return "".join(text_lines)

def process_domain(domain, attributes):
    entities = hass.states.entity_ids(domain)
    if not entities:
        logger.warning(f"Domain '{domain}' not found or has no entities.")
        return f"# Domain '{domain}' not found or has no entities.\n"
    text_lines = [format_header(domain)]
    text_lines.append(process_entities(entities, attributes))
    return "".join(text_lines)

def process_domains(domains, attributes):
    if not domains:
        return ""
    return "".join(process_domain(domain, attributes) for domain in domains)

def process_input(domains, entities, attributes):
    if entities:
        return process_entities(entities, attributes)
    else:
        return process_domains(domains, attributes)

def export_results(text, save_file):
    if save_file:
        try:
            hass.services.call("notify", "scene_generator", {"message": "{}".format(text)})
        except Exception as e:
            logger.error(f"Failed to call 'notify.scene_generator' service: {str(e)}")
    else:
        logger.warning(text)

domains = data.get('domains', ['light','switch','fan'])
entities = data.get('entities')
attributes = data.get('attributes', ['brightness','color_temp','xy_color','rgb_color'])
save_file = data.get('save_file')

text = process_input(domains, entities, attributes)
export_results(text, save_file)
