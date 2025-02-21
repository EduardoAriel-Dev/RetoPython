import random

n = random.randint(0,1)

class ProductsPrices():
    
    def __init__(self):
        self.price = []
        self.DiscountList = []
        self.DiscountOnlyList = []
        
        
    def PriceList(self,cantProduct,minPrice,maxPrice):
                
        for _ in range(cantProduct):
            rangeOfPrice = random.randint(minPrice,maxPrice)
            #rangeOfPrice = random.sample(range(minPrice,maxPrice+1),cantProduct)
            self.price.append(rangeOfPrice)
        
        lists =list(self.price)
        return lists

    def IsDiscount(self):   
        discountPrice = 0
        for d in self.price:
            if d < 0:
                self.DiscountList.append("IsDiscount")
                discountPrice += d
                self.DiscountOnlyList.append(d)
            else:
                self.DiscountList.append("IsNotDiscount")
        
        return {"Discount_list" : self.DiscountList,
                "Discount_price": discountPrice}
        
    def AveragePrice(self):
        average = 0
        discountAverage = 0
        for d in self.DiscountOnlyList:
            discountAverage += d
        
        discountAverage = discountAverage/len(self.DiscountOnlyList)     
        
        for p in self.price:
            average += p
        
        average = average/len(self.price)
        
        return {"DiscountAverage": discountAverage,
                "Average": average}
    
    def ExistPrice(self,price):
        
        return price in self.price
        
    def MaxAndMinPrice(self):
        maxPrice = max(self.price)
        indexMax = self.price.index(maxPrice)
        minPrice = min(self.price)
        indexMin = self.price.index(minPrice)
        
        return {
            "MaxPrice":maxPrice,"IndexMax":indexMax,
            "MinPrice":minPrice,"IndesMin":indexMin
            }
    
product = ProductsPrices()

#Generamos 10 precios entre -10 y 50 (incluyendo negativos para pruebas)
print("Lista de precios generada:")
print(product.PriceList(10, -10, 10))

#Verifico los descuentos
print("Resultados del descuento:")
print(product.IsDiscount())

#Verifico el promedio
print("Resultados del promedio:")
print(product.AveragePrice())

#Verifico si existe el precio
print("Existe el precio:")
print(product.ExistPrice(40))

#Verifico el precio maximo y minimo
print("El precio maximo es:")
print(product.MaxAndMinPrice())