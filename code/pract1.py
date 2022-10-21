import numpy as np

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