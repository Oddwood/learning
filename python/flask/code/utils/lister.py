class Lister:
    @staticmethod
    def getList(numOfElements: int) ->str:
        out = ''
        for i in range(numOfElements):
            out += "<li>Item {}</li>".format(i)

        return '<ul>'+out+'</ul>'