# python_scripts

This repository contains Python scripts that can be used with the Home Assistant automation platform. Each script provides a unique functionality to extend the capabilities of your Home Assistant setup.

## scene_generator.py

### DEMO

![scene generator walkthrough](https://github.com/sunnythaper/python_scripts/raw/master/readme-assets/scene_generator.gif)

### OVERVIEW

The `scene_generator.py` script allows you to export your current entity states and attributes into the YAML format for Home Assistant Scenes. This is a powerful tool for creating scenes based on your current device configurations.

Here's how it works:

1. Set individual lights, fans, switches, covers, etc. to your desired state for the scene.
2. Call the `scene_generator` service with your custom service data, or leave it blank for default settings.
3. If you set `save_file` to false, go to the Home Assistant logs to copy the generated YAML for the scene.
4. If you set `save_file` to true, go to your configuration folder and open `generated_scene.yaml`.

### EXAMPLE SERVICE DATA

![example service call](https://github.com/sunnythaper/python_scripts/raw/master/readme-assets/service_call.png)

```yaml
domains:
  - light
  - switch
  - fan
attributes:
  - brightness
  - color_temp
  - xy_color
  - rgb_color
save_file: true
```

In this example, we're generating a scene for all light, switch, and fan entities, and including brightness, color temperature, and color attributes.

### FILE SAVING

If you would like `scene_generator.py` to save the generated scene directly to a file in the Home Assistant configuration directory, you'll need to set up a file notification in your Home Assistant configuration. Here's an example of how to do that:

```yaml
notify:
  - name: scene_generator
    platform: file
    filename: generated_scene.yaml
    timestamp: false
```

In this configuration, the generated scene will be saved to a file named `generated_scene.yaml` in your Home Assistant configuration directory. The `timestamp` option is set to false, meaning that timestamps will not be included in the generated file.
