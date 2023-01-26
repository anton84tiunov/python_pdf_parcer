import typing

class TextSpane():

    def __init__(self):
        self.span_size: float = ...
        self.span_flags: int =  ...
        self.span_font: str = ...
        self.span_color: typing.Union[typing.Tuple[float, float, float], int, None] = ...
        self.span_ascender: float = ...
        self.span_descender: float = ...
        self.span_text: str = ...
        self.span_origin: typing.Union[typing.Tuple[float, float], None] = ...
        self.span_bbox: typing.Union[typing.Tuple[float, float, float, float], None] = ...

class TextLine():

    def __init__(self):
        self.line_wmode: int = ...
        self.line_dir: typing.Union[typing.Tuple[float, float], None] = ...
        self.line_bbox: typing.Union[typing.Tuple[float, float, float, float], None] = ...
        self.line_spans: typing.List[TextSpane] = [] #list[self.TextSpane]
        
class TextModel():

    def __init__(self):
        self.block_number: typing.Union[typing.Int, None] = ...
        self.block_type: typing.Union[typing.Int, None] = ...
        self.block_bbox: typing.Union[typing.Tuple[float, float, float, float], None] = ...
        # @typing.List[self.TextLine]
        self.block_lines: typing.List[TextLine] = []  #list[self.TextLine]

    def __repr__(self) -> str:
        return f"""
        ______________________________
        class TextModel:  
        ...block_number: {self.block_number},
        ...block_type: {self.block_type},
        ...block_bbox: {self.block_bbox},
        ...block_lines: List[class TextLine]:
        .......line_wmode: {self.block_lines[0].line_wmode},
        .......line_dir: {self.block_lines[0].line_dir},
        .......line_bbox: {self.block_lines[0].line_bbox},
        .......line_spans: List[class TextSpane]:
        ..........span_size: {self.block_lines[0].line_spans[0].span_size},
        ..........span_flags: {self.block_lines[0].line_spans[0].span_flags},
        ..........span_font: {self.block_lines[0].line_spans[0].span_font},
        ..........span_color: {self.block_lines[0].line_spans[0].span_color},
        ..........span_ascender: {self.block_lines[0].line_spans[0].span_ascender},
        ..........span_descender: {self.block_lines[0].line_spans[0].span_descender},
        ..........span_text: {self.block_lines[0].line_spans[0].span_text},
        ..........span_origin: {self.block_lines[0].line_spans[0].span_origin},
        ..........span_bbox: {self.block_lines[0].line_spans[0].span_bbox}.
        ______________________________
        """



# def convert_text(self, block, scene):
#     block_number = block["number"] # 0
#     block_type = block["type"] # 0
#     block_bbox = block["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
#     block_lines = block["lines"]
#     for line in block_lines:
#         line_wmode = line["wmode"] # 0
#         line_dir = line["dir"] # (1.0, 0.0)
#         line_bbox = line["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
#         line_spans = line["spans"]
#         for span in line_spans:
#             span_size = span["size"] # 20.0
#             span_flags =  span["flags"] # 4
#             span_font = span["font"] # 'Times New Roman'
#             span_color = span["color"] # 0
#             span_ascender = span["ascender"] # 0.89111328125   восходящий
#             span_descender = span["descender"] # -0.21630859375 спусковое устройство
#             span_text = span["text"] # 'Пример PDF файла'
#             span_origin = span["origin"] # (43.0, 54.0)
#             span_bbox = span["bbox"] # (43.0, 36.177734375, 207.52720642089844, 58.326171875)
#             # flags_decomposer(s["flags"])