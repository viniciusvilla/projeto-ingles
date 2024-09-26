import pygame
from PyQt5 import uic, QtWidgets

def tocar_som(letra):
    pygame.mixer.music.load(f'audio/som_{letra}.mp3')
    pygame.mixer.music.play()

def main():
    pygame.init()

    app = QtWidgets.QApplication([])
    tela = uic.loadUi('tela.ui')

    botoes = {
        'a': tela.botao_a,
        'b': tela.botao_b,
        'c': tela.botao_c,
        'd': tela.botao_d,
        'e': tela.botao_e,
        'f': tela.botao_f,
        'g': tela.botao_g,
        'h': tela.botao_h,
        'i': tela.botao_i,
        'j': tela.botao_j,
        'k': tela.botao_k,
        'l': tela.botao_l,
        'm': tela.botao_m,
        'n': tela.botao_n,
        'o': tela.botao_o,
        'p': tela.botao_p,
        'q': tela.botao_q,
        'r': tela.botao_r,
        's': tela.botao_s,
        't': tela.botao_t,
        'u': tela.botao_u,
        'v': tela.botao_v,
        'w': tela.botao_w,
        'x': tela.botao_x,
        'y': tela.botao_y,
        'z': tela.botao_z
    }

    for letra, botao in botoes.items():
        botao.clicked.connect(lambda _, l=letra: tocar_som(l))

    tela.show()
    app.exec()

if __name__ == "__main__":
    main()
