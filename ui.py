from flet import *
import flet 
import os
from main import download_file

WidthB=980
HeightB=650

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.minecraft//mods"
link = "https://github.com/Halosesparta13/Lucky-World-Launcher/raw/main/Part%201.zip"


body = Container(
    Stack([
        #BACKGROUND IMAGE
        Image(
            "assets/background_1.png",
            width=WidthB, #Puede ser tmb 1200 px
            height=HeightB,
            top=0,
            fit=ImageFit.COVER
        ),
        #logo
        Image(
            "assets/logo.png",
            height=300,
            left= 30
            
        ),
        #MARCO CONO ELEMENTOS
        Image(
            "assets/marco.png",
            height = 270,
            width = 860,
            border_radius=border_radius.all(10),
            top = 325,
            fit=ImageFit.FILL,
            left = 50,           
        ),
        Container(
            bgcolor="red",
            height= 60,
            width=150,
            content = Text("DESCARGAR",size=18,weight=FontWeight.BOLD),
            margin=10,
            padding=10,
            alignment=alignment.center,
            border_radius=10,
            ink=False,
            top=470,
            left = 400,
            on_click=lambda e: download_file(link, minecraft_directory),
        ),
        #descripcion
        Container(
            height= 100,
            width=450,
            content = Text("¡Este es el launcher de Luckyworld! Aquí se actualizará a tiempo real los archivos de los Mods y RS",size=18,font_family="Minecraft",text_align="center"),
            margin=10,
            padding=10,
            alignment=alignment.center,
            border_radius=10,
            top = 350,
            ink=False,
            left = 250,
        ),
        ##Container(
           # content=Text("Clickable with Ink"),
           # margin=10,
           # padding=10,
          #  alignment=alignment.center,
          #  bgcolor=colors.CYAN_200,
          #  width=150,
          #  height=150,
          #  border_radius=10,
          #  ink=True,
          #  on_click=lambda e: print("Clickable with Ink clicked!"),
        ##),
        Row([
            Text(
                "Version Beta 0.6.0 ",
                color="white",
                size=25,
                weight="bold",
                opacity=0.5,
            ),
        ],
        alignment=MainAxisAlignment.END,
    ),
    ]),
    width= WidthB,
    height= HeightB
)

#propiedades de la 
def main(page: Page):
    page.horizontal_alignment= "center"
    BG = '#FFE382'
    page.title = "Lucky World Launcher (BETA)"
    page.window_width = WidthB
    page.window_height = HeightB
    page.window_max_width = WidthB
    page.window_max_height = HeightB
    page.fonts = {
        "Minecraft": "assets/Minecraft.otf",
        "Minecraft-Bold": "assets/Minecraft-Bold.otf"
    }
    page.padding = 0
    page.add(
        body,
    )
    

flet.app(target=main)
