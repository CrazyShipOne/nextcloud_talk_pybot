from config import Config
import poll_runner as runner
import ncbot.command.commander as commander
import ncbot.config as ncconfig

def start():
    ncconfig.conf.checkEnv()
    commander.load_plugin(commander.plugin_path)
    runner.start()
