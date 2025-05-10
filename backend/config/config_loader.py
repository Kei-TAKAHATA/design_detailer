import os
import yaml


def load_prompt_templates():
    config_path = os.getenv('PROMPT_TEMPLATE_PATH', 'config/prompt_templates.yaml')
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        raise
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        raise


PROMPT_TEMPLATES = load_prompt_templates()
