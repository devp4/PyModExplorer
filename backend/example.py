from typing import Any


class Main(Exception): 
    """TEST DOC"""
    name = "Test"
    class Main2(EncodingWarning):
        name = "test"
        class Main4():
            def __init__(self) -> None:
                """INIT FUNC"""
                self.test = "test"         
            def __delattr__(self, __name: str, test=5,) -> None:
                y = "t"  
        class Main5():
            def __delattr__(self, __name: str) -> None:
                pass
    class Main3():
        def __ne__(self, __value: object) -> bool:
            pass

        async def test():
            pass
        

class Main6(): 
    name = "Test"
    class Main7():
        class Main8():
            pass
        class Main9():
            pass
    class Main10():
        def __call__(self, *args: Any, **kwds: Any) -> Any:
            pass
    
    # def __init__(self, name: int) -> None:
    #     pass

def func():
    pass

async def test():
    pass


print(Main.o)