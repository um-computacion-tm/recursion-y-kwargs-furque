import unittest


def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        match = True
        for arg in args:
            if arg not in value.values():
                match = False
                break
        if match:
            return key
    return 'No existe'

database = {
    '1': {
        'nombre1': 'Pablo',
        'nombre2': 'Diego',
        'apellido1': 'Ruiz',
        'apellido2': 'Picasso'
    },
    '2': {
        'nombre1': 'Joaquin',
        'apellido1': 'Furque'
    },
    '3': {
        'nombre1': 'Lionel',
        'nombre2': 'Andres',
        'nombre3': 'Gonzalo',
        'apellido1': 'Messi',
        'apellido2': 'Roccuzo'
    },
    '4': {
        'nombre1': 'Sebastian',
        'nombre2': 'Matias',
        'apellido1': 'Merino',
        'apellido2': 'Roldan'
    }    
    
}

print(buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database))
print(buscar_datos("Joaquin", "Furque", **database))
print(buscar_datos("Lionel", "Andres", "Gonzalo", "Messi", "Roccuzo", **database))

class TestPersona(unittest.TestCase):
    def test_1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, "1")
    
    def test_2(self):
        resultado = buscar_datos("Joaquin", "Furque", **database)
        self.assertEqual(resultado, "2")
    
    def test_3(self):
        resultado = buscar_datos("Lionel", "Andres", "Gonzalo", "Messi", "Roccuzo", **database)
        self.assertEqual(resultado, "3")

    def test_3(self):
        resultado = buscar_datos("Lionel", "Miguel", "Gonzalo", "Messi", "Roccuzo", **database)
        self.assertEqual(resultado, "No existe")

    def test_1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Martinez", **database)
        self.assertEqual(resultado, "No existe")

    def test_4(self):
        resultado = buscar_datos("Sebastian", "Matias", "Merino", "Roldan", **database)
        self.assertEqual(resultado, "4")       
    
    def test_4(self):
        resultado = buscar_datos("Sebastian", "Roberto", "Merino", "Roldan", **database)
        self.assertEqual(resultado, "No existe") 
    
    def test_2(self):
        resultado = buscar_datos("Joaquin", "Ñurfle", **database)
        self.assertEqual(resultado, "No existe") 


unittest.main()