from enum import Enum
import typing


class DrawModel():
    """модель для хранения параметров необходимых для отрисовки
    графических фигур"""
    class ItemDraw():
        """"""
        def __init__(self):
            self.draw: typing.Union[str, None]= None
            self.cords: list = []

    def __init__(self):
        self.items = self.ItemDraw()
        # self.items.draw = None
        # self.items.cords = []
        self.type: typing.Union[str, None]= None
        self.color: typing.Union[tuple[float, float, float], 0,  None ] = None
        self.fill: typing.Union[tuple[float, float, float], 0,  None ] = None
        self.closePath: typing.Union[bool, None]= None
        self.even_odd: typing.Union[bool, None]= None
        self.seqno: typing.Union[int, None]= None
        self.dashes: typing.Union[str, None]= None
        self.dashes_pattern = None
        self.dashes_offset = None
        self.lineJoin: typing.Union[tuple[int, int, int], float,  None ] = None
        self.lineCap: typing.Union[tuple[int, int, int], float,  None ] = None
        self.width: typing.Union[float, None]= None
        self.stroke_opacity: typing.Union[float, None]= None
        self.fill_opacity: typing.Union[float, None]= None






    # def convert_even_odd(self, even_odd):
    #     if even_odd:
    #         return Qt.FillRule.OddEvenFill
    #     else:
    #         return  Qt.FillRule.WindingFill


    # def convert_line_join(self, line_join):
    #     if line_join == 0:
    #         return Qt.PenJoinStyle.BevelJoin
    #     elif line_join == 1:
    #         return Qt.PenJoinStyle.RoundJoin
    #     else:
    #         return Qt.PenJoinStyle.MiterJoin

    # def convert_line_cap(self, line_cap):
    #     if line_cap == 2:
    #         return Qt.PenCapStyle.SquareCap
    #     elif line_cap == 1:
    #         return Qt.PenCapStyle.RoundCap
    #     else:
    #         return Qt.PenCapStyle.FlatCap

    # def convert_dashes(self, dashes: str):
    #     list_str_dashes_pattern = "[]"
    #     str_dashes_offset = "0"
    #     # print(type(dashes), dashes)
    #     if  isinstance(dashes, str):
    #         if "[" in dashes and "]" in dashes:
    #             list_str_dashes_pattern = re.search(r'^\[[ 0-9\.]*\]', dashes).group(0).replace("[ ", "").replace(" ]", "").split(' ')
    #         if any(map(str.isdigit, dashes)):
    #             str_dashes_offset_0 = re.search(r'\] [\d]*$', dashes)
    #             if str_dashes_offset_0 is not None:
    #                 str_dashes_offset = str_dashes_offset_0.group(0).replace("] ", "")
    #     dashes_pattern = []
    #     dashes_offset = 0
    #     if list_str_dashes_pattern is not None and any(map(str.isdigit, list_str_dashes_pattern)): 
    #         dashes_pattern = list(map(float, list_str_dashes_pattern))
    #         # for d_p in range(len(dashes_pattern)):
    #         if dashes_pattern[0] == 0.0:
    #             dashes_pattern[0] = 1.0
    #             dashes_pattern[1] = 1.0
    #     if  str_dashes_offset.isdigit():
    #         dashes_offset = int(str_dashes_offset)
    #     return dashes_pattern, dashes_offset

