from pygments.lexer import *
from pygments.token import *

class CustomLexer(RegexLexer):
    name = 'Balloon'
    aliases = ['balloon', 'bl']
    filenames = '*.bl'

    tokens = {
        'root': [

            include('keywords'),

            (r'[]{}(),:;[]', Punctuation),
            (r'#.*?$', Comment),

            (r'[+-]?[0-9]+\.[0-9]+', Number.Float),
            (r'[+-]?[0-9]+', Number.Integer),

            (r'<=|>=|==|[+*<>=%\-\/]', Operator),
            (r'(and|or|not)\b', Operator.Word),

            (r'".*"', String),

            (r'(var|fn)\b', Keyword.Declaration),

            (r'[a-zA-Z_][a-zA-Z0-9_]*[!?]?', Name),
            (r'\s+', Text)
        ],

        'keywords': [
            (words((
                'if', 'else', 'loop', 'break', 'continue', 'return',
                'Number', 'Bool', 'String', 'Function', 'Tuple',
                'any', 'void', 'true', 'false'), suffix=r'\b'),
            Keyword),
        ],

    }
