#!/usr/bin/python3

# This is how a configuration setup can look like. The key will form a herarchical key in Config object.
# The values will be taken from environment variables. They should be case insensitive (only the leaf values should be case sensitive). All lists will be flattened.
# If the value is not found then the default value can be found after the semicolon.

import cf_config

config_fields = {
  'foo': {
    'bar': 'VCAP_SERVICES.user_management.url:default_url',
    'spam': 'VCAP_SERVICES.user_management.url:something'
  },
  'ham': 'VCAP_PORT:5000'
}

app_cfg = cf_config.get_config(config_fields)

# This will hold the value of VCAP_SERVICES['user_management'][0]['url']
# Or it can be also taken from user-provided services
x = app_cfg.foo.bar 
