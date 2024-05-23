import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import date


# Default settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def verCuotas():
    pass

def devolverFrame()->ctk:
    return ventasGUI
ventasGUI = ctk.CTkFrame()

def cambiarVenta():
    ventasGUI.pack_forget()

cuotas_label = ctk.CTkLabel(master=ventasGUI, text="Cuotas:", font=("Roboto", 16))
cuotas_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
cuotas_entry = ctk.CTkEntry(master=ventasGUI,width=250, placeholder_text="$")
cuotas_entry.grid(row=1, column=0, padx=10, pady=10)

# Input para capturar la tasa de interés efectiva mensual
tasa_label = ctk.CTkLabel(master=ventasGUI, text="Tasa de interés efectiva mensual:", font=("Roboto", 16))
tasa_label.grid(row=0, column=1, pady=10, sticky="w")
tasa_entry = ctk.CTkEntry(master=ventasGUI,width=250, placeholder_text="%")
tasa_entry.grid(row=1, column=1, padx=10, pady=10)

# Período inicial
periodo_inicial_label = ctk.CTkLabel(master=ventasGUI, text="Período inicial:", font=("Roboto", 16))
periodo_inicial_label.grid(row=2, column=0,padx=10, sticky="w")
periodo_inicial_cal = DateEntry(ventasGUI, selectmode='day',
                               date_pattern='yyyy-mm-dd')
periodo_inicial_cal.grid(row=3, column=0, padx=10, pady=5)

# Período final
periodo_final_label = ctk.CTkLabel(master=ventasGUI, text="Período final:", font=("Roboto", 16))
periodo_final_label.grid(row=2, column=1,padx=10, sticky="w")
periodo_final_cal = DateEntry(ventasGUI, selectmode='day',
                             date_pattern='yyyy-mm-dd')
periodo_final_cal.grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar datos
enviar_button = ctk.CTkButton(master=ventasGUI, text="Calcular", font=("Roboto", 16),command=verCuotas)
enviar_button.grid(row=5, column=1, pady=10, padx=8)

# Botón con icono
# Agregar un botón con el carácter "<-"
boton_icono = ctk.CTkButton(master=ventasGUI, text="↔",width=3, command=cambiarVenta)
boton_icono.grid(row=5, column=0, pady=5)
