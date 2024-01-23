# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\5\2|\n\2\3\3\3\3\3\3\5\3\u0081\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\7\5\u0091\n\5\f\5\16\5\u0094\13\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\5\6\u009b\n\6\3\6\3\6\3\6\5\6\u00a0\n\6\7\6\u00a2")
        buf.write("\n\6\f\6\16\6\u00a5\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u00b2\n\7\3\b\5\b\u00b5\n\b\3\b\6\b")
        buf.write("\u00b8\n\b\r\b\16\b\u00b9\3\b\3\b\7\b\u00be\n\b\f\b\16")
        buf.write("\b\u00c1\13\b\5\b\u00c3\n\b\3\b\3\b\5\b\u00c7\n\b\3\b")
        buf.write("\6\b\u00ca\n\b\r\b\16\b\u00cb\5\b\u00ce\n\b\3\t\6\t\u00d1")
        buf.write("\n\t\r\t\16\t\u00d2\3\n\3\n\3\n\7\n\u00d8\n\n\f\n\16\n")
        buf.write("\u00db\13\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\5!\u0155\n!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u015c\n\"\3#\3#\3#\3#\5#\u0162")
        buf.write("\n#\3$\3$\3$\3$\7$\u0168\n$\f$\16$\u016b\13$\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,")
        buf.write("\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\78\u019e\n8\f8\168\u01a1\138\39\69\u01a4")
        buf.write("\n9\r9\169\u01a5\39\39\3:\3:\3:\7:\u01ad\n:\f:\16:\u01b0")
        buf.write("\13:\3:\3:\3;\3;\3;\7;\u01b7\n;\f;\16;\u01ba\13;\3;\3")
        buf.write(";\3;\3<\3<\3<\3\u0169\2=\3\3\5\4\7\5\t\2\13\2\r\6\17\7")
        buf.write("\21\2\23\b\25\2\27\2\31\2\33\t\35\n\37\13!\f#\r%\16\'")
        buf.write("\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32")
        buf.write("?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g")
        buf.write("/i\60k\61m\62o\63q\64s\65u\66w\67\3\2\n\4\2GGgg\4\2--")
        buf.write("//\3\2\62;\6\2\f\f\17\17$$))\n\2$$))^^ddhhppttvv\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01d6\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\3{\3\2\2\2\5\u0080\3\2\2\2\7\u0082\3\2\2")
        buf.write("\2\t\u008b\3\2\2\2\13\u0097\3\2\2\2\r\u00b1\3\2\2\2\17")
        buf.write("\u00b4\3\2\2\2\21\u00d0\3\2\2\2\23\u00d4\3\2\2\2\25\u00df")
        buf.write("\3\2\2\2\27\u00e1\3\2\2\2\31\u00e4\3\2\2\2\33\u00e7\3")
        buf.write("\2\2\2\35\u00ec\3\2\2\2\37\u00f2\3\2\2\2!\u00f9\3\2\2")
        buf.write("\2#\u00fe\3\2\2\2%\u0105\3\2\2\2\'\u010c\3\2\2\2)\u0110")
        buf.write("\3\2\2\2+\u0118\3\2\2\2-\u011d\3\2\2\2/\u0121\3\2\2\2")
        buf.write("\61\u0127\3\2\2\2\63\u012a\3\2\2\2\65\u0130\3\2\2\2\67")
        buf.write("\u0139\3\2\2\29\u013c\3\2\2\2;\u0141\3\2\2\2=\u0146\3")
        buf.write("\2\2\2?\u014c\3\2\2\2A\u0154\3\2\2\2C\u015b\3\2\2\2E\u0161")
        buf.write("\3\2\2\2G\u0163\3\2\2\2I\u016e\3\2\2\2K\u0170\3\2\2\2")
        buf.write("M\u0172\3\2\2\2O\u0174\3\2\2\2Q\u0176\3\2\2\2S\u0178\3")
        buf.write("\2\2\2U\u017b\3\2\2\2W\u017e\3\2\2\2Y\u0180\3\2\2\2[\u0183")
        buf.write("\3\2\2\2]\u0186\3\2\2\2_\u0188\3\2\2\2a\u018a\3\2\2\2")
        buf.write("c\u018e\3\2\2\2e\u0191\3\2\2\2g\u0193\3\2\2\2i\u0195\3")
        buf.write("\2\2\2k\u0197\3\2\2\2m\u0199\3\2\2\2o\u019b\3\2\2\2q\u01a3")
        buf.write("\3\2\2\2s\u01a9\3\2\2\2u\u01b3\3\2\2\2w\u01be\3\2\2\2")
        buf.write("y|\5\5\3\2z|\5\7\4\2{y\3\2\2\2{z\3\2\2\2|\4\3\2\2\2}\u0081")
        buf.write("\5\37\20\2~\u0081\5!\21\2\177\u0081\5#\22\2\u0080}\3\2")
        buf.write("\2\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\6\3\2\2\2")
        buf.write("\u0082\u0083\5\5\3\2\u0083\u0084\5\t\5\2\u0084\u0085\7")
        buf.write(">\2\2\u0085\u0086\7/\2\2\u0086\u0087\3\2\2\2\u0087\u0088")
        buf.write("\5i\65\2\u0088\u0089\5\13\6\2\u0089\u008a\5k\66\2\u008a")
        buf.write("\b\3\2\2\2\u008b\u008c\5i\65\2\u008c\u0092\5\21\t\2\u008d")
        buf.write("\u008e\5m\67\2\u008e\u008f\5\21\t\2\u008f\u0091\3\2\2")
        buf.write("\2\u0090\u008d\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0095\u0096\5k\66\2\u0096\n\3\2\2\2\u0097")
        buf.write("\u009a\5i\65\2\u0098\u009b\5\5\3\2\u0099\u009b\5\13\6")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u00a3")
        buf.write("\3\2\2\2\u009c\u009f\5m\67\2\u009d\u00a0\5\5\3\2\u009e")
        buf.write("\u00a0\5\13\6\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2")
        buf.write("\2\u00a0\u00a2\3\2\2\2\u00a1\u009c\3\2\2\2\u00a2\u00a5")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\5k\66\2")
        buf.write("\u00a7\f\3\2\2\2\u00a8\u00a9\7V\2\2\u00a9\u00aa\7T\2\2")
        buf.write("\u00aa\u00ab\7W\2\2\u00ab\u00b2\7G\2\2\u00ac\u00ad\7H")
        buf.write("\2\2\u00ad\u00ae\7C\2\2\u00ae\u00af\7N\2\2\u00af\u00b0")
        buf.write("\7U\2\2\u00b0\u00b2\7G\2\2\u00b1\u00a8\3\2\2\2\u00b1\u00ac")
        buf.write("\3\2\2\2\u00b2\16\3\2\2\2\u00b3\u00b5\7/\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6")
        buf.write("\u00b8\5\21\t\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00c2")
        buf.write("\3\2\2\2\u00bb\u00bf\13\2\2\2\u00bc\u00be\5\21\t\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c2\u00bb\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00cd")
        buf.write("\3\2\2\2\u00c4\u00c6\t\2\2\2\u00c5\u00c7\t\3\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00ca\5\21\t\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00ce\3\2\2\2\u00cd\u00c4\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\20\3\2\2\2\u00cf\u00d1\t\4\2\2\u00d0\u00cf\3\2")
        buf.write("\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\22\3\2\2\2\u00d4\u00d9\7$\2\2\u00d5\u00d8")
        buf.write("\5\25\13\2\u00d6\u00d8\5\27\f\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00dd\7$\2\2\u00dd\u00de\b\n\2\2\u00de\24")
        buf.write("\3\2\2\2\u00df\u00e0\n\5\2\2\u00e0\26\3\2\2\2\u00e1\u00e2")
        buf.write("\7^\2\2\u00e2\u00e3\t\6\2\2\u00e3\30\3\2\2\2\u00e4\u00e5")
        buf.write("\7^\2\2\u00e5\u00e6\n\6\2\2\u00e6\32\3\2\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\34\3\2\2\2\u00ec\u00ed\7h\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7w\2\2\u00f4\u00f5\7o\2\2\u00f5\u00f6\7d\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7t\2\2\u00f8 \3\2\2\2\u00f9\u00fa")
        buf.write("\7d\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7n\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7i\2\2\u0104$\3\2\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7g\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7w\2\2\u0109\u010a\7t\2\2\u010a\u010b\7p\2\2\u010b&\3")
        buf.write("\2\2\2\u010c\u010d\7x\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f(\3\2\2\2\u0110\u0111\7f\2\2\u0111\u0112")
        buf.write("\7{\2\2\u0112\u0113\7p\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7o\2\2\u0115\u0116\7k\2\2\u0116\u0117\7e\2\2\u0117*\3")
        buf.write("\2\2\2\u0118\u0119\7h\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7e\2\2\u011c,\3\2\2\2\u011d\u011e")
        buf.write("\7h\2\2\u011e\u011f\7q\2\2\u011f\u0120\7t\2\2\u0120.\3")
        buf.write("\2\2\2\u0121\u0122\7w\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7k\2\2\u0125\u0126\7n\2\2\u0126\60")
        buf.write("\3\2\2\2\u0127\u0128\7d\2\2\u0128\u0129\7{\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7d\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\u012e\7c\2\2\u012e\u012f\7m\2\2\u012f\64")
        buf.write("\3\2\2\2\u0130\u0131\7e\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7p\2\2\u0133\u0134\7v\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\7p\2\2\u0136\u0137\7w\2\2\u0137\u0138\7g\2\2\u0138\66")
        buf.write("\3\2\2\2\u0139\u013a\7k\2\2\u013a\u013b\7h\2\2\u013b8")
        buf.write("\3\2\2\2\u013c\u013d\7g\2\2\u013d\u013e\7n\2\2\u013e\u013f")
        buf.write("\7u\2\2\u013f\u0140\7g\2\2\u0140:\3\2\2\2\u0141\u0142")
        buf.write("\7g\2\2\u0142\u0143\7n\2\2\u0143\u0144\7k\2\2\u0144\u0145")
        buf.write("\7h\2\2\u0145<\3\2\2\2\u0146\u0147\7d\2\2\u0147\u0148")
        buf.write("\7g\2\2\u0148\u0149\7i\2\2\u0149\u014a\7k\2\2\u014a\u014b")
        buf.write("\7p\2\2\u014b>\3\2\2\2\u014c\u014d\7g\2\2\u014d\u014e")
        buf.write("\7p\2\2\u014e\u014f\7f\2\2\u014f@\3\2\2\2\u0150\u0155")
        buf.write("\7#\2\2\u0151\u0152\7p\2\2\u0152\u0153\7q\2\2\u0153\u0155")
        buf.write("\7v\2\2\u0154\u0150\3\2\2\2\u0154\u0151\3\2\2\2\u0155")
        buf.write("B\3\2\2\2\u0156\u0157\7(\2\2\u0157\u015c\7(\2\2\u0158")
        buf.write("\u0159\7c\2\2\u0159\u015a\7p\2\2\u015a\u015c\7f\2\2\u015b")
        buf.write("\u0156\3\2\2\2\u015b\u0158\3\2\2\2\u015cD\3\2\2\2\u015d")
        buf.write("\u015e\7~\2\2\u015e\u0162\7~\2\2\u015f\u0160\7q\2\2\u0160")
        buf.write("\u0162\7t\2\2\u0161\u015d\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0162F\3\2\2\2\u0163\u0164\7%\2\2\u0164\u0165\7%\2\2")
        buf.write("\u0165\u0169\3\2\2\2\u0166\u0168\13\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u016a\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016c\u016d\7\f\2\2\u016dH\3\2\2\2\u016e\u016f\7,\2\2")
        buf.write("\u016fJ\3\2\2\2\u0170\u0171\7\61\2\2\u0171L\3\2\2\2\u0172")
        buf.write("\u0173\7-\2\2\u0173N\3\2\2\2\u0174\u0175\7/\2\2\u0175")
        buf.write("P\3\2\2\2\u0176\u0177\7\'\2\2\u0177R\3\2\2\2\u0178\u0179")
        buf.write("\7>\2\2\u0179\u017a\7?\2\2\u017aT\3\2\2\2\u017b\u017c")
        buf.write("\7@\2\2\u017c\u017d\7?\2\2\u017dV\3\2\2\2\u017e\u017f")
        buf.write("\7?\2\2\u017fX\3\2\2\2\u0180\u0181\7#\2\2\u0181\u0182")
        buf.write("\7?\2\2\u0182Z\3\2\2\2\u0183\u0184\7>\2\2\u0184\u0185")
        buf.write("\7/\2\2\u0185\\\3\2\2\2\u0186\u0187\7>\2\2\u0187^\3\2")
        buf.write("\2\2\u0188\u0189\7@\2\2\u0189`\3\2\2\2\u018a\u018b\7\60")
        buf.write("\2\2\u018b\u018c\7\60\2\2\u018c\u018d\7\60\2\2\u018db")
        buf.write("\3\2\2\2\u018e\u018f\7?\2\2\u018f\u0190\7?\2\2\u0190d")
        buf.write("\3\2\2\2\u0191\u0192\7*\2\2\u0192f\3\2\2\2\u0193\u0194")
        buf.write("\7+\2\2\u0194h\3\2\2\2\u0195\u0196\7]\2\2\u0196j\3\2\2")
        buf.write("\2\u0197\u0198\7_\2\2\u0198l\3\2\2\2\u0199\u019a\7.\2")
        buf.write("\2\u019an\3\2\2\2\u019b\u019f\t\7\2\2\u019c\u019e\t\b")
        buf.write("\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0p\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a2\u01a4\t\t\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a8\b9\3\2\u01a8r\3\2\2\2")
        buf.write("\u01a9\u01ae\7$\2\2\u01aa\u01ad\5\25\13\2\u01ab\u01ad")
        buf.write("\5\27\f\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\b")
        buf.write(":\4\2\u01b2t\3\2\2\2\u01b3\u01b8\7$\2\2\u01b4\u01b7\5")
        buf.write("\25\13\2\u01b5\u01b7\5\27\f\2\u01b6\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3")
        buf.write("\2\2\2\u01bb\u01bc\5\31\r\2\u01bc\u01bd\b;\5\2\u01bdv")
        buf.write("\3\2\2\2\u01be\u01bf\13\2\2\2\u01bf\u01c0\b<\6\2\u01c0")
        buf.write("x\3\2\2\2\36\2{\u0080\u0092\u009a\u009f\u00a3\u00b1\u00b4")
        buf.write("\u00b9\u00bf\u00c2\u00c6\u00cb\u00cd\u00d2\u00d7\u00d9")
        buf.write("\u0154\u015b\u0161\u0169\u019f\u01a5\u01ac\u01ae\u01b6")
        buf.write("\u01b8\7\3\n\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DATATYPE = 1
    PRIMITIVE = 2
    ARRAY = 3
    BOOLEANLIT = 4
    NUMBERLIT = 5
    STRINGLIT = 6
    TRUE = 7
    FALSE = 8
    NUMBER = 9
    BOOL = 10
    STRING = 11
    RETURN = 12
    VAR = 13
    DYNAMIC = 14
    FUNC = 15
    FOR = 16
    UNTIL = 17
    BY = 18
    BREAK = 19
    CONTINUE = 20
    IF = 21
    ELSE = 22
    ELIF = 23
    BEGIN = 24
    END = 25
    NOT = 26
    AND = 27
    OR = 28
    COMMENT = 29
    MUL = 30
    DIV = 31
    ADD = 32
    MINUS = 33
    MOD = 34
    LTE = 35
    GTE = 36
    EQ = 37
    NEQ = 38
    ASS = 39
    LT = 40
    GT = 41
    CONC = 42
    EQEQ = 43
    LR = 44
    RR = 45
    LS = 46
    RS = 47
    COMMA = 48
    IDENTIFIER = 49
    WS = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52
    ERROR_CHAR = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'*'", "'/'", "'+'", "'-'", "'%'", "'<='", "'>='", 
            "'='", "'!='", "'<-'", "'<'", "'>'", "'...'", "'=='", "'('", 
            "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DATATYPE", "PRIMITIVE", "ARRAY", "BOOLEANLIT", "NUMBERLIT", 
            "STRINGLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "COMMENT", 
            "MUL", "DIV", "ADD", "MINUS", "MOD", "LTE", "GTE", "EQ", "NEQ", 
            "ASS", "LT", "GT", "CONC", "EQEQ", "LR", "RR", "LS", "RS", "COMMA", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "DATATYPE", "PRIMITIVE", "ARRAY", "DIMENSION", "ARRAY_VALUES", 
                  "BOOLEANLIT", "NUMBERLIT", "DIGIT", "STRINGLIT", "NON_ESC", 
                  "ESC", "ILL_ESC", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "COMMENT", "MUL", "DIV", "ADD", "MINUS", 
                  "MOD", "LTE", "GTE", "EQ", "NEQ", "ASS", "LT", "GT", "CONC", 
                  "EQEQ", "LR", "RR", "LS", "RS", "COMMA", "IDENTIFIER", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


