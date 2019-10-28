from ramile.processors import FileProcessorBase
from ramile.processors import BlankLineFilter
from ramile.filters.c_style_comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.double_slash_comment_filter import DoubleSlashCommentFilter


class JsProcessor(FileProcessorBase):
    expected_extensions = ['.js', '.jsx', '.vue', '.wpy']

    def __init__(self):
        self.filters.append(BlankLineFilter())
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
