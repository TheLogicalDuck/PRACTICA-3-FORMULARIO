import flet as ft
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# ---------------------------
# 1) Cargar variables .env
# ---------------------------
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "escuela")
MONGO_COL = os.getenv("MONGO_COL", "registros")

if not MONGO_URI:
    raise RuntimeError("Falta MONGO_URI en tu archivo .env")

# ---------------------------
# 2) Conexión a MongoDB Atlas (UNA SOLA VEZ - más rápido)
# ---------------------------
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=3000,
    connectTimeoutMS=3000,
    socketTimeoutMS=5000,
)
col = client[MONGO_DB][MONGO_COL]


def main(page: ft.Page):
    page.title = "Práctica 3 — Formularios Estructurados con Modelo de Datos"
    page.window_width = 920
    page.window_height = 680
    page.padding = 20

    # Estado/mensajes
    status = ft.Text("", selectable=True)

    # Indicador de carga
    loading = ft.Row(
        controls=[ft.ProgressRing(), ft.Text("Cargando…")],
        visible=False,
        spacing=10,
    )

    # ---------------------------
    # Utilidades UI
    # ---------------------------
    def toast(msg: str, ok: bool = True):
        sb = ft.SnackBar(
            content=ft.Text(("✅ " if ok else "❌ ") + msg),
            open=True,
            duration=2200,
        )
        page.overlay.append(sb)
        page.update()

    def set_status(msg: str, ok: bool = True):
        status.value = ("✅ " if ok else "❌ ") + msg
        page.update()

    def set_loading(value: bool):
        loading.visible = value
        page.update()

    # ---------------------------
    # Formulario
    # ---------------------------
    txt_nombre = ft.TextField(label="Nombre", width=280)
    txt_grupo = ft.TextField(label="Grupo", width=160, hint_text="Ej. 3A")
    txt_correo = ft.TextField(label="Correo", width=280)

    # Búsqueda
    txt_buscar = ft.TextField(
        label="Buscar por nombre o grupo",
        width=420,
        hint_text="Ej. Luis o 3A",
    )

    # Tabla
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Grupo")),
            ft.DataColumn(ft.Text("Correo")),
            ft.DataColumn(ft.Text("Fecha")),
        ],
        rows=[],
    )

    # ---------------------------
    # Lógica: cargar datos
    # ---------------------------
    def cargar_datos(filtro: str = ""):
        set_loading(True)
        try:
            f = (filtro or "").strip()
            query = {}

            if f:
                query = {
                    "$or": [
                        {"nombre": {"$regex": f, "$options": "i"}},
                        {"grupo": {"$regex": f, "$options": "i"}},
                    ]
                }

            docs = list(
                col.find(query, {"nombre": 1, "grupo": 1, "correo": 1, "fecha": 1})
                .sort("fecha", -1)
                .limit(100)
            )

            tabla.rows.clear()
            for d in docs:
                fecha = d.get("fecha")
                fecha_txt = (
                    fecha.strftime("%Y-%m-%d %H:%M")
                    if isinstance(fecha, datetime)
                    else ""
                )

                tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(d.get("nombre", ""))),
                            ft.DataCell(ft.Text(d.get("grupo", ""))),
                            ft.DataCell(ft.Text(d.get("correo", ""))),
                            ft.DataCell(ft.Text(fecha_txt)),
                        ]
                    )
                )

            set_status(f"Registros cargados: {len(docs)}")
        except Exception as e:
            set_status(f"Error al cargar: {e}", ok=False)
            toast(f"Error al cargar: {e}", ok=False)
        finally:
            set_loading(False)

    def limpiar_form():
        txt_nombre.value = ""
        txt_grupo.value = ""
        txt_correo.value = ""
        page.update()

    # ---------------------------
    # Lógica: guardar
    # ---------------------------
    def guardar(e):
        nombre = (txt_nombre.value or "").strip()
        grupo = (txt_grupo.value or "").strip()
        correo = (txt_correo.value or "").strip()

        if not nombre or not grupo:
            toast("Nombre y Grupo son obligatorios.", ok=False)
            return

        set_loading(True)
        try:
            col.insert_one(
                {
                    "nombre": nombre,
                    "grupo": grupo,
                    "correo": correo,
                    "fecha": datetime.now(),
                }
            )

            toast("Registro guardado en Atlas.")
            set_status("Registro guardado correctamente.")
            limpiar_form()
            cargar_datos(txt_buscar.value)

        except Exception as ex:
            set_status(f"Error al guardar: {ex}", ok=False)
            toast(f"Error al guardar: {ex}", ok=False)
        finally:
            set_loading(False)

    def buscar(e):
        cargar_datos(txt_buscar.value)

    def refrescar(e):
        txt_buscar.value = ""
        page.update()
        cargar_datos("")

    # Botones
    btn_guardar = ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE, on_click=guardar)
    btn_buscar = ft.ElevatedButton("Buscar", icon=ft.Icons.SEARCH, on_click=buscar)
    btn_refrescar = ft.OutlinedButton("Refrescar", icon=ft.Icons.REFRESH, on_click=refrescar)

    # UI
    formulario = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("Registro de datos", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row([txt_nombre, txt_grupo, txt_correo], wrap=True),
                    ft.Row([btn_guardar], alignment=ft.MainAxisAlignment.END),
                ],
            ),
        )
    )

    visor = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("Visualización (MongoDB Atlas)", size=18, weight=ft.FontWeight.BOLD),
                    ft.Row([txt_buscar, btn_buscar, btn_refrescar], wrap=True),
                    loading,
                    ft.Container(
                        height=380,
                        content=ft.ListView(controls=[tabla]),
                    ),
                    status,
                ],
            ),
        )
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Práctica 3 — Diseño de Formularios Estructurados con Modelo de Datos",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text("Objetivo: registrar y visualizar datos dentro de la misma app."),
                formulario,
                visor,
            ],
            spacing=15,
        )
    )

    # Carga inicial
    cargar_datos("")


ft.app(target=main)