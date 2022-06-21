#フレームレートとステップ時間
FPS=30
DT=1/FPS
#gravity
G=9.8

for i in range(n_count):
    #fouce
    f = m*G
    a = f/m 
    #integra ax sp
    vel += a*DT
    #integra sp pos
    y += vel * DT
    time += DT
