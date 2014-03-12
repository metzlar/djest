from djest import BaseCase

from django.contrib.auth.models import User, Group


class AdminCase(BaseCase):
    def assert_result_count(self, n):
        try:
            self.assertEqual(
                self.response.context['cl'].result_count,
                n
            )
        except KeyError:
            self.wout()
            self.assertEqual(-1, n)

    def assert_not_authorized(self):
        try:
            self.assertEqual(
                self.response.status_code,
                403
            )
        except AssertionError:
            self.wout()
            raise
    
    def login(self, user_name, user_pass):
        self.response = self.client.login(
            username = user_name,
            password = user_pass
        )
        return self.response

    def logout(self):
        self.response = self.client.logout()
        return self.response

    def reverse(self, name, *args, **kwargs):
        if not ':' in name:
            name = 'admin:%s' % name
        elif name[0] == ':':
            name = name[1:]
        return super(AdminCase, self).reverse(
            name, *args, **kwargs)
        
    def get_or_create_group(self, name):
        group, created = Group.objects.get_or_create(name=name)
        return group
        
    def create_user(self, groups=None, do_login=False, **kwargs):
        user_name = self.uuid4()
        user_pass = self.uuid4()

        user = User.objects.create_user(
            user_name,
            '%s@djest.generated' % user_name,
            user_pass
        )

        for group in groups or []:
            user.groups.add(group)

        for k, v in kwargs.iteritems():
            setattr(user, k, v)

        user.save()

        if do_login:
            self.login(user_name, user_pass)

        self[user_name] = user

        return user_name, user_pass, user