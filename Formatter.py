from typing import Optional


class Formatter:
    def format(self,string:str)->str:
        return str(string).title()
class Point:
    pass
    
def format_string(string: str,formatter:Optional[Formatter]=None)->str:
    """ 
    formatter 객체를 사용해 문자열을 포맷한다.
    formatter은 문자열을 수신하는 format()메서드를 가져야한다.
    """
    
    class DefaultFormatter(Formatter):
        """제목 대소문자 형식으로 문자열을 포맷한다."""
        
        def format(self,string:str)->str:
            return str(string).title()
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)

print(format_string("hello world!"))