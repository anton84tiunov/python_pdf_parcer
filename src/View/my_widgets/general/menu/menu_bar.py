import sys
import src.Utility.general.comfig.config as config
from PySide6 import QtWidgets, QtGui,  QtCore 


class MenuBar(QtWidgets.QMenuBar):
    """Бпзовый класс для создания вкладок QTabWidget"""

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.list_style = ["Clocker", "Clientor", "Chatbee", "Eclippy", "Dtor", "EasyCode", "Geoo", "Mixchat", "Scalcula", "TCobra", "Webmas", "Ubuntu", "NeonButtons", "MaterialDark", "ManjaroMix", "MacOS", "ConsoleStyle", "Aqua", "AMOLED", "MailSy"]



        self.menu_file = self.addMenu("File")
        self.menu_file.addAction("New")
        self.menu_file.addAction("Open")
        self.menu_file.addAction("Save")

        self.menu_settings = self.addMenu("settings")
        self.menu_settings_style = self.menu_settings.addMenu("style")
     
        # for style in self.list_style:
        #     # action = QtGui.QAction(self)
        #     # action = self.menu_settings_style.addAction(style)
        #     action = QtWidgets.QWidgetAction( self)
        #     self.menu_settings_style.addAction(action)
        #     action.setText(style)
            
        #     action.triggered.connect(lambda: self.set_win_style(style))

   
        
        self.win_style  = self.menu_settings_style.addAction("win_style")
        self.win_style.triggered.connect(lambda: self.set_win_style("win_style"))

        # self.style_Clocker  = self.menu_settings_style.addAction("Clocker")
        # self.style_Clocker.triggered.connect(lambda: self.set_win_style("Clocker"))
        
        # self.style_Clientor  = self.menu_settings_style.addAction("Clientor")
        # self.style_Clientor.triggered.connect(lambda: self.set_win_style("Clientor"))
        
        self.style_Chatbee  = self.menu_settings_style.addAction("Chatbee")
        self.style_Chatbee.triggered.connect(lambda: self.set_win_style("Chatbee"))
        
        # self.style_Eclippy  = self.menu_settings_style.addAction("Eclippy")
        # self.style_Eclippy.triggered.connect(lambda: self.set_win_style("Eclippy"))
        
        # self.style_Dtor = self.menu_settings_style.addAction("Dtor")
        # self.style_Dtor.triggered.connect(lambda: self.set_win_style("Dtor"))
        
        self.style_EasyCode  = self.menu_settings_style.addAction("EasyCode")
        self.style_EasyCode.triggered.connect(lambda: self.set_win_style("EasyCode"))
        
        self.style_Geoo  = self.menu_settings_style.addAction("Geoo")
        self.style_Geoo.triggered.connect(lambda: self.set_win_style("Geoo"))
        
        # self.style_Mixchat  = self.menu_settings_style.addAction("Mixchat")
        # self.style_Mixchat.triggered.connect(lambda: self.set_win_style("Mixchat"))
        
        # self.style_Scalcula  = self.menu_settings_style.addAction("Scalcula")
        # self.style_Scalcula.triggered.connect(lambda: self.set_win_style("Scalcula"))
        
        self.style_TCobra  = self.menu_settings_style.addAction("TCobra")
        self.style_TCobra.triggered.connect(lambda: self.set_win_style("TCobra"))
        
        self.style_Webmas  = self.menu_settings_style.addAction("Webmas")
        self.style_Webmas.triggered.connect(lambda: self.set_win_style("Webmas"))
        
        self.style_Ubuntu  = self.menu_settings_style.addAction("Ubuntu")
        self.style_Ubuntu.triggered.connect(lambda: self.set_win_style("Ubuntu"))
        
        self.style_NeonButtons  = self.menu_settings_style.addAction("NeonButtons")
        self.style_NeonButtons.triggered.connect(lambda: self.set_win_style("NeonButtons"))
        
        # self.style_MaterialDark  = self.menu_settings_style.addAction("MaterialDark")
        # self.style_MaterialDark.triggered.connect(lambda: self.set_win_style("MaterialDark"))
        
        self.style_ManjaroMix  = self.menu_settings_style.addAction("ManjaroMix")
        self.style_ManjaroMix.triggered.connect(lambda: self.set_win_style("ManjaroMix"))
        
        self.style_MacOS  = self.menu_settings_style.addAction("MacOS")
        self.style_MacOS.triggered.connect(lambda: self.set_win_style("MacOS"))
        
        self.style_ElegantDark  = self.menu_settings_style.addAction("ElegantDark")
        self.style_ElegantDark.triggered.connect(lambda: self.set_win_style("ElegantDark"))
        
        self.style_ConsoleStyle  = self.menu_settings_style.addAction("ConsoleStyle")
        self.style_ConsoleStyle.triggered.connect(lambda: self.set_win_style("ConsoleStyle"))
        
        # self.style_Aqua  = self.menu_settings_style.addAction("Aqua")
        # self.style_Aqua.triggered.connect(lambda: self.set_win_style("Aqua"))
        
        # self.style_AMOLED  = self.menu_settings_style.addAction("AMOLED")
        # self.style_AMOLED.triggered.connect(lambda: self.set_win_style("AMOLED"))
        
        self.style_MailSy  = self.menu_settings_style.addAction("MailSy")
        self.style_MailSy.triggered.connect(lambda: self.set_win_style("MailSy"))

    def set_win_style(self, style):
        # self.root.setStyleSheet(QtWidgets.QProxyStyle.baseStyle())
        self.root.setStyleSheet(open(config.resource_path("style/" + style + ".qss"), "r").read())
        config.update_setting(config.resource_path("configs/sryle_config.INI"), "Style", "current_style", style)

