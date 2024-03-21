class Class:

   def __init__(self, base_attr):

       self.base_attr = base_attr

   def base_method(self):
class SportClass(Class):

   def __init__(self, base_attr, child1_attr):

    super().__init__(base_attr)

    self.child1_attr = child1_attr

