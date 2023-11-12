/*
 * View model for OctoPrint-DebugEnabled
 *
 * Author: jneilliii
 * License: AGPLv3
 */
$(function() {
    function Debug_enabledViewModel(parameters) {
        var self = this;

        self.logViewModel = parameters[0];
        self.debug_message = ko.observableDictionary();
        
        self.debug_logging_enabled =  ko.computed(function() {
            var debug_enabled = null;
            debug_enabled = ko.utils.arrayFirst(self.logViewModel.configuredLoggers(), function(item) {
                return item.component == "octoprint.plugins.debug_enabled" && item.level() == "DEBUG";
            });
            if (debug_enabled == null)
                return false;
            return true;
        })
        
        self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "debug_enabled") {
                return;
            }

            self.debug_message.removeAll();
            self.debug_message.pushAll(data);
        }
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: Debug_enabledViewModel,
        dependencies: [ "logsViewModel" /* "loginStateViewModel", "settingsViewModel" */ ],
        elements: [ "#tab_plugin_debug_enabled_link", "#tab_plugin_debug_enabled" ]
    });
});
