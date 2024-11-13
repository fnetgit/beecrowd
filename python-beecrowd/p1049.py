lista = {
    ('vertebrado', 'mamifero', 'onivoro') :'homem',
    ('vertebrado', 'mamifero', 'herbivoro') :'vaca',
    ('vertebrado', 'ave', 'onivoro') :'pomba',
    ('vertebrado', 'ave', 'carnivoro') :'aguia',
    ('invertebrado', 'inseto', 'hematofago') :'pulga',
    ('invertebrado', 'inseto', 'herbivoro') :'lagarta',
    ('invertebrado', 'anelideo', 'hematofago') :'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro') :'minhoca',
}
entrada1 = input()
entrada2 = input()
entrada3 = input()

print(lista[(entrada1, entrada2, entrada3)])