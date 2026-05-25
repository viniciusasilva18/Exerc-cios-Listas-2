produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

# O enumerate traz o índice (i) e o nome do produto ao mesmo tempo
for i, produto in enumerate(produtos):
    venda_2019 = vendas2019[i]
    venda_2020 = vendas2020[i]
    
    # Verifica se vendeu mais em 2020 do que em 2019
    if venda_2020 > venda_2019:
        # Calcula o crescimento percentual
        crescimento = (venda_2020 / venda_2019) - 1
        
        print(f"Produto: {produto.title()}")
        print(f"  Vendas 2019: {venda_2019} | Vendas 2020: {venda_2020}")
        print(f"  Crescimento: {crescimento:.2%}")
        print("-" * 40)