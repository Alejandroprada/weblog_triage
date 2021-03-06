import configparser
import os


def config_parser(section, key):
    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__)+"/weblog_triage.ini"))
        result = config.get(section, key)
        return result
    except config.NoOptionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")
    except config.NoSectionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")


def config_parser_section(section):
    parser = config = configparser.ConfigParser()
    try:
        parser.read(os.path.dirname(__file__)+"/weblog_triage.ini")
        result = dict(parser.items(section))
        return result
    except config.NoSectionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")


def get_attack_patterns(attack):
    config = configparser.ConfigParser()
    try:
        config.read(os.path.dirname(__file__)+"/attack_patterns.ini")
        result = dict(config.items(attack))
        return result
    except config.NoSectionError:
        raise Exception("There was a problem with configuration file. The key does not exist.")

