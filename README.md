# just_config
Minimalistic library to handle configuration for the application.

As for now, it will look for the configuration value in the following order:
  1.  In system environment variables.
  2.  In `default.ini` file in the current working directory
  3.  In `default.ini` file in application-specific folder under user home directory
  
## Usage:
```python
>>> from just_config.configuration import Configuration
>>> cfg = Configuration()
>>> cfg['test']
'value'
>>> # If I store my configuration in ~/.app/default.ini
>>> cfg = Configuration('app')
>>> cfg['test']
'value'
```

## Example configuration file:
```ini
[DEFAULT]
test=value
```

![](https://img.shields.io/pypi/dm/just-config.svg)

