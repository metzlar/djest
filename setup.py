from setuptools import setup # pragma: no cover 

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()] # pragma: no cover

setup(name='Djest',
      version='0.1',
      py_modules=['djest'],
      cmdclass={'upload':lambda x:None},
      install_requires=[
          'django',
      ],
      dependency_links=REQUIREMENTS,
      
      )# pragma: no cover 
 
 