from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Flavio Cardoso', cpf='12345678901', email='flavio@cardoso.net',
                    phone='61-3345-4721')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'flavio@cardoso.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Flavio Cardoso',
                    '12345678901',
                    'flavio@cardoso.net',
                    '61-3345-4721']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)