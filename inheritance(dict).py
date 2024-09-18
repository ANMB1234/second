from typing import Optional


class LongNameDict(dict[str,int]):
    def longest_key(self)->Optional[str]:
        """
        사실상 max(self,key-len)이지만 모호하지않다.

        Returns:
            Optional[str]: _description_
        """
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest