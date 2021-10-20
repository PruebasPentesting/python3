import pygame
import time
pygame.init()

out = False
end = False
anchura, altura = 400, 200
window = pygame.display.set_mode((anchura, altura))

while not out:
    events = pygame.event.get()
    window.fill((255, 0, 0))
    for event in events:
        if event.type == pygame.QUIT:
            out = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                out = True
    


    txt = open("passlst.txt", "r")
    content = txt.readlines()

    last_line = "10000"

    #print (content)
    font = pygame.font.SysFont("comicsans", 50)

    """for line in content:
        if last_line in line.strip():
            print("line is " + last_line)
            out = True

        else:
            print("not " + line.strip())"""

   

    while not end:

        for line in content:
            word = font.render(line, False, (0, 0, 0))
            anchuraTexto, alturaTexto = word.get_width(), word.get_height() 


            window.fill((255, 0, 0))

            if last_line in line:
                end = True

            else:
                window.blit(word, (((anchura - anchuraTexto)/2),((altura - alturaTexto)/2)))

       
            
            if end:
                break
            else:
                pygame.display.flip()

            
    
    if end:
        found = font.render(str("password = " + last_line), False, (0, 0, 0))
        anchuraTexto, alturaTexto = found.get_width(), found.get_height() 
        window.blit(found, (((anchura - anchuraTexto)/2, (altura - alturaTexto)/2)))

    pygame.display.flip()
    
txt.close()
