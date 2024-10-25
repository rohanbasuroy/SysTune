# option_evaluator.py

import json

class OptionEvaluator:
    def __init__(self, safety_enforcer):
        self.safety_enforcer = safety_enforcer

    def evaluate(self, llm_response):
        try:
            response_json = json.loads(llm_response)
            app_params = response_json.get('app_params', {})
            system_params = response_json.get('system_params', {})

            # Check if parameters are safe
            if not self.safety_enforcer.is_safe(app_params, system_params):
                print("Suggested parameters are not safe.")
                return None

            return {
                'app_params': app_params,
                'system_params': system_params
            }
        except json.JSONDecodeError:
            print("Failed to parse LLM response.")
            return None
