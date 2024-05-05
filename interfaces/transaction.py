from abc import ABC, abstractclassmethod, abstractmethod

class Transaction(ABC):
  @property
  @abstractmethod
  def value(self):
    pass

  @abstractclassmethod
  def register(self, account):
    pass
  
  