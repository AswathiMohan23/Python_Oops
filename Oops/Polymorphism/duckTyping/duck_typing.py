class MyEditor:
    def execute(self):
        print("compiling")
        print("Running")


class MyNewEditor:
    def execute(self):
        print("spell check")
        print("check")
        print("compiling")
        print("Running")


class Laptop:
    def code(self,editor):
        editor.execute()


editor = MyEditor()
lap1 = Laptop()
lap1.code(editor)
editor = MyNewEditor()
lap2 = Laptop()
lap2.code(editor)



