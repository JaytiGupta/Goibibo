class AppConfig:
    def __init__(self, available_env):
        self._env = ""
        self._take_screenshot = False
        self.available_env = available_env

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        if value not in self.available_env:
            raise ValueError(f"Invalid 'env' value. Allowed values are {', '.join(self.available_env)}.")
        self._env = value

    @property
    def take_screenshot(self):
        return self._take_screenshot

    @take_screenshot.setter
    def take_screenshot(self, value):
        if not isinstance(value, bool):
            raise ValueError("Invalid value for 'take_screenshot'. It should be a boolean.")
        self._take_screenshot = value
