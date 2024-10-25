# safety_enforcer.py

class SafetyEnforcer:
    def __init__(self, param_blacklist, app_params, system_params):
        self.param_blacklist = param_blacklist
        self.app_params = app_params
        self.system_params = system_params

    def is_safe(self, app_params, system_params):
        # Check app_params
        compiler_flags = app_params.get('compiler_flags', [])
        for flag in compiler_flags:
            if flag in self.param_blacklist:
                print(f"Compiler flag '{flag}' is blacklisted.")
                return False
            if flag not in self.app_params:
                print(f"Compiler flag '{flag}' is not in the list of available parameters.")
                return False

        # Check system_params
        for param, value in system_params.items():
            if param in self.param_blacklist:
                print(f"System parameter '{param}' is blacklisted.")
                return False
            if param not in self.system_params:
                print(f"System parameter '{param}' is not in the list of available parameters.")
                return False
            if value not in self.system_params[param]:
                print(f"Value '{value}' for system parameter '{param}' is not in the list of available values.")
                return False

        return True
