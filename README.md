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
