# python_scripts

## scene_generator.py

![scene generator walkthrough](https://github.com/sunnythaper/python_scripts/raw/master/readme-assets/scene_generator.gif)

This script allows you to export your current states/attributes into the YAML format for HASS Scenes!

1. Set your devices to how you want them
2. Call the scene_generator service with your JSON settings
3. Go to the info tab to copy/paste the result

**EXAMPLE JSON**

```js
{
    "domain": "light",
    "attributes": ["brightness", "color_temp", "xy_color", "rgb_color"],
    "save_file": true
}
```

**FILE SAVING**

If you would like scene_generator.py to save directly to a file in the HASS configuration directory, simply add a file notification declaration exactly as below. Currently the name is referenced by the script directly so do not change the name. You may change the filename to whatever you wish, however.

```yaml
notify:
  - name: scene_generator
    platform: file
    filename: generated_scene.yaml
    timestamp: false
```

**FUTURE ENHANCEMENTS**

1. Multiple domain service call support - get everything all at once
2. Notifier service tie in - no longer use the info tab
3. Possible hass.io add-on to autogenerate scene YAML files
