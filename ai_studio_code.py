import sys  # <--- ESTA LÍNEA FALTABA

def validar_dato(mensaje, min_fisico, max_fisico, umbral_alerta_min=None, umbral_alerta_max=None):
    """
    Valida input con criterios ajustados a la realidad experimental de la tesis.
    """
    while True:
        try:
            entrada = input(mensaje)
            if not entrada.strip(): continue
            valor = float(entrada)
            
            # 1. LÍMITE FÍSICO (Imposibles)
            if valor < min_fisico:
                print(f"   ⛔ ERROR FÍSICO: Valor menor a {min_fisico} no es posible.")
                continue
            if max_fisico is not None and valor > max_fisico:
                print(f"   ⛔ ERROR FÍSICO: Valor mayor a {max_fisico} no es posible.")
                continue

            # 2. LÍMITE OPERATIVO (Advertencias)
            advertencia = False
            msg = ""

            if umbral_alerta_min is not None and valor < umbral_alerta_min:
                msg = f"   ⚠️  ALERTA: Valor {valor} es muy BAJO respecto al estudio (Min exp: {umbral_alerta_min})."
                advertencia = True

            if umbral_alerta_max is not None and valor > umbral_alerta_max:
                msg = f"   ⚠️  ALERTA: Valor {valor} es muy ALTO respecto al estudio (Max exp aprox: {umbral_alerta_max})."
                advertencia = True

            if advertencia:
                print(msg)
                print("       El modelo lineal podría perder precisión.")
                confirmar = input("       ¿Confirmar uso de este valor? (s/n): ").strip().lower()
                if confirmar != 's':
                    continue 

            return valor

        except ValueError:
            print("   ❌ Error: Ingrese un número válido.")

def clasificar_recuperacion(valor):
    """
    Clasifica la eficiencia basada en los resultados históricos de la tesis (Anexo D).
    """
    if valor < 50.0:
        return "🔴 BAJA (Requiere Optimización)"
    elif 50.0 <= valor <= 75.0:
        return "🟡 MEDIA (Rango Estándar de Mezclas)"
    else:
        return "🟢 ALTA (Eficiencia Óptima)"

def solicitar_variables_comunes():
    print("\n   --- VARIABLES OPERATIVAS ---")
    
    # pH: Ajustado a 9.0 (Más allá cambia la química de sulfuros)
    x1 = validar_dato("1. pH de Pulpa [0-14]: ", 
                      min_fisico=0.0, max_fisico=14.0, 
                      umbral_alerta_min=4.0, umbral_alerta_max=9.0)
    
    # Sulfuros: 0-100% es el rango experimental completo
    x2 = validar_dato("2. % Sulfuros [0-100]: ", 
                      min_fisico=0.0, max_fisico=100.0)
    
    # Dosis: Mantenemos 150 (~2x del experimental)
    x4 = validar_dato("3. Dosis Colector (g/t): ", 
                      min_fisico=0.0, max_fisico=1000000.0, 
                      umbral_alerta_max=150.0)
    
    # Molienda: Bajado a 25 min (El exp era máx 12. 60 era excesivo)
    x5 = validar_dato("4. Tiempo Molienda (min): ", 
                      min_fisico=0.01, max_fisico=None, 
                      umbral_alerta_max=25.0)
    return x1, x2, x4, x5

def calcular_oro_flow():
    print("\n🌟 CÁLCULO DE ORO (Au)")
    x1, x2, x4, x5 = solicitar_variables_comunes()
    
    # Ley Au: Alerta en 20 g/t
    print("   --- VARIABLE ESPECÍFICA ---")
    x3 = validar_dato("5. Ley de Cabeza Au (g/t): ", 
                      min_fisico=0.0, max_fisico=1000000.0, 
                      umbral_alerta_max=20.0)
    
    y_au = 35.5 - (4.2 * x1) + (0.35 * x2) + (1.8 * x3) + (0.15 * x4) + (0.8 * x5)
    resultado = max(0.0, min(100.0, y_au))
    clasificacion = clasificar_recuperacion(resultado)
    
    print("\n" + "═"*50)
    print(f"💰 RECUPERACIÓN ORO: {resultado:.2f} %")
    print(f"📊 CLASIFICACIÓN:    {clasificacion}")
    
    if resultado == 100.0: 
        print("   (⚠️ Saturación del modelo alcanzada)")
    print("═" * 50)

def calcular_plata_flow():
    print("\n🌟 CÁLCULO DE PLATA (Ag)")
    x1, x2, x4, x5 = solicitar_variables_comunes()
    
    # Ley Ag: Alerta en 200 g/t
    print("   --- VARIABLE ESPECÍFICA ---")
    ley_ag = validar_dato("5. Ley de Cabeza Ag (g/t): ", 
                          min_fisico=0.0, max_fisico=1000000.0, 
                          umbral_alerta_max=200.0)
    
    y_ag = 30.0 - (3.8 * x1) + (0.40 * x2) + (0.05 * ley_ag) + (0.12 * x4) + (0.9 * x5)
    resultado = max(0.0, min(100.0, y_ag))
    clasificacion = clasificar_recuperacion(resultado)
    
    print("\n" + "═"*50)
    print(f"⚪ RECUPERACIÓN PLATA: {resultado:.2f} %")
    print(f"📊 CLASIFICACIÓN:      {clasificacion}")
    
    if resultado == 100.0: 
        print("   (⚠️ Saturación del modelo alcanzada)")
    print("═" * 50)

def main():
    while True:
        print("\n" + "█"*60)
        print("   SIMULADOR METALÚRGICO V7.1 (CON INTERPRETACIÓN)")
        print("█"*60)
        print("1. Calcular ORO (Au)")
        print("2. Calcular PLATA (Ag)")
        print("3. Salir")
        
        opcion = input("\n👉 Opción: ")

        if opcion == '3':
            print("Saliendo...")
            sys.exit() # Ahora funcionará correctamente
        elif opcion == '1':
            calcular_oro_flow()
        elif opcion == '2':
            calcular_plata_flow()
        else:
            print("❌ Opción inválida.")
            continue
            
        input("\n[Enter] para continuar...")

if __name__ == "__main__":
    main()