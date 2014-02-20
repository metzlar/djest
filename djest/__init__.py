from django.test import TestCase

from uuid import uuid4


class BaseCase(TestCase, dict):

    def __init__(self, *args, **kwargs):
        super(BaseCase, self).__init__(*args, **kwargs)

    def nop(*args, **kwargs):
        # use for mocking
        # don't do anything
        pass
        
    def new(self, name, klass, m_kwargs ):
        if name in self:
            raise ValueError('Model already exists %s' % name)
        m = klass(**m_kwargs)
        m.save()
        self[name] = m
        return m
    
    def uuid4(self):
        return uuid4().hex