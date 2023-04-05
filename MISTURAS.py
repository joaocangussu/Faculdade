size=int(input("Informe quantos m² você deseja pintar:"))
litro=size/6
# LATAS
lata=litro/18
if litro%18!=0:
    lata=litro//18
    lata+=1  
# GALÃO
galao=litro/3.6
if litro%3.6!=0:
    galao=litro//3.6
    galao+=1
# MISTURA
misturalata= int(litro/18)
misturagalao= int(litro - (misturalata*18))/3.6
if litro - (misturalata*18)%3.6!=0:
    misturagalao+=1
    precom= (misturalata*80) + (misturagalao*25)
    precog= galao*25
    precol= lata*80
if precog<precol and precog<precom:
    print("Você pode pagar R${:.0f} por {:.0f} galões de tinta.".format(precog,galao))
elif precol<precog and precol<precom:
    print("Você pode pagar R${:.0f} por {:.0f} latas de tinta.".format(precol,lata))
else:
    print("Você pode pagar R${:.0f} por {:.0f} latas e {:.0f} galões de tinta.".format(precom,misturalata,misturagalao))

#6m² = 1L
#galao= 3,6L custa R$25
#lata= 18L custa R$80







