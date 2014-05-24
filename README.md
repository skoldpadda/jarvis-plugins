# jarvis-plugins

A collection of plugins for [jarvis](https://github.com/willyg302/jarvis).

## Writing

To be discoverable by jpm, a plugin must have an entry in the `registry.json`. An entry has the following format:

```json
{
    "name": "coolplugin",
    "description": "This plugin does awesome things yo!",
    "source": "https://raw.githubusercontent.com/joe/my-cool-repo/master/coolplugin.py",
    "tags": ["cool", "rad", "bacon"]
}
```

If `source` is omitted, the plugin is assumed to be in the `src/` directory of this repo. Tags is likewise optional.