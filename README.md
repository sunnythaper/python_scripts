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
    "attributes": "brightness, color_temp, xy_color, rgb_color"
}
```

**FUTURE ENHANCEMENTS**

1. Multiple domain service call support - get everything all at once
2. Notifier service tie in - no longer use the info tab
3. Possible hass.io add-on to autogenerate scene YAML files
