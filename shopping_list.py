shopping_list = {
"piekarnia" : ["chleb", "bułki", "pączek"],
"warzywniak" : ["marchew", "seler", "rukola"],
}

for shop, products in shopping_list.items():
    print ("Ide do", shop.capitalize(), "i kupuje tu następujące rzeczy:",
        str(products).title())