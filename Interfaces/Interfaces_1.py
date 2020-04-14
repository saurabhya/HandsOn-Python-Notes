"""
   In certain circumstances, you may not need the strict rules of a formal interface.
    Python's dynamic nature allows you to implement an informal interface.
    An informal interface is a class that defines methods that can be overridden,
    but there's no strict enforcement.

    Following we will see the perpective of a data engineer who needs to extract
    text from various different unstructured file types. We will create
    an informal interface that defines the methods that will be in both the
    PdfParser and EmlParser concrete classes:
"""

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """
            Load in the file for extracting text.
        """
        pass
    def extract_text(self, full_file_name: str) -> dict:
        """
            Extract text from the currently loaded file
        """
        pass

"""
    InformalParserInterface defines the two methods .load_data_source() and
    .extract_text(). These methods are defined but bot implemented.
    The implementation will occur once you create concrete classes that inherit from
    InformalParserInterface.



    With duck typing in mind, you define two classes that implment the InfroamlParserInterface
    To use your interface, you musr create a concrete class. A concrete class is
    a subclass of the interface that provides an implementation of the interface's methods.
    We'll crrete two concrete classes to implement our interface.
"""

class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path:str, file_name:str) -> str:
        """Overrides InformalParserInterface.load_data_source() """
        pass
    def extract_text(self, full_file_name:str)->str:
        """Overrides InformalParserInterface.extract_text() """
        pass


# The second cocrete class is EmlParser, which you'll us to pasrse the text fro emails.

class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name:str)-> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass
    def extract_text_from_email(self, full_file_name:str)->str:
        """ A method defined only in EmlParser.
            Does not override InformalParserInterface.extract_text()"""
        pass

"""
    So far, we have defined two concrete implementation of the InformalparserInterface.
    However, note that EmlParser fails to properly define .extract_text().
    If you were to check whether EmlParser implements InformalparserInterface,
    then you will get a True for is subclass(Emlparser, InformalParserInterface).
    which is a bit of a problem as it violets the definition of an interface.
"""