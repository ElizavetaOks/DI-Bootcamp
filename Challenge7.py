# Daily Challenge : Pagination
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
# The Pagination class will accept 2 parameters:
# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.

class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = int(pageSize)
        self.totalPages = 0
        self.currentPage = 1
        self.updateTotalPages()

# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:
    # p.getVisibleItems() 
# You will have to implement various methods to go through the pages such as:
    # prevPage()
    # nextPage()
    # firstPage()
    # lastPage()
    # goToPage(pageNum)

    def updateTotalPages(self):
        self.totalPages = max(1, int(len(self.items) / self.pageSize) + (len(self.items) % self.pageSize > 0))

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        self.currentPage = max(1, min(self.totalPages, int(pageNum)))
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems()) 
p.goToPage(10)
print(p.getVisibleItems()) 





