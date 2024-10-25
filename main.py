# main.py

import openai
import os
from prompt_generator import PromptGenerator
from option_evaluator import OptionEvaluator
from performance_analyzer import PerformanceAnalyzer
from safety_enforcer import SafetyEnforcer
import config

def main():
    openai.api_key = config.OPENAI_API_KEY or os.getenv('OPENAI_API_KEY')

    prompt_generator = PromptGenerator(config.APP_COMPILER_FLAGS, config.SYSTEM_PARAMS)
    safety_enforcer = SafetyEnforcer(config.PARAM_BLACKLIST, config.APP_COMPILER_FLAGS, config.SYSTEM_PARAMS)
    option_evaluator = OptionEvaluator(safety_enforcer)
    performance_analyzer = PerformanceAnalyzer()

    previous_params = {}
    previous_performance = {}
    best_performance = None
    best_params = None

    for iteration in range(config.MAX_ITERATIONS):
        print(f"Iteration {iteration + 1}")

        # Generate prompt
        prompt = prompt_generator.generate_prompt(previous_params, previous_performance)

        # Get response from LLM
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        llm_response = response.choices[0].message['content'].strip()

        # Evaluate options
        new_params = option_evaluator.evaluate(llm_response)
        if new_params is None:
            print("No valid parameters obtained. Stopping.")
            break

        # Analyze performance
        performance = performance_analyzer.analyze_performance(
            new_params['app_params'].get('compiler_flags', []),
            new_params['system_params']
        )

        if performance is None:
            print("Performance analysis failed. Stopping.")
            break

        # Compare performance
        if best_performance is None or performance['execution_time'] < best_performance['execution_time']:
            best_performance = performance
            best_params = new_params
            print(f"New best performance: {performance['execution_time']} seconds")
        else:
            print("No performance improvement.")
            break

        # Update previous parameters and performance
        previous_params = new_params
        previous_performance = performance

    print("Tuning completed.")
    print(f"Best performance: {best_performance}")
    print(f"Best parameters: {best_params}")

if __name__ == "__main__":
    main()
