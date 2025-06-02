import matplotlib.pyplot as plt

#Lista de produtos
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"]

#Lista de preços
precos = [3500, 80, 150, 900, 600]

#Criando gráfico de barras
plt.bar(produtos, precos, color="red")

#Titulos e rótulos
plt.title("Preços dos Produtos")
plt.xlabel("Produtos")
plt.ylabel("Preço ($)")

#Exibindo o gráfico
plt.show()