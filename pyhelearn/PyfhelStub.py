from Phfhel import PyPtxt, PyCtxt

class PyPtxtStub(PyPtxt):
  def __init__(self, v, *a, **kw):
    super(*a, **kw)
    self.value = v
  def setval(self, v):
    self.value = v
  def getval(self):
    return self.value


class PyCtxtStub(PyCtxt):
  def __init__(self, v, he):
    super(v, he)
    self.value = v
  def setval(self, v):
    self.value = v
  def getval(self):
    return self.value


class PyfhelStub():
  def __init__(self):
    """Create an instance of Pyfhel"""
    pass

  def keyGen(self, run_params):
    """Create the key used during the encryption."""
    self._p = run_params["p"]

  def encrypt(self, PyPtxt: ptxt, fill=0):
    """Encrypt a PyPtxt object into a PyCtxt object."""
    return PyCtxtStub(ptxt.getval(), ptxt.getPyfhel(), ptxt.getPtxtLen())

  def decrypt(self, PyCtxt: ctxt) -> PyCtxt:
    """Decrypt a PyCtxt object into a List of values."""
    return PyPtxtStub(ctxt.getval(), self)

  def duplicate(self, PyCtxt: c) -> PyCtxt:
    """DUPLICATE a PyCtxt with all its parameters, useful to keep originals in ops."""
    return c.copy()

  def add(self, PyCtxt: a, PyCtxt: b):
    """ADD two PyCtxt objects for each ID in both."""
    _sum_ = [(aa + bb) % self._p for a, b in zip(a,b)]
    return PyCtxtStub(_sum_, self, ctxt.getLen())

  def mult(self, PyCtxt: a, PyCtxt: b):
    """MULTiply two PyCtxt objects for each ID in both."""
    _sum_ = a.getval() + b.getval()
    _sum_ %= self._p
    return PyCtxtStub(_sum_, self, ctxt.getLen())

  def mult3(self):
    """MULTIPLY 3 PyCtxt objects for each ID in both."""
    pass

  def scalarProd(self):
    """SCALAR PRODuct between two PyCtxt objects for each ID in both."""
    pass

  def square(self):
    """SQUARE each cyphertext inside PyCtxt ctxt for each ID in it."""
    pass

  def cumSum(self):
    """CUMSUM Cumulative sum over all the values in the cyphertext."""
    pass

  def cube(self):
    """CUBE each cyphertext inside PyCtxt ctxt for each ID in it."""
    pass

  def negate(self):
    """NEGATE each cyphertext inside PyCtxt ctxt for each ID in it."""
    pass

  def equalsTo(self):
    """COMPARE two PyCtxt objects for each ID in both."""
    pass

  def rotate(self):
    """ROTATE each cyphertext inside PyCtxt ctxt for each ID in it."""
    pass

  def shift(self):
    """SHIFT each cyphertext inside PyCtxt ctxt for each ID in it."""
    pass

  def saveEnv(self):
    """Saves the environment into a .aenv file."""
    raise NotImplemented("not implemented")

  def restoreEnv(self):
    """Restores the environment from a .aenv file."""
    raise NotImplemented("not implemented")

