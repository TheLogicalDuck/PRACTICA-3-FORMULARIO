import flet as ft
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "JuegoQuizODS")
MONGO_COL = os.getenv("MONGO_COL", "Jugadores")


def main(page: ft.Page):
    page.title = "Quiz ODS 🌍"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    coleccion = db[MONGO_COL]

    preguntas =[
        # --- PREGUNTAS ORIGINALES (1-10) ---
        {
            "pregunta": "¿Qué significan las siglas ODS?",
            "opciones":[
                "Objetivos de Desarrollo Sostenible",
                "Organización de Desarrollo Social",
                "Objetivos de Desarrollo Social",
                "Organización de Desarrollo Sustentable"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Cuántos ODS existen?",
            "opciones": ["10", "12", "17", "20"],
            "respuesta": 2
        },
        {
            "pregunta": "¿Qué busca el ODS 1?",
            "opciones":[
                "Fin de la pobreza",
                "Educación de calidad",
                "Acción por el clima",
                "Igualdad de género"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Cuál ODS promueve la educación para todos?",
            "opciones":[
                "ODS 3",
                "ODS 4",
                "ODS 5",
                "ODS 6"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué ODS se relaciona con el cuidado del planeta?",
            "opciones":[
                "ODS 13 Acción por el clima",
                "ODS 8 Trabajo decente",
                "ODS 4 Educación",
                "ODS 16 Justicia"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué ODS promueve la igualdad entre hombres y mujeres?",
            "opciones":[
                "ODS 5 Igualdad de género",
                "ODS 7 Energía limpia",
                "ODS 9 Industria",
                "ODS 11 Ciudades"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué ODS busca proteger la vida marina?",
            "opciones":[
                "ODS 14 Vida submarina",
                "ODS 15 Vida terrestre",
                "ODS 11 Ciudades sostenibles",
                "ODS 6 Agua limpia"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué ODS busca garantizar agua limpia y saneamiento?",
            "opciones":[
                "ODS 6",
                "ODS 7",
                "ODS 10",
                "ODS 12"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué ODS promueve energía limpia?",
            "opciones":[
                "ODS 7 Energía asequible y no contaminante",
                "ODS 3 Salud",
                "ODS 2 Hambre cero",
                "ODS 9 Industria"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Cuál es el objetivo principal de los ODS?",
            "opciones":[
                "Mejorar el planeta y la vida de las personas",
                "Solo mejorar la economía",
                "Construir más ciudades",
                "Reducir la tecnología"
            ],
            "respuesta": 0
        },
        
        # --- PREGUNTAS NUEVAS BASADAS EN EL INFORME MÉXICO 2024 (11-30) ---
        {
            "pregunta": "¿A qué lenguas indígenas fue traducido el 4° Informe Nacional Voluntario de México?",
            "opciones":[
                "Zapoteco y Mixteco",
                "Náhuatl y Maya",
                "Otomí y Purépecha",
                "Totonaco y Tzotzil"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "De 2018 a 2022, ¿cuántas personas en México salieron de la condición de pobreza multidimensional?",
            "opciones":[
                "Más de 1 millón",
                "Más de 3 millones",
                "Más de 5 millones",
                "Más de 10 millones"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿Qué programa es considerado el esfuerzo de reforestación productiva más grande del mundo?",
            "opciones":[
                "Producción para el Bienestar",
                "Sembrando Vida",
                "Jóvenes Construyendo el Futuro",
                "Original"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué sistema agrícola sostenible impulsa el programa Sembrando Vida?",
            "opciones":[
                "Monocultivo intensivo",
                "Milpa Intercalada con Árboles Frutales (MIAF)",
                "Cultivo hidropónico exclusivo",
                "Tala y quema"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué busca resolver el programa 'Jóvenes Construyendo el Futuro'?",
            "opciones":[
                "La exclusión laboral y social de las juventudes",
                "La falta de universidades públicas",
                "El acceso a vivienda para jóvenes",
                "La migración al extranjero"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué porcentaje de cumplimiento de la Agenda 2030 reportó México en 2023 según la ONU?",
            "opciones":[
                "45.5%",
                "69.7%",
                "85.2%",
                "99.1%"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Cuál es el movimiento en defensa de los derechos colectivos y contra el plagio de las comunidades artesanas?",
            "opciones":[
                "Artesanía Mexa",
                "Raíces Vivas",
                "Original",
                "Manos Indígenas"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿En qué estado opera la Escuela Técnica Roberto Rocca, impulsada por la empresa Ternium?",
            "opciones":[
                "Puebla",
                "Baja California",
                "Nuevo León",
                "Yucatán"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿Qué significan las siglas NODESS en México?",
            "opciones":[
                "Nodos de Desarrollo Sostenible y Salud",
                "Nodos de Impulso a la Economía Social y Solidaria",
                "Núcleos de Organización de Empresas Sociales",
                "Nuevas Oportunidades de Desarrollo Sostenible"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿En qué estado de México nació la Unión de Cooperativas Tosepan Titataniske?",
            "opciones":[
                "Chihuahua",
                "Chiapas",
                "Puebla",
                "San Luis Potosí"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿Cómo se llama el modelo de 'vida buena' que construye la cooperativa Tosepan?",
            "opciones":[
                "Yeknemilis",
                "Crecimiento exponencial",
                "Industrialización agraria",
                "Monopolio comercial"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué indicador económico se redujo en México de 2016 a 2022, reflejando menor desigualdad?",
            "opciones":[
                "El Índice de Gini",
                "La tasa de natalidad",
                "El Producto Interno Bruto",
                "La inversión extranjera"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Qué plataforma oficial recopila la información cuantitativa de los avances de México en los ODS?",
            "opciones":[
                "CONEVAL",
                "SIODS",
                "BANXICO",
                "SAT"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué porcentaje del poder adquisitivo del salario mínimo se recuperó en México entre 2018 y 2024?",
            "opciones":[
                "10%",
                "50%",
                "110%",
                "200%"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿A cuántos jóvenes ha beneficiado históricamente el programa 'Jóvenes Construyendo el Futuro' hasta 2023?",
            "opciones":[
                "Medio millón",
                "1 millón",
                "Más de 2.8 millones",
                "5 millones"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿Qué especie nativa cultiva la cooperativa Tosepan para producir miel y derivados?",
            "opciones":[
                "Abeja africana",
                "Abeja europea",
                "Pisilnekmej (abeja chiquita sin aguijón)",
                "Abeja reina asiática"
            ],
            "respuesta": 2
        },
        {
            "pregunta": "¿Qué institución pública en México es responsable de procesar y analizar los datos estadísticos y geográficos?",
            "opciones":[
                "INEGI",
                "CONEVAL",
                "INAES",
                "SEMARNAT"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿Cuál es la frase del Plan Nacional de Desarrollo vinculada al principio de 'no dejar a nadie atrás'?",
            "opciones":[
                "Por el bien de todos, primero los pobres",
                "Crecimiento a toda costa",
                "Austeridad extrema",
                "Desarrollo industrial rápido"
            ],
            "respuesta": 0
        },
        {
            "pregunta": "¿A qué ODS contribuye el programa 'Original' al fomentar la autonomía económica de las mujeres artesanas?",
            "opciones":[
                "ODS 14 Vida submarina",
                "ODS 5 Igualdad de género",
                "ODS 7 Energía asequible",
                "ODS 13 Acción por el clima"
            ],
            "respuesta": 1
        },
        {
            "pregunta": "¿Qué significa 'Tosepan Titataniske' en lengua náhuatl?",
            "opciones":[
                "Tierra fértil",
                "Mujeres unidas",
                "Unidos Venceremos",
                "Agua limpia"
            ],
            "respuesta": 2
        }
    ]

    indice = 0
    puntaje = 0
    nombre_jugador = ""

    titulo = ft.Text(
        "Quiz sobre los ODS 🌍",
        size=28,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )


    progreso = ft.Text(value=f"Pregunta 1 de {len(preguntas)}", size=16)

    jugador_texto = ft.Text(value="Jugador:", size=18)

    puntaje_texto = ft.Text(
        value="Puntaje: 0",
        size=18,
        weight=ft.FontWeight.BOLD
    )

    pregunta_texto = ft.Text(
        value="",
        size=22,
        weight=ft.FontWeight.BOLD
    )

    opciones = ft.RadioGroup(content=ft.Column(spacing=10))

    mensaje = ft.Text(value="", color=ft.Colors.RED_400)

    nombre_input = ft.TextField(label="Escribe tu nombre", width=300)

    mensaje_inicio = ft.Text(value="", color=ft.Colors.RED_400)

    def guardar_resultado():
        documento = {
            "nombre": nombre_jugador,
            "puntos_totales": puntaje
        }

        coleccion.insert_one(documento)

    def cargar_pregunta():
        nonlocal indice

        if indice < len(preguntas):
            pregunta_actual = preguntas[indice]

            progreso.value = f"Pregunta {indice+1} de {len(preguntas)}"
            jugador_texto.value = f"Jugador: {nombre_jugador}"
            puntaje_texto.value = f"Puntaje: {puntaje}"
            pregunta_texto.value = pregunta_actual["pregunta"]

            opciones.content.controls =[
                ft.Radio(value=str(i), label=op)
                for i, op in enumerate(pregunta_actual["opciones"])
            ]

            opciones.value = None
            mensaje.value = ""
            page.update()
        else:
            mostrar_resultado()

    def siguiente(e):
        nonlocal indice, puntaje

        if opciones.value is None:
            mensaje.value = "Selecciona una respuesta."
            page.update()
            return

        if int(opciones.value) == preguntas[indice]["respuesta"]:
            puntaje += 1
        else:
            puntaje -= 1

        indice += 1
        cargar_pregunta()

    def mostrar_resultado():
        guardar_resultado()

        page.controls.clear()

        page.add(
            ft.Column([
                    ft.Text("Quiz terminado 🎉", size=30, weight="bold"),
                    ft.Text(f"Jugador: {nombre_jugador}", size=20),
                    ft.Text(f"Puntos totales: {puntaje}", size=22),
                    ft.ElevatedButton("Reiniciar", on_click=reiniciar)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        page.update()

    def iniciar_quiz(e):
        nonlocal nombre_jugador

        if not nombre_input.value.strip():
            mensaje_inicio.value = "Escribe tu nombre."
            page.update()
            return

        nombre_jugador = nombre_input.value.strip()

        page.controls.clear()

        construir_vista_quiz()
        cargar_pregunta()

    def reiniciar(e):
        page.controls.clear()
        construir_vista_inicio()
        page.update()

    def construir_vista_inicio():
        page.add(
            ft.Column([
                    titulo,
                    ft.Text("Ingresa tu nombre para comenzar"),
                    nombre_input,
                    mensaje_inicio,
                    ft.ElevatedButton("Comenzar", on_click=iniciar_quiz)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def construir_vista_quiz():
        page.add(
            ft.Column([
                    titulo,
                    progreso,
                    jugador_texto,
                    puntaje_texto,
                    pregunta_texto,
                    opciones,
                    mensaje,
                    ft.ElevatedButton("Siguiente", on_click=siguiente)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    construir_vista_inicio()

ft.run(main)