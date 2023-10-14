
from datetime import date
today = date.today()
masterResponse = popAsk('Iniciamos el proceso de declaracion en la SAT ahora?')
#La contraseña de tu SAT Virtual debe estar acá
password = ''
#Tu correo para enviar el formulario por correo
email = ''
#Tu fecha de cumpleaños
dateOfBirth =''
if not masterResponse:
    popError('Recuerda hacer tu declaracion de la SAT!')
else:
    click("1697265138552.png") 
    wait(1)
    type('Edge')
    type(Key.ENTER)
    click("1697265668886.png")
    type('https://declaraguate.sat.gob.gt/declaraguate-web/')
    type(Key.ENTER)
    wait("1697266204095.png")
    click("1697265787104.png")
    captcha = input('No pudimos validar el captcha, porfavor ingresalo:')
    click("1697266965960.png")
    type(captcha)
    click("1697267018949.png")
    wait(3)
    type(Key.PAGE_UP * 5)
    wait("1697267093816.png")
    click("1697267307320.png")
    type('103475664')
    type(Key.ENTER)
    wait(2)
    click("1697268919605.png")
    type(password)
    type(Key.ENTER)
    wait(2)
    type(Key.PAGE_DOWN)
    wait(3)
    click("1697271119785.png")
    wait(2)
    num = today.month
    if num == 1:
        click("1697271955075.png")
    elif num == 2:
        click("1697270824168.png")
    elif num == 3:
        click("1697271432345.png")
    elif num == 4:
        click("1697271474372.png")
    elif num == 5:
        click("1697271506846.png")
    elif num == 6:
        click("1697271552769.png")
    elif num == 7:
        click("1697271582599.png")
    elif num == 8:
        click("1697271637934.png")
    elif num == 9:
        click("1697271663205.png")
    elif num == 10:
        click(    "1697273371963.png")
    elif num == 11:
        click("1697271691514.png")
    else:
        click("1697271708164.png")

    click("1697273554692.png") 
    type(Key.PAGE_DOWN)
    wait(1)
    click("1697273087293.png")
    wait(3)    
    click("1697273736425.png")

    wait(3)
    click("1697273923367.png")
    type(email)
    click("1697274084572.png")
    click("1697274199876.png")
    wait("1697274229996.png")
    click("1697274247953.png")
    wait("1697274281348.png")
    click("1697274297497.png")
    type(dateOfBirth)
    wait(1)
    click("1697274391836.png")
    wait("1697274436506.png")
    click("1697274488992.png")
    
      
    
    
 
