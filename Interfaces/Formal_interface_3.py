"""
    You must be careful when you're combining .__subclasshook__() with .register(),
    as .__subclasshook__() takes precedence over virtual subclass registration.
    To ensure that the registered virtual subclasses are taken into consideration,
    you must ass NotImplemented to the .__subclasshook__() dunder method.
    The FormalParserInterface would be updated to the following:
"""
import abc

class FormalParserInterface(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

class PdfParserNew:
    """
        Extract text from a PDF.
    """
    def load_data_source(self, path:str, file_name:str) -> str:
        pass
    def extract_text(self, full_file_path: str) -> dict:
        pass

@FormalParserInterface.register
class EmlParserNew:
    """Extract text from an email """
    def load_data_source(self, path:str, file_name:str)-> str:
        pass
    def extract_text_from_email(self, full_file_path:str) -> dict:
        pass

print(issubclass(PdfParserNew, FormalParserInterface))
print(issubclass(EmlParserNew, FormalParserInterface))

"""
    Since you've used registraction, you can see that EmlParserNew
    is considered a virtual subclass of you FormalparserInterface interface.
    This is not what you wanted since EmlParserNew doesn't override
    .extract_text().
"""