# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin


class Debug_enabledPlugin(octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.EventHandlerPlugin
):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            # put your plugin's default settings here
        }

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/ko.observableDictionary.js", "js/debug_enabled.js"]
        }

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        return [{'type': "tab", 'name': 'Debug Enabled', 'custom_bindings': True, 'data_bind': "visible: debug_logging_enabled()", 'template': "debug_enabled_tab.jinja2"}]

    ##~~ EventHandlerPlugin mixin

    def on_event(self, event, payload):
        if event == "UserLoggedIn":
            self._plugin_manager.send_plugin_message(self._identifier, payload)

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "debug_enabled": {
                "displayName": "Debug Enabled",
                "displayVersion": self._plugin_version,
                "type": "github_release",
                "user": "jneilliii",
                "repo": "OctoPrint-DebugEnabled",
                "current": self._plugin_version,
                "pip": "https://github.com/jneilliii/OctoPrint-DebugEnabled/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "Debug Enabled"
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Debug_enabledPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
