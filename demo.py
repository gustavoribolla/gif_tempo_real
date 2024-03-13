import numpy as np
# Instalar a biblioteca cv2 pode ser um pouco demorado. Não deixe para ultima hora!
import cv2 as cv

def criar_indices(min_i, max_i, min_j, max_j):
    import itertools
    L = list(itertools.product(range(min_i, max_i), range(min_j, max_j)))
    idx_i = np.array([e[0] for e in L])
    idx_j = np.array([e[1] for e in L])
    idx = np.vstack( (idx_i, idx_j) )
    return idx

def run():
    # Essa função abre a câmera. Depois desta linha, a luz de câmera (se seu computador tiver) deve ligar.
    cap = cv.VideoCapture(0)

    # Aqui, defino a largura e a altura da imagem com a qual quero trabalhar.
    # Dica: imagens menores precisam de menos processamento!!!
    width = 480
    height = 640
    theta = 0
    vel = 0.05

    # Talvez o programa não consiga abrir a câmera. Verifique se há outros dispositivos acessando sua câmera!
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    # Esse loop é igual a um loop de jogo: ele encerra quando apertamos 'q' no teclado.
    while True:
        # Captura um frame da câmera
        ret, frame = cap.read()

        # A variável `ret` indica se conseguimos capturar um frame
        if not ret:
            print("Não consegui capturar frame!")
            break

        # A variável image é um np.array com shape=(width, height, colors)
        image = np.array(frame).astype(float)/255
        image_ = np.zeros_like(image)

        # Mudo o tamanho do meu frame para reduzir o processamento necessário
        # nas próximas etapas
        frame = cv.resize(frame, (width,height), interpolation =cv.INTER_AREA)

        Xd = criar_indices(0, width, 0, height)
        Xd = np.vstack ((Xd,np.ones(Xd.shape[1])))

        T = np.array([[1, 0, - (width/2)], [0, 1, - (height/2)], [0, 0, 1]]) 

        # Definindo o ângulo e a matriz
        theta += vel
        A = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
        
        T_ = np.linalg.inv(T)

        B = T_ @ A @ T
        C = np.linalg.inv(B) @ Xd

        Xd = Xd.astype(int)
        C = C.astype(int)

        filtro = (C[0,:] >= 0) & (C[0,:] < width) & (C[1,:] >= 0) & (C[1,:] < height)
        Xd = Xd[:,filtro]
        C = C[:,filtro]

        Xd[0,:] = np.clip(Xd[0,:], 0, width)
        Xd[1,:] = np.clip(Xd[1,:], 0, height)

        image_[Xd[0,:], Xd[1,:], :] = image[C[0,:], C[1,:], :]

        # Agora, mostrar a imagem na tela!
        cv.imshow('Minha Imagem!', image_)
        
        # Se aperto 'q', encerro o loop
        if cv.waitKey(1) == ord('q'):
            break

    # Ao sair do loop, vamos devolver cuidadosamente os recursos ao sistema!
    cap.release()
    cv.destroyAllWindows()

run()