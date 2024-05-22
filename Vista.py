import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import date
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
    cuotas = int(cuotas_entry.get())
    tasa_interes = float(tasa_entry.get())
    periodo_inicial = periodo_inicial_cal.get_date()
    periodo_final = periodo_final_cal.get_date()
    piy,pim,pid = map(int, str(periodo_inicial).split("-"))
    pfy, pfm,pfd = map(int, str(periodo_final).split("-"))

    if detalle.winfo_ismapped():
        detalle.place_forget()
    else:
        detalle.pack()
    valor_final_label.configure(text=f"Valor Final: {Renta.calcularValor(tasa_interes, cuotas, date(piy,pim,pid), date(pfy,pfm,pfd)):.02f}")
        
# Frame principal
frame = ctk.CTkFrame(master=root)
frame.pack(padx=20, pady=20,)
# Input para capturar las cuotas
cuotas_label = ctk.CTkLabel(master=frame, text="Cuotas:", font=("Roboto", 16))
cuotas_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
cuotas_entry = ctk.CTkEntry(master=frame,width=250, placeholder_text="Cantidad de cuotas")
cuotas_entry.grid(row=1, column=0, padx=10, pady=10)

# Input para capturar la tasa de interés efectiva mensual
tasa_label = ctk.CTkLabel(master=frame, text="Tasa de interés efectiva mensual:", font=("Roboto", 16))
tasa_label.grid(row=0, column=1, pady=10, sticky="w")
tasa_entry = ctk.CTkEntry(master=frame,width=250, placeholder_text="%")
tasa_entry.grid(row=1, column=1, padx=10, pady=10)

# Período inicial
periodo_inicial_label = ctk.CTkLabel(master=frame, text="Período inicial:", font=("Roboto", 16))
periodo_inicial_label.grid(row=2, column=0,padx=10, sticky="w")
periodo_inicial_cal = DateEntry(frame, selectmode='day',
                               date_pattern='yyyy-mm-dd')
periodo_inicial_cal.grid(row=3, column=0, padx=10, pady=5)

# Período final
periodo_final_label = ctk.CTkLabel(master=frame, text="Período final:", font=("Roboto", 16))
periodo_final_label.grid(row=2, column=1,padx=10, sticky="w")
periodo_final_cal = DateEntry(frame, selectmode='day',
                             date_pattern='yyyy-mm-dd')
periodo_final_cal.grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar datos
enviar_button = ctk.CTkButton(master=frame, text="Calcular", font=("Roboto", 16),command=verValorFinal)
enviar_button.grid(row=5, column=1, pady=10, padx=8)

# Botón con icono
# Agregar un botón con el carácter "<-"
boton_icono = ctk.CTkButton(master=frame, text="↔",width=3)
boton_icono.grid(row=5, column=0, pady=5)

# Ver detalle 
detalle = ctk.CTkFrame(master=root)
valor_final_label = ctk.CTkLabel(master=detalle, text="", font=("Roboto", 16))
valor_final_label.grid(row=0,column=0, padx=10,pady=20, sticky="w")
detalle.place_forget()