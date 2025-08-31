from .custom_logger import CustomLogger
# Initialize a global logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("prod_assistant")