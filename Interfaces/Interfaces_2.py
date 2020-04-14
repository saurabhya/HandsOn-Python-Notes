"""
    Using Metaclass
    Ideally, you would want issubclass(EmlParser, InformalParserInterface) to return False
    when the implementing class doesn't define all of the interface's abstract methods.
    To do this, you'll create a metaclass called ParseMeta. You'll be overriding
    two dunder(special methods) methods.
    1. __instancecheck()__
    2. __subclasscheck()__

    below, we create a class called UpdatedInformalparserInterface that builds from the
    parseMeta metaclass:
"""
class ParseMeta(type):
    """
        A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and callable(subclass.load_data_source) and hasattr(subclass, 'extract_text') and callable(subclass.extract_text))

class UpdatedInformalparserInterface(metaclass=ParseMeta):
    """
        This interface is used for concrete classes to inherit from.
        There is no need to define the Parsemeta methods as any class as
        they are implicitely made available via .__subclasscheck__().
    """
    pass

"""
    Now that ParseMeta and UpdatedInformalParseInterface have been created, you can create
    your concrete implementations.
"""
class PdfParserNew:
    def load_data_source(self, path:str, file_name:str)-> str:
        pass
    def extract_text(self, full_filr_path: str)-> dict:
        pass

class EmlParserNew:
    def load_data_source(self, path: str, file_name: str)-> str:
        pass
    def extract_text_from_email(self, full_file_path)->dict:
        pass

"""
    Here, we have a metaclass that's used to create UpdatedInformalParserInterface.
    By using a metaclass, you don't need to explicitely define the subclass.
    Instead, the subclass must define the required nethods. If it doesn't, then
    issubclass(EmlParserNew, UpdatedInformalparserInterface) will return False.
"""
