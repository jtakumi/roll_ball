import pyxel

#parameters
WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16


#フレームレートとステップ時間
FPS=60
DT=1/FPS
#gravity
G=9.8

class Vec2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class cat:
    def __init__(self,img_id):
        self.pos=Vec2(0,0)
        self.vec=0
        self.vel=0
        self.weight=1
        self.time=0
        self.img_cat=img_id

    def update(self,x,y,dx):
        self.pos.x=x
        self.pos.y=y
        self.vec=dx

class App:
    def __init__(self):
        self.IMG_ID0_X=60
        self.IMG_ID0_Y=65
        self.IMG_ID0=0
        self.IMG_ID1 = 1

        pyxel.init(WINDOW_W,WINDOW_H,fps = FPS)
        pyxel.image(self.IMG_ID0).load(0,0,"assets/pyxel_logo_38x16.png")
        pyxel.image(self.IMG_ID1).load(0,0,"assets/cat_16x16.png")

        pyxel.mouse(True)

        #instance
        self.Cats=[]

        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #cat control]
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            new_cat = cat(self.IMG_ID1)

            new_cat.update(pyxel.mouse_x,pyxel.mouse_y,new_cat.vec)
            self.Cats.append(new_cat)

        cat_count =len(self.Cats)
        for i in range(cat_count):
            if self.Cats[i].pos.y < WINDOW_H:
                #fouce
                f = self.Cats[i].weight *  + 10**2
                a = f/ self.Cats[i].weight
                #integra ax sp
                self.Cats[i].vel += a*DT
                #integra sp pos
                self.Cats[i].pos.y += self.Cats[i].vel * DT
                self.Cats[i].time += DT
                #cat update
                self.Cats[i].update(self.Cats[i].pos.x,
                                    self.Cats[i].pos.y,
                                    self.Cats[i].vec)
            else:
                del self.Cats[i]
                break

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50,40,"I would like to FIRE.\n but I wanna no get fire.",pyxel.frame_count % 16)
        pyxel.blt(self.IMG_ID0_X,self.IMG_ID0_Y,self.IMG_ID0,0,0,38,16)

        #draw cat
        for cats in self.Cats:
            pyxel.blt(cats.pos.x,cats.pos.y,cats.img_cat,0,0,CAT_W,CAT_H,5)

App()



