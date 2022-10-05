class NodeMahasiswa:
    def __init__(self,nama,ipk,n=None,p=None):
        self._element = nama
        self._ipk = ipk
        self._next = n
        self._prev = p

    def getNama(self):
        return self._element
    
    def getIpk(self):
        return self._ipk

    def setNama(self,nama):
        self._element = nama

    def setIpk(self,ipk):
        self._ipk = ipk