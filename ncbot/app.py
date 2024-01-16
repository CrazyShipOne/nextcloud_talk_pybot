import ncbot.poll_runner as runner
import ncbot.command.commander as commander
import ncbot.config as ncconfig

def start():
    ncconfig.cf.checkEnv()
    commander.load_plugin(commander.plugin_path)
    runner.start()
