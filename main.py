import numpy as np
import cv2 

def definir_dimensoes(imagem_bruta, n_visoes, n_visoes_v):
    altura_total, largura_total, canais = imagem_bruta.shape
    s_dim = altura_total // n_visoes
    t_dim = largura_total // n_visoes_v
    return s_dim, t_dim

def processar_vissoes(imagem_bruta, n_visoes_u, n_visoes_v, s_dim, t_dim):
    lista_de_visoes = []
    for u in range(n_visoes_u):
        for v in range(n_visoes_v):
            start_s = u * s_dim
            end_s = start_s + s_dim
            start_t = v * t_dim
            end_t = start_t + t_dim

            visao_atual =imagem_bruta[start_s:end_s, start_t:end_t]
            q_factor = 20
            visao_quantizada = np.round(visao_atual / q_factor) * q_factor
            visao_quantizada = visao_quantizada.astype(np.uint8)
            lista_de_visoes.append(visao_quantizada)
    bloco_4d = np.array(lista_de_visoes)
    return bloco_4d

img = cv2.imread('sua_imagem')
s, t = definir_dimensoes(img, 9, 9)
bloco_4d = processar_vissoes(img, 9, 9, s, t)

np.savez_compressed('meu_lightfield_final.npz', dados_4d=bloco_4d)

print("Arquivo gerado com sucesso!")