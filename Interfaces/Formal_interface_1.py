"""
    Informal interfaces can be useful for projects with small
    code base and a limited number of programmers. However,
    informal interfaces would be the wrong approach for larger
    applications. In order to create a formal Python Interface, 
    you'll need a few more tools from Python's abc module.


    To inforce the subclass instatiation of abstract methods,
    we'll utilize Python's builtin AbCMeta from abc module.

    Rather than create your own metaclass, you'll use
    abc.ABCMeta as the metaclass. Then you'll ovwrwrite .__subclasshook__()
    in place of .__instancecheck() and .__subclasscheck__() as it creates
    more reliable implementation of these dunder methods.

    Following we'll see the implemantation of FormalParserInterface using
    abc.ABCMeta as your metaclass.
"""
import abc

class FormalParserInterface(metaclass= abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class PdfParserNew:
    def load_data_source(self, path:str, file_name:str) -> str:
        pass

    def extract_text(self, full_file_path:str) -> dict:
        pass

class EmlParserNew:
    def load_data_source(self, path:str, file_name:str) -> str:
        pass

    def extract_text_from_email(self, full_file_path:str)-> dict:
        pass


"""
    If you run issubclass() on PdfPaserNew and EmlParsernew, then
    issubclass() will return True and False, respectively.
"""