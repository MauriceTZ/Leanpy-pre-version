from random import randint, random
import pygame, sys, numpy

TAMANO_PIEZA = 20   # Px.
LIMITE_MAPA = 20


# N_LARGO_GRID = 4

class Piece(pygame.sprite.RenderPlain):
    active: bool
    origen: pygame.Vector2

    def __init__(self, type: int | None = None, color: tuple[int, int, int] | None = None) -> None:
        super().__init__()
        self.active = True
        types = {
            0: ((0, 0), (1, 0), (2, 0), (3, 0)),
            1: ((0, 0), (1, 0), (0, 1), (1, 1)),
            2: ((0, 0), (1, 0), (2, 0), (0, 1)),
            3: ((0, 0), (1, 0), (2, 0), (1, 1))
        }

        if not color:
            color = (255 * random(), 255 * random(), 255 * random())

        if not type:
            type = randint(0, 3)

        for x, y in types[type]:
            sprite = pygame.sprite.Sprite()
            sprite.image = pygame.Surface((TAMANO_PIEZA - 1, TAMANO_PIEZA - 1))
            sprite.image.fill(color)
            sprite.rect = sprite.image.get_rect()
            sprite.rect.move_ip(x * TAMANO_PIEZA, y * TAMANO_PIEZA)
            self.add(sprite)
        self.origen = pygame.Vector2(x * TAMANO_PIEZA, y * TAMANO_PIEZA)

    def update(self) -> None:
        if self.active:
            for sp in self:
                sp.rect.move_ip(0, TAMANO_PIEZA)
            self.origen += (0, TAMANO_PIEZA)
        return super().update()

    def collide(self, other: pygame.sprite.RenderPlain):
        for sp in self:
            for other_sp in other:
                if sp.rect.colliderect(other_sp.rect):
                    return True
        return False

    def move_ip(self, x: float, y: float):
        for sp in self:
            sp.rect.move_ip(x * TAMANO_PIEZA, y * TAMANO_PIEZA)
        self.origen += (x * TAMANO_PIEZA, y * TAMANO_PIEZA)

    def getPos(self):
        return self.origen
        # return(self.sprites())
        # return pygame.Vector2(self.sprites()[0].rect.topleft) / TAMANO_PIEZA

    def rotar(self):
        for sp in self:
            # sp.rect.x, sp.rect.y = sp.rect.y, sp.rect.x
            
            pass




# class Pieza(pygame.sprite.Sprite):
#     # partes = []
#     active: bool

#     def __init__(self, tipo: int, color: tuple[int, int, int] | None = None) -> None:
#         super().__init__()
#         self.active = True
#         self.image = pygame.Surface((TAMANO_PIEZA * N_LARGO_GRID, TAMANO_PIEZA * N_LARGO_GRID))
#         self.image.set_colorkey((0,0,0))
#         self.rect = self.image.get_rect()
#         cuadrado = pygame.Surface((TAMANO_PIEZA - 1, TAMANO_PIEZA - 1))
#         if color:
#             cuadrado.fill(color)
#         else:
#             color = (255 * random(), 255 * random(), 255 * random())
#             cuadrado.fill(color)
#         if tipo == 0:   # Palo plano
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 2, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 3, TAMANO_PIEZA * 0))
#         elif tipo == 1: # Cuadrado
#             pass
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 1))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 1))
#         elif tipo == 2: # L
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 2, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 1))
#         elif tipo == 3: # esta forma culia rara _|_
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 0, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 2, TAMANO_PIEZA * 0))
#             self.image.blit(cuadrado, (TAMANO_PIEZA * 1, TAMANO_PIEZA * 1))
#         else:
#             raise Exception("BRO WTF ARE YOU DOING!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#         # super().__init__()
#         # self.partes = []
#         # self.image = pygame.Surface((200,200))
#         # self.rect = self.image.get_rect()
#         # # self.rect.center = origen
#         # self.rect.move(origen)
#         # self.origen = origen
#         # for punto in puntos:
#         #     cuadrado = pygame.Surface((45,45))
#         #     cuadrado.fill((255 * random(), 255 * random(), 255 * random()))
#         #     self.partes.append(punto)
#         #     self.image.blit(cuadrado, punto)


    
#     def update(self) -> None:
#         if self.active:
#             self.rect.move_ip(0, TAMANO_PIEZA)

#     def setPos(self, pos: pygame.Vector2) -> None:
#         self.rect.topleft = pos * TAMANO_PIEZA
#         print(self.rect.topleft)

# def createBlock(type: int):
#     out = numpy.zeros((4, 4), dtype=bool)
#     if type == 0:   # Palo plano
#         out[0, 0] = True
#         out[0, 1] = True
#         out[0, 2] = True
#         out[0, 3] = True
#     elif type == 1: # Cuadrado
#         out[0, 0] = True
#         out[0, 1] = True
#         out[1, 0] = True
#         out[1, 1] = True
#     elif type == 2: # L
#         out[0, 0] = True
#         out[0, 1] = True
#         out[0, 2] = True
#         out[1, 0] = True
#     elif type == 3: # esta forma culia rara _|_
#         out[0, 0] = True
#         out[0, 1] = True
#         out[0, 2] = True
#         out[1, 1] = True
#     return out

