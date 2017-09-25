import gitlab

gl = gitlab.Gitlab('http://gitlab', email='root', password='kubernetes')
gl.auth()

# Create user
gl.users.create({'email': 'kedge@example.com',
                        'password': 'kubernetes',
                        'username': 'kedge',
                        'name': 'The Kedge Project'})
