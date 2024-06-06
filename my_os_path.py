import os
import src.Utility.general.comfig.config as config


root_path = os.path.dirname(os.path.abspath(__file__))
print(root_path)
icon = config.resource_path(os.path.join(root_path, "assets", "icon", "icon_png"))
icon_svg = config.resource_path(os.path.join(root_path, "assets", "icon", "icon_svg"))
icon_ico = config.resource_path(os.path.join(root_path, "assets", "icon", "icon_ico"))