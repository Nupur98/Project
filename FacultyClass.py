from collections import defaultdict
#Faculty Class
class Faculty:
       def __init__(self,ename,eid,bookissued):
            self.ename=ename
            self.eid=eid
            self.book_list=defaultdict(int)