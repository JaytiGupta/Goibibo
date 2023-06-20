class Config:
    def __init__(self, env):

        self.base_url = {
            "dev": "dev-url",
            "qa": "qa-url",
        }[env]

