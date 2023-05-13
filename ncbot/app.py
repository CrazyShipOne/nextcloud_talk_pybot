from config import Config
import poll_runner as runner
import ncbot.command.commander as commander

conf = Config()

def start():
    conf.checkEnv()
    commander.load_plugin(commander.plugin_path)
    runner.start()
