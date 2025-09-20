from .interfaces import SSMLParser, SSMLNode, SSMLTag, SSMLText


class SSMLParserImpl(SSMLParser):
    def escape(self, txt: str) -> str:
        return txt.replace("&", "&amp;").replace("<", '&lt;').replace(">", "&gt;")

    def unescape(self, txt: str) -> str:
        return txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    
    def to_text(self, node: SSMLNode) -> str:
        raise NotImplementedError("to_text() has not been implemented yet.")
    
    def parse(self, ssml: str) -> SSMLNode:
        raise NotImplementedError("parse() has not been implemented yet.")
        
