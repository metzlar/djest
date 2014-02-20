djest
=====

Better tests for django

Example of testing a custom Admin form:

```python
from djest.admin import AdminCase
from yourapp.models import MyModel
	
class MyCase(AdminCase):
	
    def setUp(self):
      (
        self.user_name,
        self.user_pass,
        self.user
      ) = self.create_user(is_staff = True)

      self.new('example', MyModel, {
        'name': 'Example'
      })

    def test_example(self):
    
      self.assertTrue('example' in self)
      self.assertTrue(self['example'].name == 'Example')
      
      #login
      self.login(self.user_name, self.user_pass)
	        
      # go to the changelist page
      self.response = self.client.get(reverse('admin:yourapp_mymodel_changelist')
	        
      # count the no. of models on the page
      self.assert_result_count(1)
	        
      # add another one through the admin
      self.post_form(
        reverse('admin:yourapp_mymodel_add'),
        {'name': 'Another example instance'}
      )
		      
      # count again
      self.assert_result_count(2)