def main():

    pygame.display.init()
    clock = pygame.time.Clock()
    width, height = 800, 800
    pos_rel = 0.25, 0.25
    block_size = 30
    screen = pygame.display.set_mode((width, height))
    render = pygame.sprite.RenderPlain()
    periodo = 0.5
    
    listaPiezas: list[Piece] = []
    listaPiezasChocadas: list[Piece] = []


    # a = Piece(0)
    # b = Piece(1)
    # b.active = False
    # b.move_ip(1, 1)
    # listaPiezas.append(b)

    matrix = numpy.zeros((16, 8), dtype=bool)
    # forma = createBlock(3)
    # inx_forma = [0, 0]
    time = 0

    while True:
        screen.fill((197,197,197))
        # render.draw(screen)
        # a.draw(screen)
        if len([pieza for pieza in listaPiezas if pieza.active]) == 0:
            listaPiezas.append(Piece())
        for pieza in listaPiezas:
            pieza.draw(screen)
        # b.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("chao nos vimos")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    periodo = 0.1
                elif event.key == pygame.K_a:
                    listaPiezas.append(Piece())
                elif event.key == pygame.K_s:
                    lPiezasNoChocadas = [p for p in listaPiezas if p.active]
                    for pieza in lPiezasNoChocadas:
                        pieza.rotar()
                elif event.key == pygame.K_LEFT:
                    lPiezasChocadas = [p for p in listaPiezas if not p.active]
                    lPiezasNoChocadas = [p for p in listaPiezas if p.active]
                    for pieza in lPiezasNoChocadas:
                        pieza.move_ip(-1, 0)
                        for pc in lPiezasChocadas:
                            if pieza.collide(pc):
                                pieza.move_ip(1, 0)
                                continue
                elif event.key == pygame.K_RIGHT:
                    # [p.move_ip(1, 0) for p in listaPiezas if p.active]
                    lPiezasChocadas = [p for p in listaPiezas if not p.active]
                    lPiezasNoChocadas = [p for p in listaPiezas if p.active]
                    for pieza in lPiezasNoChocadas:
                        pieza.move_ip(1, 0)
                        for pc in lPiezasChocadas:
                            if pieza.collide(pc):
                                pieza.move_ip(-1, 0)
                                continue
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    periodo = 0.5
        
        
        # for y in range(forma.shape[0]):
        #     for x in range(forma.shape[1]):
        #         if forma[y, x]:
        #             matrix[inx_forma[0] + y, inx_forma[1] + x] = False

        fps = clock.get_fps()
        if fps != 0:
            time += 1 / fps
        
        if time > periodo:
            time = 0
            # render.update()
            # a.update()
            # b.update()
            # print(a.collide(b))
            # if a.collide(b):
            #     a.active = False
            #     a.move_ip(0, -1)
        
            lPiezasChocadas = [p for p in listaPiezas if not p.active]
            lPiezasNoChocadas = [p for p in listaPiezas if p.active]

            for pn in lPiezasNoChocadas:
                # pn.move_ip(0, 1)
                pn.update()
                if (pn.getPos() / TAMANO_PIEZA).y > LIMITE_MAPA:
                    pn.move_ip(0, -1)
                    pn.active = False
                    continue

                for pc in lPiezasChocadas:
                    if pn.collide(pc):
                        pn.move_ip(0, -1)
                        pn.active = False
                        break
            

            # for pieza in listaPiezas:
            #     pieza.update()
            #     for piezaChocada in listaPiezasChocadas:
            #         if pieza.collide(piezaChocada):
            #             print("CHOQUE")
            #             pieza.active = False
            #             pieza.move_ip(0, -1)
            #             listaPiezas.remove(pieza)
            #             listaPiezasChocadas.append(pieza)

            # print(a.rect.colliderect(b))
            # print("update")

            # inx_forma[0] += 1
        
        # for y in range(forma.shape[0]):
        #     for x in range(forma.shape[1]):
        #         try:
        #             if forma[y, x] and not matrix[inx_forma[0] + y, inx_forma[1] + x]:
        #                 matrix[inx_forma[0] + y, inx_forma[1] + x] = True
        #         except:
        #             print("Choque")
        #             matrix[inx_forma[0] + y - 2, inx_forma[1] + x] = True
        #             inx_forma = [0,0]


        
        
        # for y in range(matrix.shape[0]):
        #     for x in range(matrix.shape[1]):
        #         xpos = pos_rel[0] * width + block_size * x
        #         ypos = pos_rel[1] * height + block_size * y
        #         xpos_end = xpos + block_size
        #         ypos_end = ypos + block_size
        #         if matrix[y, x]:
        #             pygame.draw.rect(screen, (15,150,15), ((xpos, ypos),(block_size - 1, block_size - 1)))
        #         else:
        #             pygame.draw.rect(screen, (150,150,150), ((xpos, ypos),(block_size - 1, block_size - 1)))


        
        # for y in range(forma.shape[0]):
        #     for x in range(forma.shape[1]):
        #         if forma[y, x]:
        #             # if matrix[inx_forma[0] + y, inx_forma[1] + x]:
        #             xpos = pos_rel[0] * width + block_size * (inx_forma[1] + x)
        #             ypos = pos_rel[1] * height + block_size * (inx_forma[0] + y)
        #             if  xpos >= pos_rel[0] * width + block_size * (matrix.shape[1]) or \
        #                 ypos >= pos_rel[1] * height + block_size * (matrix.shape[0]): continue
        #             pygame.draw.rect(screen, (255,0,0), ((xpos, ypos),(block_size - 1, block_size - 1)))
                    
        pygame.display.update()
        clock.tick(165)




if __name__ == "__main__":
    main()