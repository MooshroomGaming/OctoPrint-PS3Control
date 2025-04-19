import octoprint.plugin
import inputs
from threading import Thread

class PS3ControlPlugin(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):

    def __init__(self):
        self._controller_thread = None
        self._running = False

    def on_after_startup(self):
        self._start_controller()

    def _start_controller(self):
        self._running = True
        self._controller_thread = Thread(target=self._control_loop)
        self._controller_thread.start()

    def _control_loop(self):
        while self._running:
            try:
                events = inputs.get_gamepad()
                for event in events:
                    if event.code == "BTN_START" and event.state == 1:
                        self._printer.commands("M112")  # Emergency stop
                    elif event.code == "BTN_SOUTH":
                        self._printer.commands("G91\nG1 E2 F100")  # Extrude
                    # Add more button mappings here
            except:
                pass

    def get_template_configs(self):
        return [dict(type="settings", custom_bindings=False)]

__plugin_name__ = "PS3 Control"
__plugin_pythoncompat__ = ">=3.7,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PS3ControlPlugin()
