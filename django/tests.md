classe exemplo de teste

```python
from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    # o metódo setUp roda automaticamente antes de cada teste e colocar as
    # vars que vc vai precisar dentro de self é a forma de vc torna-la global na classe
    def setUp(self):
        # o client é uma ferramenta do django capaz de fazer requests no projeto para fins de teste
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return code 200""" # docstring serve para descrever o teste
        self.assertEqual(200, self.response.status_code) # é igual?

    def test_template(self):
        """Must use subscription_form.html"""
        self.assertTemplateUsed(
            self.response, 'subscription_form.html') # é esse template usado?

    def test_html(self):
        """Html must contain tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6) # contem isso no html? esse numerop de vezes?
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf_token(self):
        """Html must contain csrf token"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')
```
