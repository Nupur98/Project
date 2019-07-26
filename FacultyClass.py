from collections import defaultdict

class Faculty:
       def __init__(self,ename,eid,bookissued):
            self.ename=ename
            self.eid=eid
            self.book_list=defaultdict(int)