# prompt_generator.py

import json

class PromptGenerator:
    def __init__(self, app_params, system_params):
        self.app_params = app_params
        self.system_params = system_params

    def generate_prompt(self, previous_params, previous_performance):
        prompt = (
            "You are an expert system tuner. Based on the previous FFmpeg parameters and performance metrics, "
            "suggest new parameter values to optimize performance.\n\n"
            f"Previous Application Parameters:\n{json.dumps(previous_params.get('app_params', {}), indent=2)}\n"
            f"Previous System Parameters:\n{json.dumps(previous_params.get('system_params', {}), indent=2)}\n"
            f"Previous Performance:\n{json.dumps(previous_performance, indent=2)}\n\n"
            "Available Application Parameters to Tune:\n"
            f"{json.dumps(self.app_params, indent=2)}\n\n"
            "Available System Parameters to Tune:\n"
            f"{json.dumps(self.system_params, indent=2)}\n\n"
            "Please provide new parameter values in the following JSON format:\n"
            "{\n"
            "  \"app_params\": {\n"
            "    \"compiler_flags\": [\"-O2\", \"-funroll-loops\", ...]\n"
            "  },\n"
            "  \"system_params\": {\n"
            "    \"vm.swappiness\": 10,\n"
            "    \"kernel.sched_latency_ns\": 20000000,\n"
            "    ...\n"
            "  }\n"
            "}\n"
            "Only include parameters from the lists provided, and ensure values are from the available options."
        )
        return prompt
