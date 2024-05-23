import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import date
from CTkMessagebox import CTkMessagebox

import Renta

# Default settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# Crear ventana principal
root = ctk.CTk()
root.title("Rentas")
root.geometry("700x450")
def run():
    root.mainloop()

def verValorFinal():
    try:
        cuotas = int(cuotas_entry.get())
        tasa_interes = float(tasa_entry.get())
        periodo_inicial = periodo_inicial_cal.get_date()
        periodo_final = periodo_final_cal.get_date()
        piy,pim,pid = map(int, str(periodo_inicial).split("-"))
        pfy, pfm,pfd = map(int, str(periodo_final).split("-"))

        detalleShowFade()
        valor_final_label.configure(text=f"Valor Final: {Renta.calcularValor(tasa_interes, cuotas, date(piy,pim,pid), date(pfy,pfm,pfd)):.02f}")
    except ValueError as e:
        CTkMessagebox(title="Error", message="Por favor, rellena los campos para continuar")
    

def detalleShowFade():
    if detalle.winfo_ismapped():
        detalle.pack_forget()
    else:
        detalle.pack()

def verCuotas():
    try:
        valor = int(cuotas_entryv.get())
        tasa_interes = float(tasa_entryv.get())
        periodo_inicial = periodo_inicial_calv.get_date()
        periodo_final = periodo_final_calv.get_date()
        piy,pim,pid = map(int, str(periodo_inicial).split("-"))
        pfy, pfm,pfd = map(int, str(periodo_final).split("-"))

        detalleShowFade()
        valor_final_label.configure(text=f"Valor de la cuota: {Renta.calcularCuotas(valor,tasa_interes, date(piy,pim,pid), date(pfy,pfm,pfd)):.02f}")
    except ValueError as e:
        CTkMessagebox(title="Error", message="Por favor, rellena los campos para continuar")
    
def cambiarCuotas():
    if cuotasGUI.winfo_ismapped():
        ctk.set_default_color_theme("green")
        cuotasGUI.pack_forget()
        ventasGUI.pack(padx=20, pady=20)
        detalle.pack_forget()
    else:
        ctk.set_default_color_theme("dark-blue")
        ventasGUI.pack_forget()
        cuotasGUI.pack(padx=20, pady=20)
        detalle.pack_forget()

# cuotasGUI principal
cuotasGUI = ctk.CTkFrame(master=root)
cuotasGUI.pack(padx=20, pady=20,)
# Input para capturar las cuotas
cuotas_label = ctk.CTkLabel(master=cuotasGUI, text="Cuotas:", font=("Roboto", 16))
cuotas_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
cuotas_entry = ctk.CTkEntry(master=cuotasGUI,width=250, placeholder_text="$")
cuotas_entry.grid(row=1, column=0, padx=10, pady=10)

# Input para capturar la tasa de interés efectiva mensual
tasa_label = ctk.CTkLabel(master=cuotasGUI, text="Tasa de interés efectiva mensual:", font=("Roboto", 16))
tasa_label.grid(row=0, column=1, pady=10, sticky="w")
tasa_entry = ctk.CTkEntry(master=cuotasGUI,width=250, placeholder_text="%")
tasa_entry.grid(row=1, column=1, padx=10, pady=10)

# Período inicial
periodo_inicial_label = ctk.CTkLabel(master=cuotasGUI, text="Período inicial:", font=("Roboto", 16))
periodo_inicial_label.grid(row=2, column=0,padx=10, sticky="w")
periodo_inicial_cal = DateEntry(cuotasGUI, selectmode='day',
                               date_pattern='yyyy-mm-dd', background="#0378A4")
periodo_inicial_cal.grid(row=3, column=0, padx=10, pady=5)

# Período final
periodo_final_label = ctk.CTkLabel(master=cuotasGUI, text="Período final:", font=("Roboto", 16))
periodo_final_label.grid(row=2, column=1,padx=10, sticky="w")
periodo_final_cal = DateEntry(cuotasGUI, selectmode='day',
                             date_pattern='yyyy-mm-dd', background="#0378A4")
periodo_final_cal.grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar datos
enviar_button = ctk.CTkButton(master=cuotasGUI, text="Calcular", font=("Roboto", 16),command=verValorFinal)
enviar_button.grid(row=5, column=1, pady=10, padx=8)

# Botón con icono
# Agregar un botón con el carácter "<-"
boton_icono = ctk.CTkButton(master=cuotasGUI, text="↔",width=3, command=cambiarCuotas)
boton_icono.grid(row=5, column=0, pady=5)
# ----------CUOTAS CALCULAR---------------
ventasGUI = ctk.CTkFrame(master=root)

cuotas_labelv = ctk.CTkLabel(master=ventasGUI, text="Valor final:", font=("Roboto", 16))
cuotas_labelv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
cuotas_entryv = ctk.CTkEntry(master=ventasGUI,width=250, placeholder_text="$")
cuotas_entryv.grid(row=1, column=0, padx=10, pady=10)

# Input para capturar la tasa de interés efectiva mensual
tasa_labelv = ctk.CTkLabel(master=ventasGUI, text="Tasa de interés efectiva mensual:", font=("Roboto", 16))
tasa_labelv.grid(row=0, column=1, pady=10, sticky="w")
tasa_entryv = ctk.CTkEntry(master=ventasGUI,width=250, placeholder_text="%")
tasa_entryv.grid(row=1, column=1, padx=10, pady=10)

# Período inicial
periodo_inicial_labelv = ctk.CTkLabel(master=ventasGUI, text="Período inicial:", font=("Roboto", 16))
periodo_inicial_labelv.grid(row=2, column=0,padx=10, sticky="w")
periodo_inicial_calv = DateEntry(ventasGUI, selectmode='day',
                               date_pattern='yyyy-mm-dd', background="#5DF9C1", text_color="#111")
periodo_inicial_calv.grid(row=3, column=0, padx=10, pady=5)

# Período final
periodo_final_labelv = ctk.CTkLabel(master=ventasGUI, text="Período final:", font=("Roboto", 16))
periodo_final_labelv.grid(row=2, column=1,padx=10, sticky="w")
periodo_final_calv = DateEntry(ventasGUI, selectmode='day',
                             date_pattern='yyyy-mm-dd', background="#5DF9C1", text_color="#111")
periodo_final_calv.grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar datos
enviar_buttonv = ctk.CTkButton(master=ventasGUI, text="Calcular",fg_color="#5DF9C1",text_color="black", font=("Roboto", 16),command=verCuotas)
enviar_buttonv.grid(row=5, column=1, pady=10, padx=8)

# Botón con icono
# Agregar un botón con el carácter "<-"
boton_iconov = ctk.CTkButton(master=ventasGUI, text="↔",width=3,fg_color="#5DF9C1",text_color="black", command=cambiarCuotas)
boton_iconov.grid(row=5, column=0, pady=5)

# Ver detalle 
detalle = ctk.CTkFrame(master=root)
valor_final_label = ctk.CTkLabel(master=detalle, text="", font=("Roboto", 16))
valor_final_label.grid(row=0,column=0, padx=10,pady=20, sticky="w")
detalle.place_forget()