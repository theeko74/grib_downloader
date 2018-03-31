#!/usr/bin/env python3

import os
import wx

from weather_models.arome import Arome
from weather_models.arpege import Arpege
from weather_models.openwrf import OpenWrf

from gui.gui_layout import mainFrame


def main():
    """
    Main function to run wxWidgets window
    and keep infinite loop.
    """
    app = wx.App(False)
    frame = gribApp(None)
    frame.Show(True)
    app.MainLoop()



class gribApp(mainFrame):

    def __init__(self, parent):
        super().__init__(parent)
        #pub.subscribe(self.updateLoadingBar, "update")
        dwl_path = os.path.expanduser("~") + '/Downloads'
        print(dwl_path)
        if os.path.isdir(dwl_path):
            self.m_folder.SetValue(dwl_path)
        else:
            self.m_folder.SetValue(os.getcwd())

    def onWeatherModelChoice(self, event):
        """
        Method to update Precision and Zone lists each time a
        Model Weather is selected. Some options for Precision
        and Zone are specific to Model Weather.
        """
        choice = self.m_choiceWeatherModel.GetSelection()

        if choice == 0:
            # Model: Météo France
            # Update other choices with the different
            # options that are available for that model
            self.updateMeteoFranceChoices()

        elif choice == 1:
            self.updateOpenSkironChoices()
        else:
            # Default value is 0
            pass

    def updateMeteoFranceChoices(self):
        """
        Method to update specific options for
        Météo France weather model.
        """
        # Clear all options from all lists
        self.clearAllLists()

        # Add data in list
        self.m_choiceModelPrecision.Append("Arome (0,025° / 2 days)")
        self.m_choiceModelPrecision.Append("Arpège (0,1° / 4 days)")
        self.m_choiceZone.Append("Hyères")

        # Enable zone list in case it has
        # been disable by another model
        self.m_choiceZone.Enable(True)

    def clearAllLists(self):
        self.m_choiceModelPrecision.Clear()
        self.m_choiceZone.Clear()

    def updateOpenSkironChoices(self):
        """
        Method to update specific options for
        OpenSkiron (open source) weather model.
        """
        # Clear all options from all lists
        self.clearAllLists()

        # Add data in list
        self.m_choiceModelPrecision.Append("France (12km / 5 days)")
        self.m_choiceModelPrecision.Append("Local zone (4km / 2 days)")

        # Disable zone list as for model France only
        # one zone (France) is selectable
        self.m_choiceZone.Enable(False)

    def onPrecisionChoice(self, event):
        choice_model = self.m_choiceWeatherModel.GetSelection()
        choice_precision = self.m_choiceModelPrecision.GetSelection()

        # Check if the weather model has been changed twice
        # and if yes, update again.
        if choice_model == 1 and choice_precision == 0:
            self.m_choiceZone.Clear()
            self.m_choiceZone.Enable(False)
        elif choice_model == 1 and choice_precision == 1:
            self.updateLocalZones()
        else:
            pass

    def updateLocalZones(self):
        self.m_choiceZone.Clear()
        self.m_choiceZone.Append("Golfe du Lion")
        self.m_choiceZone.Append("Nice - Corse")
        self.m_choiceZone.Enable(True)

    def onDownloadClick(self, event):
        """
        Method to be launched when user click the download
        button, and start downloading grib file
        """
        # First, check if indicated path exists
        # otherwise display an error message and stops
        path = self.m_folder.GetValue()
        if not self.verifyFolderExists(path):
            return

        # First option is that user chooses
        # Météo France weather model
        if self.m_choiceWeatherModel.GetSelection() == 0:
            # Second option it that user select Arpege
            # or the Arome precision model
            if self.m_choiceModelPrecision.GetSelection() == 0:
                # Arome model
                model = Arome()
            else:
                # Arpege model
                model = Arpege()

            # Third option is to select the geographic
            # zone to download the data
            zone_number = self.m_choiceZone.GetSelection()
            if zone_number == 0:
                model.set_zone("hyeres")
            elif zone_number == 1:
                model.set_zone("lion-sardaigne")
            else:
                # Error
                sys.exit(1)

        # The second weather model is OpenSkiron,
        # an open source weather model with good results
        else:
            if self.m_choiceModelPrecision.GetSelection() == 0:
                # France zone
                model = OpenWrf('france')
            else:
                # Local zone
                if self.m_choiceZone.GetSelection() == 0:
                    # Golf du Lion
                    model = OpenWrf('lion')
                else:
                    # Nice - Corse
                    model = OpenWrf('nice')

        # Download
        progress_bar = wx.ProgressDialog(
            "Downloader",
            "GRIB file is downloading...",
            maximum=100,
            parent=self,
            style=wx.PD_APP_MODAL | wx.PD_SMOOTH | wx.PD_AUTO_HIDE
        )
        progress_bar.Update(0)
        model.dwl(path=path, loadingBarGUI=progress_bar)
        progress_bar.Destroy()

    def onFolderClick(self, event):
        # Open folder dialog box to choose
        # where to store the GRIB file
        dir_dialog = wx.DirDialog(self, "Choose a directory to save GRIB file")
        if dir_dialog.ShowModal() == wx.ID_OK:
            path = dir_dialog.GetPath()
            self.m_folder.SetValue(path)
        dir_dialog.Destroy()

    def verifyFolderExists(self, path):
        if os.path.isdir(path):
            return True
        else:
            error_dialog = wx.MessageDialog(
                self,
                "Error, not a valid folder to save grib file.\n" \
                "Please, check again the path name.",
                "Erreur",
                wx.OK | wx.ICON_WARNING
            )
            error_dialog.ShowModal()
            error_dialog.Destroy()
            return False

if __name__ == "__main__":
    main()
