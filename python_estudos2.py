vendas_2025 = {"jan": 1000, "fev": 2000, "mar": 3000, "abr": 5000, "mai": 5000, "jun": 6000, "jul": 7000, "ago": 8000, "set": 9000, "out": 10000, "nov": 11000, "dez": 12000}

vendas_2026 = {"jan": 1500, "fev": 2500, "mar": 3500, "abr": 4500, "mai": 5500, "jun": 6500, "jul": 7500, "ago": 8500, "set": 9500, "out": 10500, "nov": 11500, "dez": 12500}

def calcular_imposto(vendas):
    imposto_total = 0
    
    for mes, valor in vendas.items():
        if valor > 5000:
            taxa = 0.2
        elif valor > 3000:
            taxa = 0.15
        elif valor > 1000:
            taxa = 0.1
        else:
            taxa = 0.05

        imposto_mes = valor * taxa

        porcentagem = f"{taxa:.2%}".replace(".", ",")
        valor_formatado = f"{imposto_mes:.2f}".replace(".", ",")

        print(f"{mes}: R${valor_formatado} ({porcentagem})")

        imposto_total += imposto_mes

    return imposto_total

total_2025 = calcular_imposto(vendas_2025)
print(f"Total 2025: R${str(round(total_2025,2)).replace('.', ',')}")

total_2026 = calcular_imposto(vendas_2026)
print(f"Total 2026: R${str(round(total_2026,2)).replace('.', ',')}")

vendas = {
    2025: {"jan": 1000, "fev": 2000, "mar": 3000, "abr": 5000, "mai": 5000, "jun": 6000, "jul": 7000, "ago": 8000, "set": 9000, "out": 10000, "nov": 11000, "dez": 12000},
    2026: {"jan": 1500, "fev": 2500, "mar": 3500, "abr": 4500, "mai": 5500, "jun": 6500, "jul": 7500, "ago": 8500, "set": 9500, "out": 10500, "nov": 11500, "dez": 12500}
}


def calcular_imposto(vendas_ano):
    imposto_total = 0
    detalhes = {}

    for mes, valor in vendas_ano.items():
        if valor > 5000:
            taxa = 0.2
        elif valor > 3000:
            taxa = 0.15
        elif valor > 1000:
            taxa = 0.1
        else:
            taxa = 0.05

        imposto = valor * taxa

        detalhes[mes] = {
            "faturamento": valor,
            "taxa": taxa,
            "imposto": imposto
        }

        imposto_total += imposto

    return imposto_total, detalhes

def gerar_relatorio(vendas):
    for ano, dados in vendas.items():
        print(f"\n===== RELATÓRIO {ano} =====")

        total, detalhes = calcular_imposto(dados)

        maior_mes = max(detalhes, key=lambda m: detalhes[m]["imposto"])
        menor_mes = min(detalhes, key=lambda m: detalhes[m]["imposto"])

        for mes, info in detalhes.items():
            faturamento = f"{info['faturamento']:.2f}".replace(".", ",")
            imposto = f"{info['imposto']:.2f}".replace(".", ",")
            taxa = f"{info['taxa']:.0%}".replace(".", ",")

            print(f"{mes.upper()} | Fat: R${faturamento} | Imp: R${imposto} | Taxa: {taxa}")

        total_formatado = f"{total:.2f}".replace(".", ",")
        print(f"\nTotal de imposto: R${total_formatado}")

        print(f"Maior imposto: {maior_mes.upper()}")
        print(f"Menor imposto: {menor_mes.upper()}")
    
gerar_relatorio(vendas)








import os

print(os.getcwd())

lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

for nome_arquivo in lista_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
print(resposta)
dic_resposta = resposta.json()

for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]
    print(moeda, valor_moeda)
