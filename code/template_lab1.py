
# Richtlijnen voor de code:
# - De signatuur van de get_entropy functie mag niet gewijzigd worden aangezien de code automatische getest zal worden. 
# - Jullie mogen zeker andere functies, of zelfs classen aanmaken. (Zorg er voor dat als we de code debuggen, het duidelijk is wat er gebeurt. Tip: maak gebruik van type-hinting, zie https://docs.python.org/3/library/typing.html)
# - Als je code wenst op te roepen, kan je dit doen in de main() functie. Dit zorgt ervoor dat als we de code importeren, er geen code begint uit te voeren buiten onze controle.
# - Het gebruik van globale variabelen is dan wel zeker toegelaten.
# - Jullie zijn vrij om externe libraries te gebruiken (numpy, pandas, scipy, ...) zolang deze niet de kern van het algorithme voor jullie uitrekenen. (Bijvoorbeeld, als er gevraagd wordt een sin-functie te implementeren, mag je uiteraard numpy.sin() niet oproepen.) 
# Veel succes!

import numpy as np
import matplotlib.pyplot as plt

def drawplot(path:str, title:str, xname:str, yname:str, ax) -> None:
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='silver')
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(xname) 
    plt.ylabel(yname)
    plt.title(title)
    plt.legend()
    plt.savefig(f"{path}.eps", format='eps')
    plt.savefig(f"{path}.png", format='png')
    plt.show()

def onlyletters(data:list[str]) -> list[str]:
    return list(filter(str.isascii, filter(str.isalpha, ''.join(data).upper())))

def get_entropy(data: list, memory: int = 0) -> float:
    # Vraag 2
    wsj, cnt_wsj = np.unique(np.lib.stride_tricks.sliding_window_view(data, memory + 1, axis=0), return_counts=True, axis=0)
    probs_wsj = cnt_wsj / np.sum(cnt_wsj)
    
    wsb, cnt_wsb = np.unique(np.lib.stride_tricks.sliding_window_view(data[:-1], memory, axis=0), return_counts=True, axis=0)
    probs_wsb = cnt_wsb / np.sum(cnt_wsj)

    probs_wsc = np.zeros(len(wsj))
    i_wsb = 0
    for i,w in enumerate(wsj):
        if not np.all(wsb[i_wsb] == w[:-1]):
            i_wsb += 1
        probs_wsc[i] = probs_wsj[i]/probs_wsb[i_wsb]

    return -np.sum(probs_wsj*np.log2(probs_wsc))

def main():
    pass

if __name__ == "__main__":
    main()
