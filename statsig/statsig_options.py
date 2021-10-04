import json

class StatsigOptions:
    def __init__(self):
        self.api = "https://api.statsig.com/v1"
        self.environment = None

    def set_tier(self, tier):
        if tier is None or type(tier) != 'string':
            return
        self.set_environment_parameter("tier", tier.lower())
    
    def set_environment_parameter(self, key, value):
        if self.environment is None:
            self.environment = {}
        self.environment[key] = value

    def to_json_string(self):
        options_nullable = {
            'api': self.api,
            'environment': self.environment,
        }
        options = {}
        for key in options_nullable:
            if not options_nullable[key] is None:
                options[key] = options_nullable[key]
        return json.dumps(options)