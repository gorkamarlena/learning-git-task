# Shopping list app

shopping_list = {
"piekarnia" : ["chleb", "bułki", "pączek"],
"warzywniak" : ["marchew", "seler", "rukola", "sałata"],
}

for shop, products in shopping_list.items():
    print ("Ide do", shop.capitalize(), "i kupuje tu następujące rzeczy:",
        str(products).title())

piekarnia_products = len(shopping_list["piekarnia"])
warzywniak_products = len(shopping_list["warzywniak"])
sum = piekarnia_products + warzywniak_products

print("W sumie kupuję", sum,"produktów")

# Greetings to my Mentor :)