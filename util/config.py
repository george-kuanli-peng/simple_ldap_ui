import configparser


__config = None


def init_config(path):
    global __config

    __config = configparser.ConfigParser()
    __config.read(path)


def get_config(path=None):
    """Gets configuration

    First attempts to read configuration cache, or reads configuration from `path`

    Args:
        path (str): configuration file path, only used on configuration cache miss
    Returns:
        configparser.ConfigParser: configuration object
    """
    global __config

    if __config:
        return __config

    init_config(path)
    return __config
